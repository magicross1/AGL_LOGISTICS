# LOGO 更换指南

## 当前LOGO位置
LOGO文件位于：`app/components/AppLogo.vue`

## 更换方法

### 方法1：使用图片文件（推荐）
1. 将您的LOGO图片文件放到 `public/images/` 目录下，例如：`public/images/agl-logo.png`

2. 修改 `app/components/AppLogo.vue` 文件，将第3-24行的SVG代码替换为：
```vue
<img 
  src="/images/agl-logo.png" 
  alt="AGL LOGISTICS" 
  class="w-10 h-10 object-contain"
/>
```

### 方法2：使用SVG文件
1. 将您的SVG文件放到 `public/images/` 目录下，例如：`public/images/agl-logo.svg`

2. 修改 `app/components/AppLogo.vue` 文件，将第3-24行的SVG代码替换为：
```vue
<img 
  src="/images/agl-logo.svg" 
  alt="AGL LOGISTICS" 
  class="w-10 h-10 object-contain text-primary"
/>
```

### 方法3：直接替换SVG代码
如果您有SVG代码，直接替换第3-24行的整个SVG标签内容即可。

## 注意事项
- 建议LOGO尺寸保持在40x40像素左右
- 支持的图片格式：PNG, JPG, SVG
- SVG格式可以更好地适应深色/浅色主题
- 如果使用PNG/JPG，建议使用透明背景

## 当前LOGO配置
- 尺寸：40x40px
- 颜色：跟随主题色（text-primary）
- 位置：导航栏左侧，AGL LOGISTICS文字旁边

## 文字部分调整
如果需要调整"AGL LOGISTICS"文字样式，修改第25-28行：
```vue
<div class="flex flex-col">
  <span class="text-2xl font-bold text-primary tracking-wider">AGL</span>
  <span class="text-sm font-medium text-muted-foreground -mt-1 tracking-widest">LOGISTICS</span>
</div>
```

可调整的属性：
- `text-2xl` - 字体大小
- `font-bold` - 字体粗细
- `tracking-wider` - 字母间距
- `text-primary` - 颜色
