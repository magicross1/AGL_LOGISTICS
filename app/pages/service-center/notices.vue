<script setup lang="ts">
useSeoMeta({
  title: 'Important Notices - AGL LOGISTICS',
  description: 'Stay updated with important notices, service alerts, regulatory changes, and operational updates from AGL LOGISTICS.',
})

// Mock notices data
const notices = [
  {
    id: 1,
    title: 'Port of Melbourne Congestion Notice',
    content: 'Due to ongoing industrial action at the Port of Melbourne, we are experiencing significant delays in cargo processing. Extended delays of 5-7 days are expected for all Melbourne port operations. We recommend considering alternative routing via Adelaide or Sydney ports for urgent shipments. Our team is monitoring the situation closely and will provide updates as they become available.',
    type: 'alert',
    priority: 'high',
    date: '2024-12-18',
    validUntil: '2024-12-25',
    affectedServices: ['Sea Freight', 'Customs Brokerage'],
    status: 'active'
  },
  {
    id: 2,
    title: 'Christmas & New Year Operating Hours',
    content: 'Please note our modified operating hours during the holiday period: December 22-24: 8:00 AM - 2:00 PM, December 25-26: Closed, December 27-31: 9:00 AM - 4:00 PM, January 1-2: Closed. Emergency services remain available 24/7 by calling our emergency hotline. Normal operations resume January 3, 2025.',
    type: 'info',
    priority: 'medium',
    date: '2024-12-01',
    validUntil: '2025-01-03',
    affectedServices: ['All Services'],
    status: 'active'
  },
  {
    id: 3,
    title: 'Enhanced Security Measures at Sydney Facility',
    content: 'Effective immediately, enhanced security protocols are in place at our Sydney warehouse facility. All visitors must provide 24-hour advance notice and valid photo identification. Additional screening procedures may apply for high-value and dangerous goods. These measures ensure the continued security and safety of your cargo.',
    type: 'info',
    priority: 'medium',
    date: '2024-12-15',
    validUntil: null,
    affectedServices: ['Storage', 'Special Transports'],
    status: 'active'
  },
  {
    id: 4,
    title: 'New Dangerous Goods Regulations - IATA 66th Edition',
    content: 'The International Air Transport Association (IATA) Dangerous Goods Regulations 66th Edition comes into effect January 1, 2025. Key changes include updated lithium battery requirements, new UN specifications, and modified packaging instructions. Our dangerous goods team has completed training on the new regulations. Please contact us to review your dangerous goods shipments.',
    type: 'regulatory',
    priority: 'high',
    date: '2024-11-30',
    validUntil: null,
    affectedServices: ['Air Freight', 'Special Transports'],
    status: 'active'
  },
  {
    id: 5,
    title: 'System Maintenance - December 20, 2024',
    content: 'Scheduled system maintenance will occur on December 20, 2024, from 2:00 AM to 6:00 AM AEDT. During this time, our online tracking system and customer portal may be unavailable. For urgent tracking requests, please contact our customer service team. We apologize for any inconvenience.',
    type: 'maintenance',
    priority: 'low',
    date: '2024-12-18',
    validUntil: '2024-12-20',
    affectedServices: ['All Services'],
    status: 'scheduled'
  }
]

const noticeTypes = [
  { value: 'all', label: 'All Notices', icon: 'lucide:list' },
  { value: 'alert', label: 'Service Alerts', icon: 'lucide:alert-triangle' },
  { value: 'info', label: 'Information', icon: 'lucide:info' },
  { value: 'regulatory', label: 'Regulatory', icon: 'lucide:book-open' },
  { value: 'maintenance', label: 'Maintenance', icon: 'lucide:settings' }
]

const selectedType = ref('all')

const filteredNotices = computed(() => {
  if (selectedType.value === 'all') {
    return notices
  }
  return notices.filter(notice => notice.type === selectedType.value)
})

const getPriorityColor = (priority) => {
  switch (priority) {
    case 'high': return 'red'
    case 'medium': return 'yellow'
    case 'low': return 'green'
    default: return 'gray'
  }
}

