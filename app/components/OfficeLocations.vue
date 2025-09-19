<script setup lang="ts">
interface Office {
  city: string
  status: 'active' | 'coming_soon'
  isHeadquarters?: boolean
  address: string
  phone: string
  email: string
  description: string
  services: string[]
}

interface Props {
  offices: Office[]
  variant?: 'default' | 'tech'
  title?: string
  description?: string
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'default',
  title: 'Our Office Locations',
  description: 'Visit us at any of our strategically located offices across Australia.'
})
</script>

<template>
  <UPageSection
    :id="variant === 'tech' ? 'offices' : 'office-locations'"
    :class="[
      'mb-32 overflow-hidden',
      variant === 'tech' 
        ? 'relative' 
        : 'bg-gray-50 dark:bg-gray-900'
    ]"
    :ui="variant === 'tech' 
      ? { title: 'text-center @container relative mb-8', description: 'text-center mb-12' }
      : {}"
  >
    <!-- Tech variant background -->
    <template v-if="variant === 'tech'">
      <div class="absolute inset-0 bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 dark:from-gray-950 dark:via-blue-950 dark:to-gray-950"></div>
      <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PGNpcmNsZSBjeD0iMzAiIGN5PSIzMCIgcj0iMSIvPjwvZz48L2c+PC9zdmc+')] opacity-40"></div>
    </template>

    <UContainer :class="variant === 'tech' ? 'relative z-10' : ''">
      <!-- Tech variant title -->
      <div v-if="variant === 'tech'" class="text-center mb-16">
        <div class="inline-flex items-center gap-3 mb-6">
          <div class="w-12 h-0.5 bg-gradient-to-r from-transparent to-primary"></div>
          <UIcon name="lucide:map-pin" class="text-primary text-2xl animate-pulse" />
          <div class="w-12 h-0.5 bg-gradient-to-l from-transparent to-primary"></div>
        </div>
        
        <h2 class="text-4xl md:text-5xl lg:text-6xl font-black text-white mb-6 leading-tight tracking-tight">
          Our <span class="bg-gradient-to-r from-blue-400 via-primary to-cyan-400 bg-clip-text text-transparent">Australian</span> Network
        </h2>
        
        <p class="text-xl md:text-2xl text-gray-300 max-w-4xl mx-auto leading-relaxed font-medium">
          {{ description.replace('Visit us at any of our strategically located offices', 'Strategically located') }}
          <span class="text-primary font-semibold">local expertise</span> and 
          <span class="text-primary font-semibold">global reach</span>.
        </p>
        
        <!-- Tech-style decorative elements -->
        <div class="flex justify-center items-center gap-2 mt-8">
          <div class="w-2 h-2 bg-primary rounded-full animate-ping"></div>
          <div class="w-16 h-0.5 bg-gradient-to-r from-primary to-transparent"></div>
          <div class="w-3 h-3 border-2 border-primary rounded-full"></div>
          <div class="w-16 h-0.5 bg-gradient-to-l from-primary to-transparent"></div>
          <div class="w-2 h-2 bg-primary rounded-full animate-ping animation-delay-1000"></div>
        </div>
      </div>

      <!-- Default variant title -->
      <div v-else class="text-center mb-12">
        <h2 class="text-3xl md:text-4xl font-bold mb-4">{{ title }}</h2>
        <p class="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">{{ description }}</p>
      </div>

      <!-- Office Grid -->
      <div class="grid md:grid-cols-2 gap-8">
        <div
          v-for="(office, index) in offices"
          :key="office.city"
          class="group relative"
        >
          <UCard 
            :class="[
              'h-full transition-all duration-500',
              variant === 'tech' 
                ? [
                    'backdrop-blur-sm border-0 shadow-2xl',
                    office.status === 'active' 
                      ? 'bg-white/10 hover:bg-white/20 hover:shadow-primary/20 hover:-translate-y-2 border-l-4 border-l-primary hover:border-l-cyan-400' 
                      : 'bg-white/5 opacity-75 border-l-4 border-l-gray-500'
                  ]
                : [
                    office.status === 'active' 
                      ? 'hover:shadow-xl hover:-translate-y-1 border-l-4 border-l-primary' 
                      : 'opacity-75 border-l-4 border-l-gray-300 dark:border-l-gray-600'
                  ]
            ]"
          >
            <template #header>
              <div class="flex items-start justify-between">
                <div class="flex items-center gap-3">
                  <div class="relative">
                    <div 
                      :class="[
                        'w-12 h-12 rounded-full flex items-center justify-center',
                        office.status === 'active' 
                          ? (variant === 'tech' ? 'bg-primary/20 text-primary' : 'bg-primary/10 text-primary')
                          : (variant === 'tech' ? 'bg-gray-500/20 text-gray-400' : 'bg-gray-200 dark:bg-gray-700 text-gray-500')
                      ]"
                    >
                      <UIcon 
                        :name="office.status === 'active' ? 'lucide:building-2' : 'lucide:clock'" 
                        class="w-6 h-6" 
                      />
                    </div>
                    <div 
                      v-if="office.isHeadquarters && office.status === 'active'"
                      class="absolute -top-1 -right-1 w-4 h-4 bg-primary rounded-full flex items-center justify-center"
                    >
                      <UIcon name="lucide:star" class="w-2.5 h-2.5 text-white" />
                    </div>
                  </div>
                  <div>
                    <h3 :class="[
                      'text-xl font-bold',
                      variant === 'tech' ? 'text-white' : 'text-gray-900 dark:text-white'
                    ]">
                      {{ office.city }}
                    </h3>
                    <div class="flex items-center gap-2 text-sm">
                      <span 
                        v-if="office.isHeadquarters && office.status === 'active'"
                        class="bg-primary/20 text-primary px-2 py-1 rounded-full text-xs font-medium"
                      >
                        HEAD OFFICE
                      </span>
                      <span 
                        :class="[
                          'px-2 py-1 rounded-full text-xs font-medium',
                          office.status === 'active' 
                            ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' 
                            : 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200'
                        ]"
                      >
                        {{ office.status === 'active' ? 'OPERATIONAL' : 'READY SOON' }}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </template>
            
            <div class="space-y-6">
              <!-- Address & Contact -->
              <div class="space-y-4">
                <div class="flex items-start gap-3">
                  <UIcon name="lucide:map-pin" class="text-primary mt-1 flex-shrink-0" />
                  <div>
                    <h4 :class="[
                      'font-semibold text-sm uppercase tracking-wide',
                      variant === 'tech' ? 'text-gray-300' : 'text-gray-600 dark:text-gray-400'
                    ]">
                      Address
                    </h4>
                    <p :class="[
                      'font-medium',
                      variant === 'tech' ? 'text-gray-100' : 'text-gray-900 dark:text-gray-100'
                    ]">
                      {{ office.address }}
                    </p>
                  </div>
                </div>
                
                <div v-if="office.status === 'active'" class="grid sm:grid-cols-2 gap-4">
                  <div class="flex items-start gap-3">
                    <UIcon name="lucide:phone" class="text-primary mt-1 flex-shrink-0" />
                    <div>
                      <h4 :class="[
                        'font-semibold text-sm uppercase tracking-wide',
                        variant === 'tech' ? 'text-gray-300' : 'text-gray-600 dark:text-gray-400'
                      ]">
                        Phone
                      </h4>
                      <a :href="`tel:${office.phone}`" class="text-primary hover:underline font-medium">{{ office.phone }}</a>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-3">
                    <UIcon name="lucide:mail" class="text-primary mt-1 flex-shrink-0" />
                    <div>
                      <h4 :class="[
                        'font-semibold text-sm uppercase tracking-wide',
                        variant === 'tech' ? 'text-gray-300' : 'text-gray-600 dark:text-gray-400'
                      ]">
                        Email
                      </h4>
                      <a :href="`mailto:${office.email}`" class="text-primary hover:underline font-medium">{{ office.email }}</a>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Description -->
              <div>
                <p :class="[
                  variant === 'tech' ? 'text-gray-300' : 'text-gray-600 dark:text-gray-400'
                ]">
                  {{ office.description }}
                </p>
              </div>

              <!-- Services -->
              <div>
                <h4 :class="[
                  'font-semibold text-sm uppercase tracking-wide mb-3',
                  variant === 'tech' ? 'text-gray-300' : 'text-gray-600 dark:text-gray-400'
                ]">
                  Services
                </h4>
                <div class="grid grid-cols-1 gap-2">
                  <div
                    v-for="service in office.services"
                    :key="service"
                    class="flex items-center gap-2 text-sm"
                  >
                    <UIcon 
                      :name="office.status === 'active' ? 'lucide:check-circle' : 'lucide:clock'" 
                      :class="office.status === 'active' ? 'text-green-500' : 'text-yellow-500'" 
                      class="w-4 h-4 flex-shrink-0" 
                    />
                    <span :class="[
                      variant === 'tech' ? 'text-gray-200' : 'text-gray-700 dark:text-gray-300'
                    ]">
                      {{ service }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Action Button -->
              <div :class="[
                'pt-4',
                variant === 'tech' ? 'border-t border-gray-600' : 'border-t border-gray-200 dark:border-gray-700'
              ]">
                <UButton 
                  v-if="office.status === 'active'"
                  :to="`tel:${office.phone}`"
                  variant="outline"
                  size="sm"
                  block
                  class="group"
                >
                  <UIcon name="lucide:phone" class="mr-2 group-hover:animate-pulse" />
                  Contact {{ office.city }}
                </UButton>
                <UButton 
                  v-else
                  disabled
                  variant="outline"
                  size="sm"
                  block
                  class="opacity-60"
                >
                  <UIcon name="lucide:clock" class="mr-2" />
                  Coming Soon
                </UButton>
              </div>
            </div>
          </UCard>
        </div>
      </div>
    </UContainer>
  </UPageSection>
</template>
