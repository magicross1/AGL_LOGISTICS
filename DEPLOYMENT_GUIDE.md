# AGL Logistics 部署指南

## 部署目标
将 AGL Logistics 项目部署到 `https://www.bsbtransport.com.au/agl`

## 部署架构
- **主网站**: `/var/www/bsbtransport/public` - 处理根路径 `/`
- **AGL 应用**: `/var/www/agl/public` - 处理子路径 `/agl/`

## 部署步骤

### 1. 构建项目
```bash
# 安装依赖
npm install

# 构建静态文件
npm run build
```

### 2. 部署到服务器
```bash
# 运行部署脚本（会自动上传 nginx 配置）
python deploy.py
```

**部署脚本功能**：
- ✅ 构建并上传 AGL 应用到 `/var/www/agl/public`
- ✅ 自动上传 `nginx.conf` 到 `/etc/nginx/nginx.conf`
- ✅ 备份原 nginx 配置文件
- ✅ 测试 nginx 配置语法
- ✅ 自动重载 nginx 服务

### 3. 服务器配置

#### Nginx 配置
- 配置文件已更新为 `nginx.conf`
- 支持 HTTPS 和 HTTP 到 HTTPS 的重定向
- 配置了 `/agl/` 子路径支持，指向独立目录
- 包含完整的 SSL 安全配置

#### SSL 证书
确保以下证书文件存在：
- `/etc/nginx/ssl/bsb.cert` - SSL 证书文件
- `/etc/nginx/ssl/bsb.key` - SSL 私钥文件

#### 部署目录结构
```
/var/www/
├── bsbtransport/public/     # 主网站
│   ├── index.html
│   └── ...
└── agl/public/              # AGL 子应用
    ├── 200.html             # SPA 回退页面
    ├── _nuxt/               # Nuxt 构建资源
    └── ...                  # 其他静态资源
```

### 4. 验证部署

#### 检查 HTTPS 配置
- 访问 `https://www.bsbtransport.com.au` 应该加载主网站
- 访问 `https://www.bsbtransport.com.au/agl` 应该加载 AGL 应用
- HTTP 请求应该自动重定向到 HTTPS
- SSL 证书应该有效且安全

#### 检查功能
- 主网站和 AGL 应用都应该正常工作
- SPA 路由应该正常工作
- 静态资源应该正确加载
- 缓存策略应该生效

## 配置说明

### Nuxt 配置
- `baseURL: '/agl/'` - 确保所有资源路径正确
- 预渲染路由已配置

### Nginx 配置特点
- **HTTPS 强制**: HTTP 自动重定向到 HTTPS
- **独立目录**: 主网站和 AGL 应用使用不同的部署目录
- **子路径支持**: `/agl/` 路径指向 `/var/www/agl/public/`
- **SPA 支持**: 回退到 `200.html` 处理客户端路由
- **静态资源优化**: 长期缓存策略
- **安全头**: 完整的 HTTPS 安全配置

### 部署脚本配置
- 目标路径: `/var/www/agl/public`
- 支持增量部署
- 自动清理和同步
- **自动上传 nginx 配置**: 部署时自动上传 `nginx.conf` 到 `/etc/nginx/`
- **配置备份**: 自动备份原 nginx 配置
- **配置测试**: 上传前测试 nginx 配置语法
- **自动重载**: 配置上传成功后自动重载 nginx

## 故障排除

### 常见问题
1. **SSL 证书错误**: 检查证书文件路径和权限
2. **404 错误**: 确认部署路径和 nginx 配置匹配
3. **静态资源加载失败**: 检查 `_nuxt` 目录权限
4. **SPA 路由不工作**: 确认 `200.html` 文件存在
5. **主网站和 AGL 冲突**: 确认两个目录独立部署
6. **Nginx 配置上传失败**: 检查 `nginx.conf` 文件是否存在
7. **Nginx 配置测试失败**: 检查配置语法错误
8. **Nginx 重载失败**: 检查 nginx 服务状态

### 调试命令
```bash
# 检查 nginx 配置
nginx -t

# 重新加载 nginx
nginx -s reload

# 查看 nginx 错误日志
tail -f /var/log/nginx/error.log

# 查看 nginx 访问日志
tail -f /var/log/nginx/access.log

# 检查 nginx 服务状态
systemctl status nginx

# 检查文件权限
ls -la /var/www/bsbtransport/public/
ls -la /var/www/agl/public/

# 检查目录结构
tree /var/www/bsbtransport/public/
tree /var/www/agl/public/

# 查看 nginx 配置备份
ls -la /etc/nginx/nginx.conf.backup.*

## 安全注意事项
- SSL 证书定期更新
- 定期检查安全头配置
- 监控访问日志
- 保持 nginx 和系统更新
- 确保两个部署目录的权限正确