const getTypeIcon = (type) => {
  switch (type) {
    case 'alert': return 'lucide:alert-triangle'
    case 'info': return 'lucide:info'
    case 'regulatory': return 'lucide:book-open'
    case 'maintenance': return 'lucide:settings'
    default: return 'lucide:bell'
  }
}
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Important Notices"
      description="Stay updated with service alerts, regulatory changes, operational updates, and other important announcements."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Notices Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <img
            src="/images/notices.png"
            alt="Important notices"
            class="absolute inset-0 w-full h-full object-cover scale-105 transition-transform duration-[20s] hover:scale-110"
          />
          <!-- Gradient overlay for better text readability -->
          <div class="absolute inset-0 bg-gradient-to-b from-red-900/40 via-black/50 to-black/70"></div>
          <!-- Animated particles overlay -->
          <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC41Ij48Y2lyY2xlIGN4PSIzMCIgY3k9IjMwIiByPSIxIi8+PC9nPjwvZz48L3N2Zz4=')] opacity-20 animate-pulse"></div>
        </div>
      </template>

      <template #title>
        <div class="flex items-center justify-center gap-4 mb-4">
          <UIcon name="lucide:alert-circle" class="text-red-400 text-3xl animate-pulse" />
          <h1 class="text-white drop-shadow-lg">Important Notices</h1>
        </div>
      </template>

      <template #links>
        <UButton
          label="Subscribe to Alerts"
          icon="lucide:bell"
          trailing
          color="red"
          to="/service-center#subscribe"
          size="xl"
          class="bg-red-600 hover:bg-red-700 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="View All Notices"
          icon="lucide:alert-circle"
          size="xl"
          color="white"
          variant="outline"
          to="#notices"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Active Alerts -->
    <UPageSection
      title="Active Alerts"
      description="Critical notices requiring immediate attention."
    >
      <div class="space-y-6">
        <div
          v-for="notice in notices.filter(n => n.priority === 'high' && n.status === 'active')"
          :key="notice.id"
          class="border border-red-200 dark:border-red-800 bg-red-50 dark:bg-red-900/20 rounded-lg p-6"
        >
          <div class="flex items-start gap-4">
            <div class="flex-shrink-0">
              <UIcon :name="getTypeIcon(notice.type)" class="text-2xl text-red-600 dark:text-red-400" />
            </div>
            <div class="flex-1">
              <div class="flex items-start justify-between mb-3">
                <h3 class="text-lg font-semibold text-red-900 dark:text-red-100">{{ notice.title }}</h3>
                <div class="flex items-center gap-2 text-sm text-red-600 dark:text-red-400">
                  <UIcon name="lucide:calendar" />
                  <time>{{ new Date(notice.date).toLocaleDateString() }}</time>
                </div>
              </div>
              <p class="text-red-800 dark:text-red-200 mb-4">{{ notice.content }}</p>
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-4 text-sm">
                  <div class="flex items-center gap-1">
                    <UIcon name="lucide:truck" class="text-red-600 dark:text-red-400" />
                    <span class="text-red-700 dark:text-red-300">Affects: {{ notice.affectedServices.join(', ') }}</span>
                  </div>
                  <div v-if="notice.validUntil" class="flex items-center gap-1">
                    <UIcon name="lucide:clock" class="text-red-600 dark:text-red-400" />
                    <span class="text-red-700 dark:text-red-300">Until: {{ new Date(notice.validUntil).toLocaleDateString() }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- All Notices -->
    <UPageSection
      title="All Notices"
      description="Browse all notices by type and priority."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <!-- Filter Tabs -->
      <div class="mb-8">
        <div class="flex flex-wrap gap-2">
          <UButton
            v-for="type in noticeTypes"
            :key="type.value"
            :variant="selectedType === type.value ? 'solid' : 'outline'"
            size="sm"
            @click="selectedType = type.value"
          >
            <UIcon :name="type.icon" class="mr-2" />
            {{ type.label }}
          </UButton>
        </div>
      </div>

      <!-- Notices List -->
      <div class="space-y-6">
        <div
          v-for="notice in filteredNotices"
          :key="notice.id"
          :class="[
            'border rounded-lg p-6',
            notice.priority === 'high' && notice.status === 'active' 
              ? 'border-red-200 dark:border-red-800 bg-red-50 dark:bg-red-900/20'
              : notice.priority === 'medium'
              ? 'border-yellow-200 dark:border-yellow-800 bg-yellow-50 dark:bg-yellow-900/20'
              : 'border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800'
          ]"
        >
          <div class="flex items-start gap-4">
            <div class="flex-shrink-0">
              <UIcon 
                :name="getTypeIcon(notice.type)" 
                :class="[
                  'text-2xl',
                  notice.priority === 'high' && notice.status === 'active'
                    ? 'text-red-600 dark:text-red-400'
                    : notice.priority === 'medium'
                    ? 'text-yellow-600 dark:text-yellow-400'
                    : 'text-gray-600 dark:text-gray-400'
                ]"
              />
            </div>
            <div class="flex-1">
              <div class="flex items-start justify-between mb-3">
                <div class="flex items-center gap-3">
                  <h3 class="text-lg font-semibold">{{ notice.title }}</h3>
                  <span 
                    :class="[
                      'px-2 py-1 rounded text-xs font-medium',
                      notice.priority === 'high'
                        ? 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200'
                        : notice.priority === 'medium'
                        ? 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200'
                        : 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
                    ]"
                  >
                    {{ notice.priority.toUpperCase() }}
                  </span>
                </div>
                <div class="flex items-center gap-2 text-sm text-muted-foreground">
                  <UIcon name="lucide:calendar" />
                  <time>{{ new Date(notice.date).toLocaleDateString() }}</time>
                </div>
              </div>
              <p class="text-muted-foreground mb-4">{{ notice.content }}</p>
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-4 text-sm text-muted-foreground">
                  <div class="flex items-center gap-1">
                    <UIcon name="lucide:truck" />
                    <span>Affects: {{ notice.affectedServices.join(', ') }}</span>
                  </div>
                  <div v-if="notice.validUntil" class="flex items-center gap-1">
                    <UIcon name="lucide:clock" />
                    <span>Until: {{ new Date(notice.validUntil).toLocaleDateString() }}</span>
                  </div>
                  <div class="flex items-center gap-1">
                    <UIcon name="lucide:activity" />
                    <span class="capitalize">{{ notice.status }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- Alert Subscription CTA -->
    <UPageCTA
      title="Stay informed with instant alerts"
      description="Subscribe to our alert system to receive immediate notifications about service disruptions, regulatory changes, and important updates."
      :links="[
        {
          label: 'Subscribe to Alerts',
          to: '/service-center#subscribe',
          color: 'primary'
        },
        {
          label: 'Contact Support',
          to: '/contact',
          variant: 'outline'
        }
      ]"
    />
  </div>
</template>
