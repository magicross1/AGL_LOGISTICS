<script setup lang="ts">
const { data: page } = await useAsyncData('index', () => queryCollection('content').first())
if (!page.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
}

// 办公室数据
const offices = [
  {
    city: 'Sydney',
    status: 'active' as const,
    isHeadquarters: true,
    address: '6 Ladbroke Street, Milperra NSW 2214',
    phone: '+61 2 8747 3069',
    email: 'ops@agllogistics.com.au',
    description: 'Our headquarters serving NSW and eastern Australia with full-service logistics capabilities.',
    services: [
      'Full freight forwarding services',
      'Customs brokerage and clearance',
      'Air and sea freight operations',
      'Specialized transport coordination',
      'Secure warehouse facilities',
      '24/7 customer support'
    ]
  },
  {
    city: 'Melbourne',
    status: 'active' as const,
    isHeadquarters: false,
    address: '12 Hawthorn Avenue, Sunshine North VIC 3020',
    phone: '+61 3 9043 3143',
    email: 'melops@agllogistics.com.au',
    description: 'Serving Victoria and southern Australia with comprehensive logistics solutions.',
    services: [
      'Complete freight management',
      'Expert customs brokerage',
      'Multi-modal transport services',
      'Project cargo handling',
      'Distribution and storage',
      'Local logistics expertise'
    ]
  },
  {
    city: 'Brisbane',
    status: 'active' as const,
    isHeadquarters: false,
    address: 'U2/26 Navigator Pl, Hendra QLD 4011',
    phone: '+61 7 3555 1838',
    email: 'bneops@agllogistics.com.au',
    description: 'Queensland operations hub providing northern Australia coverage.',
    services: [
      'Air and sea freight services',
      'Customs documentation',
      'Regional distribution network',
      'Mining and resources logistics',
      'Temperature-controlled storage',
      'Express delivery options'
    ]
  },
  {
    city: 'Perth',
    status: 'coming_soon' as const,
    isHeadquarters: false,
    address: 'Coming Soon',
    phone: '+61 2 8747 3069',
    email: 'ops@agllogistics.com.au',
    description: 'Western Australia operations expanding soon to serve mining and resources sector.',
    services: [
      'Mining and resources expertise',
      'Bulk cargo handling',
      'International freight services',
      'Customs and quarantine',
      'Heavy machinery transport',
      'Remote area delivery'
    ]
  }
]

useSeoMeta({
  title: page.value.seo?.title || page.value.title,
  ogTitle: page.value.seo?.title || page.value.title,
  description: page.value.seo?.description || page.value.description,
  ogDescription: page.value.seo?.description || page.value.description
})
</script>

