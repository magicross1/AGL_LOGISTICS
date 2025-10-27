#!/usr/bin/env python3
"""
Nginx 配置部署脚本
专门用于快速部署 nginx.conf 配置文件，不涉及网页内容更新
"""

import os
import sys
import time
import paramiko
from types import SimpleNamespace

# =====================
# 配置（按需修改）
# =====================
HOST = "139.180.160.177"                 # 服务器 IP 或域名
PORT = 22                  # SSH 端口
USER = "root"                 # SSH 用户名
PASSWORD = "2X]f}!v#T6PtpUG8"            # SSH 密码
KEY = None                 # SSH 私钥路径（如果使用密钥认证）

# Nginx 配置文件路径
NGINX_CONF_LOCAL = "nginx.conf"           # 本地 nginx.conf 文件
NGINX_CONF_REMOTE = "/etc/nginx/nginx.conf"  # 远程 nginx.conf 文件路径

# 其他选项
RELOAD_NGINX = True         # True: 上传 nginx 配置后自动重载
BACKUP_CONFIG = True       # True: 备份原配置文件


def load_config():
    """加载配置并验证"""
    if not HOST or not USER or not NGINX_CONF_REMOTE:
        print("[ERROR] 请在脚本顶部配置 HOST、USER、NGINX_CONF_REMOTE", file=sys.stderr)
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
        nginx_conf_local=NGINX_CONF_LOCAL,
        nginx_conf_remote=NGINX_CONF_REMOTE,
        reload_nginx=RELOAD_NGINX,
        backup_config=BACKUP_CONFIG,
    )


def connect_ssh_sftp(host, port, user, password=None, key_path=None):
    """建立 SSH 和 SFTP 连接"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        if key_path:
            pkey = paramiko.RSAKey.from_private_key_file(key_path)
            ssh.connect(hostname=host, port=port, username=user, pkey=pkey, timeout=30)
        else:
            ssh.connect(hostname=host, port=port, username=user, password=password, timeout=30)
        sftp = ssh.open_sftp()
        return ssh, sftp
    except Exception as e:
        print(f"[ERROR] SSH/SFTP 连接失败: {e}", file=sys.stderr)
        sys.exit(2)


def backup_nginx_config(ssh, remote_path):
    """备份当前的 nginx 配置文件"""
    try:
        timestamp = int(time.time())
        backup_path = f"{remote_path}.backup.{timestamp}"
        print(f"[INFO] 备份当前 nginx 配置到 {backup_path}")
        
        stdin, stdout, stderr = ssh.exec_command(f"cp {remote_path} {backup_path}")
        stdout.read()  # 等待命令完成
        
        # 检查备份是否成功
        stdin, stdout, stderr = ssh.exec_command(f"ls -la {backup_path}")
        if stdout.read().decode().strip():
            print(f"[INFO] 备份成功: {backup_path}")
            return backup_path
        else:
            print(f"[WARN] 备份可能失败，但继续执行")
            return backup_path
    except Exception as e:
        print(f"[WARN] 备份失败: {e}")
        return None


def test_nginx_config(ssh):
    """测试 nginx 配置语法"""
    try:
        print("[INFO] 测试 nginx 配置语法...")
        stdin, stdout, stderr = ssh.exec_command("nginx -t")
        stdout_output = stdout.read().decode()
        stderr_output = stderr.read().decode()
        
        # nginx -t 成功时会在 stderr 中输出 "test is successful" 或 "syntax is ok"
        if "test is successful" in stderr_output or "syntax is ok" in stderr_output:
            print("[INFO] Nginx 配置语法测试通过")
            return True
        else:
            print(f"[ERROR] Nginx 配置语法测试失败:")
            print(f"STDOUT: {stdout_output}")
            print(f"STDERR: {stderr_output}")
            return False
    except Exception as e:
        print(f"[ERROR] 测试 nginx 配置时出错: {e}")
        return False


def upload_nginx_config(sftp, local_path, remote_path):
    """上传 nginx 配置文件"""
    try:
        print(f"[INFO] 上传 {local_path} 到 {remote_path}")
        sftp.put(local_path, remote_path)
        print("[INFO] 配置文件上传成功")
        return True
    except Exception as e:
        print(f"[ERROR] 上传配置文件失败: {e}")
        return False


def reload_nginx(ssh):
    """重载 nginx 配置"""
    try:
        print("[INFO] 重载 nginx 配置...")
        stdin, stdout, stderr = ssh.exec_command("nginx -s reload")
        stdout.read()  # 等待命令完成
        
        # 检查重载是否成功
        stdin, stdout, stderr = ssh.exec_command("ps aux | grep nginx | grep -v grep")
        if stdout.read().decode().strip():
            print("[INFO] Nginx 重载成功")
            return True
        else:
            print("[WARN] Nginx 进程可能未运行")
            return False
    except Exception as e:
        print(f"[ERROR] 重载 nginx 失败: {e}")
        return False


def restore_backup(ssh, backup_path, remote_path):
    """恢复备份的配置文件"""
    try:
        print(f"[INFO] 恢复备份配置: {backup_path}")
        stdin, stdout, stderr = ssh.exec_command(f"cp {backup_path} {remote_path}")
        stdout.read()  # 等待命令完成
        print("[INFO] 配置已恢复")
        return True
    except Exception as e:
        print(f"[ERROR] 恢复配置失败: {e}")
        return False


def main():
    """主函数"""
    args = load_config()
    
    # 检查本地配置文件是否存在
    if not os.path.exists(args.nginx_conf_local):
        print(f"[ERROR] 本地配置文件不存在: {args.nginx_conf_local}", file=sys.stderr)
        sys.exit(1)
    
    print(f"[INFO] 连接到 {args.user}@{args.host}:{args.port} ...")
    
    try:
        ssh, sftp = connect_ssh_sftp(args.host, args.port, args.user, args.password, args.key)
    except Exception as e:
        print(f"[ERROR] 连接失败: {e}", file=sys.stderr)
        sys.exit(2)
    
    backup_path = None
    
    try:
        # 1. 备份当前配置（如果启用）
        if args.backup_config:
            backup_path = backup_nginx_config(ssh, args.nginx_conf_remote)
        
        # 2. 上传新配置
        if not upload_nginx_config(sftp, args.nginx_conf_local, args.nginx_conf_remote):
            print("[ERROR] 上传配置文件失败")
            sys.exit(3)
        
        # 3. 测试配置语法
        if not test_nginx_config(ssh):
            print("[ERROR] 配置语法测试失败")
            # 恢复备份
            if backup_path:
                restore_backup(ssh, backup_path, args.nginx_conf_remote)
            sys.exit(4)
        
        # 4. 重载 nginx（如果启用）
        if args.reload_nginx:
            if not reload_nginx(ssh):
                print("[WARN] Nginx 重载失败，但配置已更新")
        
        print("[SUCCESS] Nginx 配置部署完成！")
        
    except Exception as e:
        print(f"[ERROR] 部署过程中出错: {e}", file=sys.stderr)
        # 尝试恢复备份
        if backup_path:
            restore_backup(ssh, backup_path, args.nginx_conf_remote)
        sys.exit(5)
    
    finally:
        try:
            sftp.close()
        except Exception:
            pass
        try:
            ssh.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()
