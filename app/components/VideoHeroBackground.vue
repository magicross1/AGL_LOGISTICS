<script setup lang="ts">
// 完全避免 hydration 不匹配的方案
const isMounted = ref(false)

onMounted(() => {
  // 确保客户端完全加载后再显示视频
  nextTick(() => {
    isMounted.value = true
  })
})
</script>

<template>
  <!-- 使用固定的静态背景，避免 hydration 问题 -->
  <div class="hero-background">
    <!-- 静态背景图片，始终显示 -->
    <div class="static-background">
      <img
        src="/images/home.png"
        alt="AGL Logistics Background"
        class="background-image"
      />
    </div>
    
    <!-- 视频背景，仅在客户端挂载后显示 -->
    <div v-if="isMounted" class="video-background">
      <video
        autoplay
        muted
        loop
        playsinline
        preload="none"
        class="background-video"
      >
        <source src="/videos/home.mp4" type="video/mp4">
      </video>
    </div>
    
    <!-- 覆盖层 -->
    <div class="overlay-gradient"></div>
    <div class="overlay-contrast"></div>
    <div class="overlay-pattern"></div>
  </div>
</template>

<style scoped>
.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 0;
}

.static-background,
.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.background-image,
.background-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scale(1.05);
}

.video-background {
  animation: fadeIn 0.5s ease-in-out;
}

.background-video {
  z-index: 1;
}

.overlay-gradient {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.6));
  z-index: 2;
}

.overlay-contrast {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, rgba(0, 0, 0, 0.4), transparent, rgba(0, 0, 0, 0.4));
  z-index: 3;
}

.overlay-pattern {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.1) 1px, transparent 1px);
  background-size: 50px 50px;
  opacity: 0.1;
  z-index: 4;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
