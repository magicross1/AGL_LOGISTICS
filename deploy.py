from types import SimpleNamespace
import os
import posixpath
import shutil
import sys
from stat import S_ISDIR
import paramiko
import tempfile
import time

# =====================
# 配置（按需修改）
# =====================
HOST = "139.180.160.177"                 # 服务器 IP 或域名，例如: "203.0.113.10"
PORT = 22                  # SSH 端口
USER = "root"                 # SSH 用户名
# 认证：二选一，设置 PASSWORD 或 KEY（私钥路径），另一个保持为空
PASSWORD = "2X]f}!v#T6PtpUG8"            # 例如: "your_password"
KEY = None                 # 例如: r"C:\\Users\\you\\.ssh\\id_rsa" 或 "/home/you/.ssh/id_rsa"

# 本地打包目录（默认 Nuxt 静态构建产物）
LOCAL_DIR = os.path.join(".output", "public")

# 远端部署目录（绝对路径）
REMOTE_DIR = "/var/www/agl/public"           # AGL 项目独立部署目录

# 其他开关
NO_CLEAN_REMOTE = False    # True: 不清空远端目录，只覆盖同名文件
DELETE_LOCAL_AFTER = False # True: 上传完成后删除本地目录
UPLOAD_NGINX_CONFIG = True # True: 上传 nginx.conf 到 /etc/nginx/
RELOAD_NGINX = True         # True: 上传 nginx 配置后自动重载


def load_config():
    # 基本校验
    if not HOST or not USER or not REMOTE_DIR:
        print("[ERROR] 请在 deploy.py 顶部配置 HOST、USER、REMOTE_DIR", file=sys.stderr)
        sys.exit(1)
    if not PASSWORD and not KEY:
        print("[ERROR] 请设置 PASSWORD 或 KEY（二选一）", file=sys.stderr)
        sys.exit(1)
    return SimpleNamespace(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        key=KEY,
        local_dir=LOCAL_DIR,
        remote_dir=REMOTE_DIR,
        no_clean_remote=NO_CLEAN_REMOTE,
        delete_local_after=DELETE_LOCAL_AFTER,
        upload_nginx_config=UPLOAD_NGINX_CONFIG,
        reload_nginx=RELOAD_NGINX,
    )


