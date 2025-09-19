<script setup lang="ts">
const nuxtApp = useNuxtApp()
const { activeHeadings, updateHeadings } = useScrollspy()

const items = computed(() => [{
  label: 'Home',
  to: '/',
  icon: 'lucide:home'
}, {
  label: 'Services',
  icon: 'lucide:truck',
  children: [{
    label: 'Air Freight',
    to: '/services/air-freight',
    description: 'Fast and reliable air cargo services',
    icon: 'lucide:plane'
  }, {
    label: 'Sea Freight', 
    to: '/services/sea-freight',
    description: 'Cost-effective ocean freight solutions',
    icon: 'lucide:ship'
  }, {
    label: 'Special Transports',
    to: '/services/special-transports', 
    description: 'Specialized handling for oversized cargo',
    icon: 'lucide:truck'
  }, {
    label: 'Customs Brokerage',
    to: '/services/customs-brokerage',
    description: 'Expert customs clearance services',
    icon: 'lucide:clipboard-check'
  }, {
    label: 'Storage Solutions',
    to: '/services/storage',
    description: 'Secure warehouse and distribution',
    icon: 'lucide:warehouse'
  }]
}, {
  label: 'Offices',
  icon: 'lucide:building-2',
  children: [{
    label: 'Sydney',
    to: '/offices/sydney',
    description: 'Head office serving NSW and eastern Australia',
    icon: 'lucide:star'
  }, {
    label: 'Melbourne',
    to: '/offices/melbourne',
    description: 'Victoria and southern Australia operations',
    icon: 'lucide:building'
  }, {
    label: 'Brisbane',
    to: '/offices/brisbane',
    description: 'Queensland and northern Australia hub',
    icon: 'lucide:building'
  }, {
    label: 'Perth',
    to: '/offices/perth',
    description: 'Western Australia operations (coming soon)',
    icon: 'lucide:clock'
  }]
}, {
  label: 'Service Center',
  icon: 'lucide:settings',
  children: [{
    label: 'News & Updates',
    to: '/service-center/news',
    description: 'Latest company news and announcements',
    icon: 'lucide:newspaper'
  }, {
    label: 'Important Notices',
    to: '/service-center/notices',
    description: 'Service alerts and regulatory updates',
    icon: 'lucide:alert-circle'
  }, {
    label: 'Downloads',
    to: '/service-center/downloads',
    description: 'Forms, guides, and documentation',
    icon: 'lucide:download'
  }, {
    label: 'Service Center Home',
    to: '/service-center',
    description: 'Access all service center resources',
    icon: 'lucide:home'
  }]
}, {
  label: 'Careers',
  to: '/careers',
  icon: 'lucide:briefcase'
}, {
  label: 'About Us',
  to: '/about',
  icon: 'lucide:info'
}, {
  label: 'Contact',
  to: '/contact',
  icon: 'lucide:mail'
}])

// Remove the scroll spy functionality since we now have proper routing
// nuxtApp.hooks.hookOnce('page:finish', () => {
//   updateHeadings([
//     document.querySelector('#services'),
//     document.querySelector('#offices'),
//     document.querySelector('#contact')
//   ].filter(Boolean) as Element[])
// })
</script>

<template>
  <UHeader 
    :ui="{
      container: 'max-w-none mx-auto px-4 sm:px-6 lg:px-8 xl:px-12'
    }"
    class="h-20"
  >
    <template #left>
      <NuxtLink to="/" class="flex items-center gap-3">
        <AppLogo class="w-auto h-10 shrink-0" />
      </NuxtLink>
    </template>

    <template #right>
      <div class="flex items-center space-x-4 lg:space-x-6 xl:space-x-8">
        <!-- Navigation Menu -->
        <nav class="hidden lg:block flex-1">
          <div class="flex items-center space-x-3 lg:space-x-4 xl:space-x-6">
            <template v-for="item in items" :key="item.label">
              <!-- Simple link without dropdown -->
              <NuxtLink 
                v-if="!item.children"
                :to="item.to"
                class="flex items-center gap-2 text-gray-700 dark:text-gray-300 hover:text-primary transition-colors duration-200 font-medium whitespace-nowrap px-2 py-1"
              >
                <UIcon :name="item.icon" class="w-4 h-4 flex-shrink-0" />
                <span>{{ item.label }}</span>
              </NuxtLink>
              
              <!-- Dropdown menu -->
              <UDropdownMenu 
                v-else
                :items="item.children"
                :ui="{
                  content: 'min-w-80 p-4 bg-white/95 dark:bg-gray-900/95 backdrop-blur-lg border border-gray-200/50 dark:border-gray-700/50 shadow-xl rounded-xl',
                  item: 'group relative p-3 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800/50 transition-all duration-200 w-full',
                  itemLeadingIcon: 'text-primary w-5 h-5',
                  itemLabel: 'font-semibold text-gray-900 dark:text-gray-100'
                }"
              >
                <div class="flex items-center gap-2 text-gray-700 dark:text-gray-300 hover:text-primary transition-colors duration-200 font-medium whitespace-nowrap px-3 py-2 cursor-pointer">
                  <UIcon :name="item.icon" class="w-4 h-4 flex-shrink-0" />
                  <span class="flex-shrink-0">{{ item.label }}</span>
                  <UIcon name="lucide:chevron-down" class="w-4 h-4 flex-shrink-0" />
                </div>
              </UDropdownMenu>
            </template>
          </div>
        </nav>
        
        <!-- Action Buttons -->
        <div class="flex items-center space-x-3">
          <UColorModeButton />
          
          <UButton
            label="Get Quote"
            variant="subtle"
            class="hidden lg:block"
            to="/contact"
          />
        </div>
      </div>
    </template>

    <template #body>
      <div class="space-y-2 -mx-2.5">
        <template v-for="item in items" :key="item.label">
          <!-- Simple link without dropdown -->
          <NuxtLink 
            v-if="!item.children"
            :to="item.to"
            class="flex items-center gap-3 p-2.5 rounded-lg text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors duration-200"
          >
            <UIcon :name="item.icon" class="w-5 h-5 text-primary" />
            <span class="font-medium">{{ item.label }}</span>
          </NuxtLink>
          
          <!-- Dropdown items (expanded for mobile) -->
          <div v-else class="space-y-1">
            <div class="flex items-center gap-3 p-2.5 font-semibold text-gray-900 dark:text-gray-100">
              <UIcon :name="item.icon" class="w-5 h-5 text-primary" />
              {{ item.label }}
            </div>
            <div class="ml-8 space-y-1">
              <NuxtLink
                v-for="child in item.children"
                :key="child.label"
                :to="child.to"
                class="flex items-start gap-3 p-2 rounded-lg text-sm text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors duration-200"
              >
                <UIcon :name="child.icon" class="w-4 h-4 text-primary mt-0.5 flex-shrink-0" />
                <div>
                  <div class="font-medium text-gray-900 dark:text-gray-100">{{ child.label }}</div>
                  <div class="text-xs text-gray-500 dark:text-gray-500 mt-0.5">{{ child.description }}</div>
                </div>
              </NuxtLink>
            </div>
          </div>
        </template>
      </div>
      <UButton
        class="mt-4"
        label="Get Quote"
        variant="subtle"
        block
        to="/contact"
      />
    </template>
  </UHeader>
</template>