<template>
  <div
    v-if="page"
    class="relative"
  >

    <UPageHero
      :description="page.description"
      :links="page.hero.links"
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <VideoHeroBackground />
      </template>

      <template #title>
        <MDC
          :value="page.title"
          unwrap="p"
          class="text-white drop-shadow-lg"
        />
      </template>
    </UPageHero>

    <UPageSection
      :description="page.section.description"
      :features="page.section.features"
      orientation="horizontal"
      :ui="{
        container: 'lg:px-0 2xl:px-20 mx-0 max-w-none md:mr-10',
        features: 'gap-0'
      }"
      reverse
    >
      <template #title>
        <MDC
          :value="page.section.title"
          class="sm:*:leading-11"
        />
      </template>
      <img
        :src="page.section.images.desktop"
        :alt="page.section.title"
        class="hidden lg:block 2xl:hidden left-0 w-full max-w-2xl"
      >
      <img
        :src="page.section.images.mobile"
        :alt="page.section.title"
        class="block lg:hidden 2xl:block 2xl:w-full 2xl:max-w-2xl"
      >
    </UPageSection>

    <USeparator :ui="{ border: 'border-primary/30' }" />

    <UPageSection
      id="services"
      :description="page.features.description"
      :features="page.features.features"
      :ui="{
        title: 'text-left @container relative flex',
        description: 'text-left'
      }"
      class="relative overflow-hidden"
    >
      <div class="absolute rounded-full -left-10 top-10 size-[300px] z-10 bg-primary opacity-30 blur-[200px]" />
      <div class="absolute rounded-full -right-10 -bottom-10 size-[300px] z-10 bg-primary opacity-30 blur-[200px]" />
      <template #title>
        <MDC
          :value="page.features.title"
          class="*:leading-9"
        />
        <div class="hidden @min-[1020px]:block">
          <UColorModeImage
            light="/images/light/line-2.svg"
            dark="/images/dark/line-2.svg"
            class="absolute top-0 right-0 size-full transform scale-95 translate-x-[70%]"
          />
        </div>
      </template>
    </UPageSection>

    <USeparator :ui="{ border: 'border-primary/30' }" />

    <UPageSection
      id="steps"
      :description="page.steps.description"
      class="relative overflow-hidden"
    >
      <template #headline>
        <UColorModeImage
          light="/images/light/line-3.svg"
          dark="/images/dark/line-3.svg"
          class="absolute -top-10 sm:top-0 right-1/2 h-24"
        />
      </template>
      <template #title>
        <MDC :value="page.steps.title" />
      </template>

      <template #features>
        <UPageCard
          v-for="(step, index) in page.steps.items"
          :key="index"
          class="group"
          :ui="{ container: 'p-4 sm:p-4', title: 'flex items-center gap-1' }"
        >
          <UColorModeImage
            v-if="step.image"
            :light="step.image?.light"
            :dark="step.image?.dark"
            :alt="step.title"
            class="size-full"
          />

          <div class="flex flex-col gap-2">
            <span class="text-lg font-semibold">
              {{ step.title }}
            </span>
            <span class="text-sm text-muted">
              {{ step.description }}
            </span>
          </div>
        </UPageCard>
      </template>
    </UPageSection>

    <!-- Office Locations Section -->
    <OfficeLocations 
      :offices="offices" 
      variant="tech"
      title="Our Australian Network"
      description="Strategically located across Australia's major cities to serve your logistics needs with local expertise and global reach."
    />

    <!-- Enhanced Testimonials Section with Scrolling -->
    <UPageSection
      id="testimonials"
      class="bg-white dark:bg-gray-900 py-8 lg:py-12"
    >
      <!-- Custom Title and Description -->
      <UContainer>
        <div class="text-center mb-10">
          <h2 v-if="page.testimonials?.title" class="text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-black text-gray-900 dark:text-white mb-6 leading-tight tracking-tight drop-shadow-lg">
            <MDC :value="page.testimonials.title" />
          </h2>
          <h2 v-else class="text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-black text-gray-900 dark:text-white mb-6 leading-tight tracking-tight drop-shadow-lg">
            Trusted by <span class="bg-gradient-to-r from-blue-600 via-primary to-purple-600 bg-clip-text text-transparent animate-pulse">businesses</span> across Australia
          </h2>
          
          <p v-if="page.testimonials?.description" class="text-xl md:text-2xl lg:text-3xl text-gray-600 dark:text-gray-300 max-w-5xl mx-auto leading-relaxed font-semibold drop-shadow-sm">
            {{ page.testimonials.description }}
          </p>
          <p v-else class="text-xl md:text-2xl lg:text-3xl text-gray-600 dark:text-gray-300 max-w-5xl mx-auto leading-relaxed font-semibold drop-shadow-sm">
            See how companies are <span class="text-primary font-bold">streamlining</span> their supply chains and achieving <span class="text-primary font-bold">logistics excellence</span> with AGL Logistics.
          </p>
        </div>
      </UContainer>

      <!-- Scrolling Testimonials Container -->
      <div class="relative overflow-hidden">
        <!-- Gradient overlays for fade effect -->
        <div class="absolute left-0 top-0 bottom-0 w-20 bg-gradient-to-r from-white to-transparent dark:from-gray-900 dark:to-transparent z-10"></div>
        <div class="absolute right-0 top-0 bottom-0 w-20 bg-gradient-to-l from-white to-transparent dark:from-gray-900 dark:to-transparent z-10"></div>
        
        <!-- Scrolling Container -->
        <div class="flex animate-scroll space-x-6 py-8">
          <!-- First set of testimonials -->
          <div
            v-for="(testimonial, index) in page.testimonials?.items || []"
            :key="`first-${index}`"
            class="flex-shrink-0 w-96"
          >
            <UCard class="h-full bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm border border-gray-200/50 dark:border-gray-700/50 shadow-lg hover:shadow-xl transition-shadow duration-300">
              <div class="space-y-4">
                <!-- Rating Stars -->
                <div class="flex items-center gap-1">
                  <UIcon
                    v-for="star in 5"
                    :key="star"
                    name="lucide:star"
                    class="w-4 h-4 text-yellow-400 fill-current"
                  />
                </div>
                
                <!-- Quote -->
                <blockquote class="text-gray-700 dark:text-gray-300 italic leading-relaxed">
                  "{{ testimonial.quote }}"
                </blockquote>
                
                <!-- User Info -->
                <div class="flex items-center gap-4 pt-4 border-t border-gray-200 dark:border-gray-700">
                  <img
                    :src="testimonial.user.avatar.src"
                    :alt="testimonial.user.name"
                    class="w-12 h-12 rounded-full object-cover"
                  />
                  <div>
                    <div class="font-semibold text-gray-900 dark:text-gray-100">{{ testimonial.user.name }}</div>
                    <div class="text-sm text-gray-600 dark:text-gray-400">{{ testimonial.user.description }}</div>
                  </div>
                </div>
              </div>
            </UCard>
          </div>
          
          <!-- Duplicate set for seamless loop -->
          <div
            v-for="(testimonial, index) in page.testimonials?.items || []"
            :key="`second-${index}`"
            class="flex-shrink-0 w-96"
          >
            <UCard class="h-full bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm border border-gray-200/50 dark:border-gray-700/50 shadow-lg hover:shadow-xl transition-shadow duration-300">
              <div class="space-y-4">
                <!-- Rating Stars -->
                <div class="flex items-center gap-1">
                  <UIcon
                    v-for="star in 5"
                    :key="star"
                    name="lucide:star"
                    class="w-4 h-4 text-yellow-400 fill-current"
                  />
                </div>
                
                <!-- Quote -->
                <blockquote class="text-gray-700 dark:text-gray-300 italic leading-relaxed">
                  "{{ testimonial.quote }}"
                </blockquote>
                
                <!-- User Info -->
                <div class="flex items-center gap-4 pt-4 border-t border-gray-200 dark:border-gray-700">
                  <img
                    :src="testimonial.user.avatar.src"
                    :alt="testimonial.user.name"
                    class="w-12 h-12 rounded-full object-cover"
                  />
                  <div>
                    <div class="font-semibold text-gray-900 dark:text-gray-100">{{ testimonial.user.name }}</div>
                    <div class="text-sm text-gray-600 dark:text-gray-400">{{ testimonial.user.description }}</div>
                  </div>
                </div>
              </div>
            </UCard>
          </div>
        </div>
      </div>
      
    </UPageSection>


    <UPageCTA
      v-bind="page.cta"
      variant="naked"
      class="overflow-hidden @container"
    >
      <template #title>
        <MDC :value="page.cta.title" />

        <div class="@max-[1280px]:hidden">
          <UColorModeImage
            light="/images/light/line-6.svg"
            dark="/images/dark/line-6.svg"
            class="absolute left-10 -top-10 sm:top-0 h-full"
          />
          <UColorModeImage
            light="/images/light/line-7.svg"
            dark="/images/dark/line-7.svg"
            class="absolute right-0 bottom-0 h-full"
          />
        </div>
      </template>

      <LazyStarsBg />
    </UPageCTA>
  </div>
</template>