def connect_ssh_sftp(host, port, user, password=None, key_path=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if key_path:
        pkey = paramiko.RSAKey.from_private_key_file(key_path)
        ssh.connect(hostname=host, port=port, username=user, pkey=pkey, timeout=30)
    else:
        ssh.connect(hostname=host, port=port, username=user, password=password, timeout=30)
    sftp = ssh.open_sftp()
    return ssh, sftp


def sftp_path_exists(sftp: paramiko.SFTPClient, path: str) -> bool:
    try:
        sftp.stat(path)
        return True
    except IOError:
        return False


def sftp_mkdirs(sftp: paramiko.SFTPClient, path: str):
    # Create directories recursively on remote (POSIX style path)
    parts = [p for p in path.split("/") if p not in ("", ".")]
    cur = "/" if path.startswith("/") else ""
    for part in parts:
        cur = posixpath.join(cur, part) if cur else part
        try:
            sftp.stat(cur)
        except IOError:
            sftp.mkdir(cur)


def sftp_rmdir_recursive(sftp: paramiko.SFTPClient, remote_path: str):
    # Remove directory tree (files and subdirs)
    try:
        for entry in sftp.listdir_attr(remote_path):
            entry_path = posixpath.join(remote_path, entry.filename)
            if S_ISDIR(entry.st_mode):
                sftp_rmdir_recursive(sftp, entry_path)
            else:
                sftp.remove(entry_path)
        sftp.rmdir(remote_path)
    except IOError:
        # If not a directory, try remove as file
        try:
            sftp.remove(remote_path)
        except Exception:
            pass


def sftp_clear_directory(sftp: paramiko.SFTPClient, remote_dir: str):
    # Ensure remote_dir exists; then delete its contents (but keep directory)
    if not sftp_path_exists(sftp, remote_dir):
        sftp_mkdirs(sftp, remote_dir)
        return
    for entry in sftp.listdir_attr(remote_dir):
        entry_path = posixpath.join(remote_dir, entry.filename)
        if S_ISDIR(entry.st_mode):
            sftp_rmdir_recursive(sftp, entry_path)
        else:
            sftp.remove(entry_path)


def upload_directory(sftp: paramiko.SFTPClient, local_dir: str, remote_dir: str):
    for root, dirs, files in os.walk(local_dir):
        # Map local path to remote path
        rel = os.path.relpath(root, start=local_dir)
        rel = "" if rel == "." else rel.replace("\\", "/")
        remote_path = remote_dir if not rel else posixpath.join(remote_dir, rel)
        sftp_mkdirs(sftp, remote_path)
        for f in files:
            local_file = os.path.join(root, f)
            remote_file = posixpath.join(remote_path, f)
            sftp.put(local_file, remote_file)


def make_local_zip(source_dir: str) -> str:
    base = os.path.join(tempfile.gettempdir(), f"deploy_{int(time.time())}")
    zip_path = shutil.make_archive(base_name=base, format="zip", root_dir=source_dir)
    return zip_path


def detect_remote_os(ssh: paramiko.SSHClient) -> str:
    # Try Unix first
    try:
        stdin, stdout, stderr = ssh.exec_command("uname -s", timeout=15)
        out = stdout.read().decode(errors="ignore").strip().lower()
        if out:
            return "unix"
    except Exception:
        pass
    # Fallback to Windows (PowerShell)
    try:
        stdin, stdout, stderr = ssh.exec_command("powershell -NoProfile -Command \"$PSVersionTable.PSVersion.ToString()\"", timeout=15)
        out = stdout.read().decode(errors="ignore").strip()
        if out:
            return "windows"
    except Exception:
        pass
    # Default to unix
    return "unix"


def upload_nginx_config(sftp, ssh):
    """上传 nginx.conf 到服务器并备份原配置"""
    nginx_conf_local = "nginx.conf"
    nginx_conf_remote = "/etc/nginx/nginx.conf"
    
    if not os.path.exists(nginx_conf_local):
        print(f"[WARN] nginx.conf not found in current directory, skipping nginx config upload")
        return False
    
    try:
        # 备份原配置
        backup_path = f"/etc/nginx/nginx.conf.backup.{int(time.time())}"
        print(f"[INFO] Backing up current nginx config to {backup_path}")
        stdin, stdout, stderr = ssh.exec_command(f"cp {nginx_conf_remote} {backup_path}")
        stdout.read()  # 等待命令完成
        
        # 上传新配置
        print(f"[INFO] Uploading nginx.conf to {nginx_conf_remote}")
        sftp.put(nginx_conf_local, nginx_conf_remote)
        
        # 测试配置
        print("[INFO] Testing nginx configuration...")
        stdin, stdout, stderr = ssh.exec_command("nginx -t")
        test_output = stdout.read().decode()
        error_output = stderr.read().decode()
        
        # 检查配置是否成功（nginx -t 成功时会在 stderr 中输出 "test is successful"）
        if "test is successful" in error_output or "syntax is ok" in error_output:
            print("[INFO] Nginx configuration test passed")
            return True
        else:
            print(f"[ERROR] Nginx configuration test failed:")
            print(f"STDOUT: {test_output}")
            print(f"STDERR: {error_output}")
            # 恢复备份
            print("[INFO] Restoring backup configuration...")
            stdin, stdout, stderr = ssh.exec_command(f"cp {backup_path} {nginx_conf_remote}")
            stdout.read()
            return False
            
    except Exception as e:
        print(f"[ERROR] Failed to upload nginx config: {e}")
        return False


def reload_nginx(ssh):
    """重载 nginx 配置"""
    try:
        print("[INFO] Reloading nginx configuration...")
        stdin, stdout, stderr = ssh.exec_command("nginx -s reload")
        stdout.read()  # 等待命令完成
        print("[INFO] Nginx reloaded successfully")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to reload nginx: {e}")
        return False


def deploy_zip_unix(ssh: paramiko.SSHClient, remote_dir_posix: str, remote_zip_posix: str):
    # Use unzip; ensure remote_dir is replaced freshly
    cmd = f"set -e; rm -rf '{remote_dir_posix}' && mkdir -p '{remote_dir_posix}' && unzip -q -o '{remote_zip_posix}' -d '{remote_dir_posix}' && rm -f '{remote_zip_posix}'"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode(errors="ignore")
    err = stderr.read().decode(errors="ignore")
    rc = stdout.channel.recv_exit_status()
    if rc != 0:
        raise RuntimeError(f"Remote unix deploy failed (rc={rc}). stderr: {err or out}")


def deploy_zip_windows(ssh: paramiko.SSHClient, remote_dir_posix: str, remote_zip_posix: str):
    # Convert to Windows-style paths for PowerShell
    dst = remote_dir_posix.replace('/', '\\')
    zf = remote_zip_posix.replace('/', '\\')
    ps = (
        "$ErrorActionPreference='Stop'; "
        f"if (Test-Path -LiteralPath '{dst}') {{ Remove-Item -LiteralPath '{dst}' -Recurse -Force }}; "
        f"New-Item -ItemType Directory -Path '{dst}' -Force | Out-Null; "
        f"Expand-Archive -Path '{zf}' -DestinationPath '{dst}' -Force; "
        f"Remove-Item -LiteralPath '{zf}' -Force"
    )
    cmd = f"powershell -NoProfile -Command \"{ps}\""
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode(errors="ignore")
    err = stderr.read().decode(errors="ignore")
    rc = stdout.channel.recv_exit_status()
    if rc != 0:
        raise RuntimeError(f"Remote windows deploy failed (rc={rc}). stderr: {err or out}")


def main():
    args = load_config()

    local_dir = os.path.abspath(args.local_dir)
    if not os.path.isdir(local_dir):
        print(f"[ERROR] Local directory not found: {local_dir}", file=sys.stderr)
        sys.exit(1)

    # Always use POSIX path for SFTP remote paths
    remote_dir = args.remote_dir.replace("\\", "/")

    print(f"[INFO] Connecting to {args.user}@{args.host}:{args.port} ...")
    try:
        ssh, sftp = connect_ssh_sftp(args.host, args.port, args.user, args.password, args.key)
    except Exception as e:
        print(f"[ERROR] SSH/SFTP connection failed: {e}", file=sys.stderr)
        sys.exit(2)

    try:
        # 1) 先压缩本地目录
        print(f"[INFO] Zipping local directory: {local_dir}")
        os.system(f"pnpm generate")
        zip_path = make_local_zip(local_dir)
        print(f"[INFO] Created zip: {zip_path}")

        # 2) 上传 zip 到远端临时位置
        remote_zip = posixpath.join("/tmp", os.path.basename(zip_path))
        # 如果远端是 Windows，/tmp 不存在，放到目标目录同级
        try:
            sftp.stat("/tmp")
        except IOError:
            remote_zip = posixpath.join(remote_dir, os.path.basename(zip_path))

        print(f"[INFO] Uploading zip -> {remote_zip}")
        sftp_mkdirs(sftp, posixpath.dirname(remote_zip))
        sftp.put(zip_path, remote_zip)

        # 3) 远端解压&清理
        os_type = detect_remote_os(ssh)
        print(f"[INFO] Remote OS detected: {os_type}")
        if os_type == "windows":
            deploy_zip_windows(ssh, remote_dir, remote_zip)
        else:
            deploy_zip_unix(ssh, remote_dir, remote_zip)
        print("[INFO] Remote deploy finished successfully.")

        # 4) 上传 nginx 配置（如果启用）
        if args.upload_nginx_config:
            print("[INFO] Uploading nginx configuration...")
            nginx_success = upload_nginx_config(sftp, ssh)
            if nginx_success and args.reload_nginx:
                reload_nginx(ssh)
            elif not nginx_success:
                print("[WARN] Nginx configuration upload failed, but deployment completed")

    except Exception as e:
        print(f"[ERROR] Upload failed: {e}", file=sys.stderr)
        sys.exit(3)
    finally:
        try:
            sftp.close()
        except Exception:
            pass
        try:
            ssh.close()
        except Exception:
            pass

    if args.delete_local_after:
        try:
            print(f"[INFO] Deleting local directory: {local_dir}")
            shutil.rmtree(local_dir)
        except Exception as e:
            print(f"[WARN] Failed to delete local directory: {e}", file=sys.stderr)

    print("[DONE]")


if __name__ == "__main__":
    main()
