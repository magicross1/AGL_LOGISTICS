<script setup lang="ts">
// 简化脚本，避免水合不匹配
const videoRef = ref<HTMLVideoElement>()

// 确保视频在客户端正确播放
function handleVideoPlay() {
  if (process.client && videoRef.value) {
    videoRef.value.play().catch(() => {
      // Autoplay failed, but that's okay
    })
  }
}

onMounted(() => {
  // 延迟确保DOM完全加载
  setTimeout(() => {
    handleVideoPlay()
  }, 500)
})
</script>

<template>
  <div class="absolute inset-0 overflow-hidden">
    <!-- Video Background -->
    <ClientOnly>
      <video
        ref="videoRef"
        autoplay
        muted
        loop
        playsinline
        preload="metadata"
        class="absolute inset-0 w-full h-full object-cover scale-105"
        @loadeddata="handleVideoPlay"
        @canplay="handleVideoPlay"
      >
        <source src="/videos/home.mp4" type="video/mp4">
      </video>
      
      <template #fallback>
        <!-- 服务端渲染时的静态背景 -->
        <div class="absolute inset-0 bg-gradient-to-br from-primary/30 via-primary/20 to-primary/10"></div>
      </template>
    </ClientOnly>
    
    <!-- Video Overlay for better text readability -->
    <div class="absolute inset-0 bg-gradient-to-b from-black/50 via-black/30 to-black/60"></div>
    
    <!-- Additional overlay for text contrast -->
    <div class="absolute inset-0 bg-gradient-to-r from-black/40 via-transparent to-black/40"></div>
    
    <!-- Subtle pattern overlay for depth -->
    <div class="absolute inset-0 opacity-10">
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(255,255,255,0.1)_1px,transparent_1px)] bg-[length:50px_50px]"></div>
    </div>
  </div>
</template>
