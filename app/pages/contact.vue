<script setup lang="ts">
useSeoMeta({
  title: 'Contact AGL LOGISTICS - Get Expert Logistics Support',
  description: 'Contact AGL LOGISTICS for professional freight forwarding services. Multiple contact options, 24/7 emergency support, and offices across Australia.',
})

const toast = useToast()

// Office data matching the OfficeLocations component interface
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

// Enhanced contact methods with more options
const contactMethods = [
  {
    title: '24/7 Emergency Hotline',
    description: 'Immediate assistance for urgent shipments and critical issues',
    icon: 'lucide:phone',
    value: '+61 2 8747 3069',
    action: 'tel:+61-2-8747-3069',
    color: 'red',
    available: '24/7 Emergency',
    badge: 'EMERGENCY',
    features: ['Immediate response', 'Crisis management', 'Priority handling']
  },
  {
    title: 'General Business Line',
    description: 'For quotes, inquiries, and general business discussions',
    icon: 'lucide:phone-call',
    value: '+61 2 8747 3069',
    action: 'tel:+61-2-8747-3069',
    color: 'primary',
    available: 'Mon-Fri 8AM-6PM',
    badge: 'BUSINESS',
    features: ['Quote requests', 'Service inquiries', 'Account management']
  },
  {
    title: 'Operations Email',
    description: 'Direct line to our operations team for service coordination',
    icon: 'lucide:mail',
    value: 'ops@agllogistics.com.au',
    action: 'mailto:ops@agllogistics.com.au',
    color: 'blue',
    available: 'Response within 4 hours',
    badge: 'EMAIL',
    features: ['Detailed inquiries', 'Documentation', 'Service requests']
  },
  {
    title: 'WhatsApp Business',
    description: 'Quick updates, tracking information, and instant messaging',
    icon: 'lucide:message-square',
    value: '+61 2 8747 3069',
    action: 'https://wa.me/61287473069',
    color: 'green',
    available: 'Mon-Fri 8AM-6PM',
    badge: 'INSTANT',
    features: ['Quick updates', 'Photo sharing', 'Real-time chat']
  }
]

// Department contacts
const departments = [
  {
    name: 'Operations',
    description: 'Freight forwarding, booking, and logistics coordination',
    email: 'ops@agllogistics.com.au',
    phone: '+61 2 8747 3069',
    icon: 'lucide:truck',
    specialties: ['Air Freight', 'Sea Freight', 'Project Cargo']
  },
  {
    name: 'Customs & Compliance',
    description: 'Import/export clearance and regulatory compliance',
    email: 'customs@agllogistics.com.au',
    phone: '+61 2 8747 3070',
    icon: 'lucide:clipboard-check',
    specialties: ['Customs Clearance', 'Documentation', 'Compliance']
  },
  {
    name: 'Warehousing',
    description: 'Storage solutions and distribution services',
    email: 'warehouse@agllogistics.com.au',
    phone: '+61 2 8747 3071',
    icon: 'lucide:warehouse',
    specialties: ['Storage', 'Distribution', 'Inventory Management']
  },
  {
    name: 'Customer Service',
    description: 'General support and account management',
    email: 'support@agllogistics.com.au',
    phone: '+61 2 8747 3072',
    icon: 'lucide:headphones',
    specialties: ['Account Support', 'Tracking', 'General Inquiries']
  }
]

// Service hours
const serviceHours = [
  {
    service: 'Emergency Support',
    hours: '24/7',
    description: 'Critical shipment issues and urgent assistance',
    color: 'red',
    icon: 'lucide:alert-circle'
  },
  {
    service: 'Phone Support',
    hours: 'Mon-Fri 8AM-6PM, Sat 9AM-2PM',
    description: 'General inquiries and business discussions',
    color: 'primary',
    icon: 'lucide:phone'
  },
  {
    service: 'Email Support',
    hours: 'Monitored 24/7',
    description: 'Detailed inquiries and documentation requests',
    color: 'blue',
    icon: 'lucide:mail'
  },
  {
    service: 'WhatsApp Business',
    hours: 'Mon-Fri 8AM-6PM',
    description: 'Quick updates and instant messaging',
    color: 'green',
    icon: 'lucide:message-square'
  }
]

function copyToClipboard(text: string, type: string) {
  navigator.clipboard.writeText(text)
  toast.add({
    title: 'Copied!',
    description: `${type} copied to clipboard`,
    color: 'green'
  })
}
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Contact AGL LOGISTICS"
      description="Connect with Australia's leading logistics experts. Multiple contact options, 24/7 emergency support, and personalized service across all major cities."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Contact Video Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <video
            autoplay
            muted
            loop
            playsinline
            class="absolute inset-0 w-full h-full object-cover"
          >
            <source src="/videos/contact.mp4" type="video/mp4">
          </video>
          <!-- Dark overlay for better text readability -->
          <div class="absolute inset-0 bg-black/40"></div>
          <!-- Tech grid overlay -->
          <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZGVmcz48cGF0dGVybiBpZD0iZ3JpZCIgd2lkdGg9IjEwMCIgaGVpZ2h0PSIxMDAiIHBhdHRlcm5Vbml0cz0idXNlclNwYWNlT25Vc2UiPjxwYXRoIGQ9Im0gMTAwIDAgTCAwIDAgMCAxMDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzMzMzMzMyIgc3Ryb2tlLXdpZHRoPSIxIiBvcGFjaXR5PSIwLjIiLz48L3BhdHRlcm4+PC9kZWZzPjxyZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9InVybCgjZ3JpZCkiLz48L3N2Zz4=')] opacity-20"></div>
        </div>
      </template>

      <template #title>
        <div class="text-center">
          <div class="flex items-center justify-center gap-4 mb-6">
            <div class="w-16 h-0.5 bg-gradient-to-r from-transparent to-primary"></div>
            <UIcon name="lucide:headphones" class="text-primary text-4xl animate-pulse" />
            <div class="w-16 h-0.5 bg-gradient-to-l from-transparent to-primary"></div>
          </div>
          <h1 class="text-white drop-shadow-lg">Contact AGL LOGISTICS</h1>
          <div class="flex justify-center items-center gap-2 mt-6">
            <div class="w-2 h-2 bg-primary rounded-full animate-ping"></div>
            <div class="w-16 h-0.5 bg-gradient-to-r from-primary to-transparent"></div>
            <div class="w-3 h-3 border-2 border-primary rounded-full"></div>
            <div class="w-16 h-0.5 bg-gradient-to-l from-primary to-transparent"></div>
            <div class="w-2 h-2 bg-primary rounded-full animate-ping animation-delay-1000"></div>
          </div>
        </div>
      </template>

      <template #links>
        <UButton
          label="Emergency Support"
          icon="lucide:phone"
          trailing
          color="red"
          to="tel:+61-2-8747-3069"
          size="xl"
          class="bg-red-600 hover:bg-red-700 text-white font-semibold px-8 py-4 shadow-lg animate-pulse"
        />
        <UButton
          label="WhatsApp Chat"
          icon="lucide:message-square"
          size="xl"
          color="white"
          variant="outline"
          to="https://wa.me/61287473069"
          target="_blank"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Primary Contact Methods -->
    <UPageSection class="bg-white dark:bg-gray-900 relative overflow-hidden">
      <!-- Background Effects -->
      <div class="absolute inset-0">
        <div class="absolute top-20 left-10 w-72 h-72 bg-primary/5 rounded-full blur-3xl animate-pulse"></div>
        <div class="absolute bottom-20 right-10 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl animate-pulse animation-delay-2000"></div>
        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-gradient-conic from-primary/5 via-transparent to-blue-500/5 rounded-full blur-3xl animate-spin-slow"></div>
      </div>

      <UContainer class="relative z-10">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl lg:text-6xl font-black text-gray-900 dark:text-white mb-6 leading-tight tracking-tight">
            Get In Touch <span class="bg-gradient-to-r from-primary via-blue-600 to-purple-600 bg-clip-text text-transparent animate-pulse">Instantly</span>
          </h2>
          <p class="text-xl md:text-2xl text-gray-600 dark:text-gray-300 max-w-4xl mx-auto leading-relaxed font-medium">
            Choose your preferred method to connect with our <span class="text-primary font-semibold">logistics experts</span>
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div
            v-for="(method, index) in contactMethods"
            :key="method.title"
            class="group relative"
          >
            <UCard 
              :class="[
                'h-full transition-all duration-500 hover:shadow-2xl hover:-translate-y-4 cursor-pointer backdrop-blur-sm border-0',
                method.color === 'red' ? 'bg-gradient-to-br from-red-50 to-red-100 dark:from-red-900/20 dark:to-red-800/20 hover:shadow-red-500/20' :
                method.color === 'green' ? 'bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900/20 dark:to-green-800/20 hover:shadow-green-500/20' :
                method.color === 'blue' ? 'bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900/20 dark:to-blue-800/20 hover:shadow-blue-500/20' :
                'bg-gradient-to-br from-primary/5 to-blue-500/10 hover:shadow-primary/20'
              ]"
              @click="window.open(method.action, method.action.startsWith('http') ? '_blank' : '_self')"
            >
              <!-- Badge -->
              <div class="absolute -top-3 -right-3">
                <span :class="[
                  'px-3 py-1 rounded-full text-xs font-bold',
                  method.color === 'red' ? 'bg-red-600 text-white animate-pulse' :
                  method.color === 'green' ? 'bg-green-600 text-white' :
                  method.color === 'blue' ? 'bg-blue-600 text-white' :
                  'bg-primary text-white'
                ]">
                  {{ method.badge }}
                </span>
              </div>

              <div class="text-center space-y-4">
                <!-- Icon -->
                <div class="flex justify-center">
                  <div :class="[
                    'w-20 h-20 rounded-full flex items-center justify-center transition-all duration-300 group-hover:scale-110',
                    method.color === 'red' ? 'bg-red-100 text-red-600 group-hover:bg-red-600 group-hover:text-white' :
                    method.color === 'green' ? 'bg-green-100 text-green-600 group-hover:bg-green-600 group-hover:text-white' :
                    method.color === 'blue' ? 'bg-blue-100 text-blue-600 group-hover:bg-blue-600 group-hover:text-white' :
                    'bg-primary/10 text-primary group-hover:bg-primary group-hover:text-white'
                  ]">
                    <UIcon :name="method.icon" class="w-10 h-10" />
                  </div>
                </div>
                
                <!-- Content -->
                <div>
                  <h3 class="font-black text-xl md:text-2xl mb-3 tracking-tight">{{ method.title }}</h3>
                  <p class="text-sm md:text-base text-gray-600 dark:text-gray-400 mb-4 leading-relaxed font-medium">{{ method.description }}</p>
                  
                  <!-- Contact Value -->
                  <div class="bg-white/70 dark:bg-gray-800/70 rounded-xl p-3 mb-4 backdrop-blur-sm border border-gray-200/50 dark:border-gray-700/50">
                    <p class="font-mono text-sm font-bold text-gray-900 dark:text-gray-100 break-all">{{ method.value }}</p>
                    <p class="text-xs text-gray-500 mt-1 font-medium">{{ method.available }}</p>
                  </div>

                  <!-- Features -->
                  <div class="space-y-2 mb-4">
                    <div
                      v-for="feature in method.features"
                      :key="feature"
                      class="flex items-center gap-2 text-xs md:text-sm"
                    >
                      <UIcon name="lucide:check" :class="[
                        'w-4 h-4',
                        method.color === 'red' ? 'text-red-600' :
                        method.color === 'green' ? 'text-green-600' :
                        method.color === 'blue' ? 'text-blue-600' :
                        'text-primary'
                      ]" />
                      <span class="text-gray-700 dark:text-gray-300 font-medium">{{ feature }}</span>
                    </div>
                  </div>
                </div>

                <!-- Action Buttons -->
                <div class="space-y-2">
                  <UButton
                    :to="method.action"
                    :color="method.color"
                    size="sm"
                    block
                    class="group-hover:scale-105 transition-transform duration-300"
                  >
                    <UIcon :name="method.icon" class="mr-2" />
                    Contact Now
                  </UButton>
                  <UButton
                    variant="ghost"
                    size="xs"
                    block
                    @click.stop="copyToClipboard(method.value, method.badge)"
                  >
                    <UIcon name="lucide:copy" class="mr-1" />
                    Copy
                  </UButton>
                </div>
              </div>
            </UCard>
          </div>
        </div>
      </UContainer>
    </UPageSection>

    <!-- Department Contacts -->
    <UPageSection class="bg-gray-50 dark:bg-gray-900">
      <UContainer>
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-black text-gray-900 dark:text-white mb-6 leading-tight tracking-tight">
            Direct <span class="bg-gradient-to-r from-primary to-cyan-500 bg-clip-text text-transparent">Department</span> Access
          </h2>
          <p class="text-xl md:text-2xl text-gray-600 dark:text-gray-300 max-w-4xl mx-auto leading-relaxed font-medium">
            Connect directly with the <span class="text-primary font-semibold">right team</span> for specialized assistance
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-8">
          <UCard
            v-for="dept in departments"
            :key="dept.name"
            class="group hover:shadow-xl transition-all duration-300 hover:-translate-y-2"
          >
            <template #header>
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center group-hover:bg-primary group-hover:text-white transition-all duration-300">
                  <UIcon :name="dept.icon" class="w-6 h-6 text-primary group-hover:text-white" />
                </div>
                <div>
                  <h3 class="text-xl md:text-2xl font-black tracking-tight">{{ dept.name }}</h3>
                  <p class="text-sm md:text-base text-gray-600 dark:text-gray-400 font-medium leading-relaxed">{{ dept.description }}</p>
                </div>
              </div>
            </template>

            <div class="space-y-4">
              <!-- Contact Details -->
              <div class="grid grid-cols-1 gap-3">
                  <div class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-800 rounded-xl border border-gray-200/50 dark:border-gray-700/50">
                    <UIcon name="lucide:phone" class="text-primary text-lg flex-shrink-0" />
                    <div class="flex-1 min-w-0">
                      <p class="font-mono text-sm font-bold truncate">{{ dept.phone }}</p>
                    </div>
                    <UButton
                      :to="`tel:${dept.phone}`"
                      size="xs"
                      variant="outline"
                      class="font-semibold flex-shrink-0"
                    >
                      Call
                    </UButton>
                  </div>
                  
                  <div class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-800 rounded-xl border border-gray-200/50 dark:border-gray-700/50">
                    <UIcon name="lucide:mail" class="text-primary text-lg flex-shrink-0" />
                    <div class="flex-1 min-w-0">
                      <p class="font-mono text-sm font-bold truncate">{{ dept.email }}</p>
                    </div>
                    <UButton
                      :to="`mailto:${dept.email}`"
                      size="xs"
                      variant="outline"
                      class="font-semibold flex-shrink-0"
                    >
                      Email
                    </UButton>
                  </div>
              </div>

              <!-- Specialties -->
              <div>
                <h4 class="font-bold text-sm md:text-base text-gray-600 dark:text-gray-400 uppercase tracking-wider mb-3">Specialties</h4>
                <div class="flex flex-wrap gap-2">
                  <span
                    v-for="specialty in dept.specialties"
                    :key="specialty"
                    class="bg-primary/10 text-primary px-3 py-2 rounded-full text-xs md:text-sm font-bold tracking-wide"
                  >
                    {{ specialty }}
                  </span>
                </div>
              </div>
            </div>
          </UCard>
        </div>
      </UContainer>
    </UPageSection>

    <!-- Service Hours & Response Times -->
    <UPageSection class="relative overflow-hidden">
      <!-- Background Pattern -->
      <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4wMyI+PGNpcmNsZSBjeD0iMzAiIGN5PSIzMCIgcj0iMSIvPjwvZz48L2c+PC9zdmc+')] opacity-40"></div>
      
      <UContainer class="relative z-10">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-black text-gray-900 dark:text-white mb-6 leading-tight tracking-tight">
            Service Hours & <span class="bg-gradient-to-r from-green-500 to-blue-500 bg-clip-text text-transparent">Response Times</span>
          </h2>
          <p class="text-xl md:text-2xl text-gray-600 dark:text-gray-300 max-w-4xl mx-auto leading-relaxed font-medium">
            Know when and how <span class="text-primary font-semibold">quickly</span> we can assist you
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div
            v-for="service in serviceHours"
            :key="service.service"
            class="text-center"
          >
            <UCard class="h-full hover:shadow-lg transition-all duration-300 hover:-translate-y-1">
              <div class="space-y-4">
                <div class="flex justify-center">
                  <div :class="[
                    'w-16 h-16 rounded-full flex items-center justify-center',
                    service.color === 'red' ? 'bg-red-100 text-red-600' :
                    service.color === 'green' ? 'bg-green-100 text-green-600' :
                    service.color === 'blue' ? 'bg-blue-100 text-blue-600' :
                    'bg-primary/10 text-primary'
                  ]">
                    <UIcon :name="service.icon" class="w-8 h-8" />
                  </div>
                </div>
                
                <div>
                  <h3 class="font-black text-lg md:text-xl mb-3 tracking-tight">{{ service.service }}</h3>
                  <p :class="[
                    'font-mono text-sm md:text-base font-black mb-3 tracking-wide',
                    service.color === 'red' ? 'text-red-600' :
                    service.color === 'green' ? 'text-green-600' :
                    service.color === 'blue' ? 'text-blue-600' :
                    'text-primary'
                  ]">
                    {{ service.hours }}
                  </p>
                  <p class="text-sm md:text-base text-gray-600 dark:text-gray-400 font-medium leading-relaxed">{{ service.description }}</p>
                </div>
              </div>
            </UCard>
          </div>
        </div>
      </UContainer>
    </UPageSection>

    <!-- Email Templates Section -->
    <UPageSection class="bg-gray-50 dark:bg-gray-900">
      <UContainer>
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-black text-gray-900 dark:text-white mb-6 leading-tight tracking-tight">
            Professional <span class="bg-gradient-to-r from-purple-500 to-pink-500 bg-clip-text text-transparent">Email Templates</span>
          </h2>
          <p class="text-xl md:text-2xl text-gray-600 dark:text-gray-300 max-w-4xl mx-auto leading-relaxed font-medium">
            Use our <span class="text-primary font-semibold">pre-written templates</span> to compose professional emails quickly and efficiently
          </p>
        </div>

        <EmailTemplates />
      </UContainer>
    </UPageSection>

    <!-- Office Locations with Tech Variant -->
    <OfficeLocations 
      :offices="offices" 
      variant="tech"
      title="Visit Our Offices"
      description="Meet our team in person at any of our strategically located offices across Australia."
    />

    <!-- Enhanced FAQ Section -->
    <UPageSection
      title="Frequently Asked Questions"
      description="Everything you need to know about contacting and working with AGL LOGISTICS."
      class="bg-white dark:bg-gray-900"
    >
      <div class="max-w-4xl mx-auto">
        <UAccordion
          :items="[
            {
              label: 'What\'s the fastest way to get a quote?',
              content: 'For the fastest quote, call our business line at +61 2 8747 3069 during business hours or use our WhatsApp Business for immediate response. Email quotes are typically provided within 4 hours.'
            },
            {
              label: 'How do I track my shipment?',
              content: 'You can track shipments by calling any of our offices, sending a WhatsApp message, or emailing ops@agllogistics.com.au with your reference number. We provide real-time updates and proactive notifications.'
            },
            {
              label: 'Which office should I contact for my location?',
              content: 'Sydney serves NSW and eastern Australia, Melbourne covers Victoria and southern regions, Brisbane handles Queensland and northern areas. Perth (opening soon) will serve Western Australia. Any office can assist with nationwide services.'
            },
            {
              label: 'Do you offer emergency support?',
              content: 'Yes! Our 24/7 emergency hotline (+61 2 8747 3069) provides immediate assistance for critical shipments, urgent issues, and time-sensitive logistics needs. Emergency response within 1 hour guaranteed.'
            },
            {
              label: 'Can I visit your offices without an appointment?',
              content: 'While we welcome walk-ins during business hours, we recommend calling ahead to ensure the right specialist is available. This helps us provide you with the most efficient and comprehensive service.'
            },
            {
              label: 'What information should I have ready when contacting you?',
              content: 'For quotes: origin/destination, cargo details, weight/dimensions, timeline. For tracking: reference number and shipment date. For general inquiries: your company details and specific questions or requirements.'
            },
            {
              label: 'Do you provide multilingual support?',
              content: 'Yes, our team includes multilingual specialists who can assist in Mandarin, Cantonese, Arabic, and other languages. Please mention your language preference when contacting us.'
            },
            {
              label: 'How quickly do you respond to different types of inquiries?',
              content: 'Emergency: Within 1 hour | Urgent business: Within 4 hours | General inquiries: Within 24 hours | Email responses: Within 4 hours during business days | WhatsApp: Usually within 30 minutes during business hours'
            }
          ]"
          :ui="{
            item: {
              padding: 'p-6'
            },
            content: 'text-gray-700 dark:text-gray-300'
          }"
        />
      </div>
    </UPageSection>
  </div>
</template>

<style scoped>
@keyframes spin-slow {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.animate-spin-slow {
  animation: spin-slow 20s linear infinite;
}

.animation-delay-1000 {
  animation-delay: 1s;
}

.animation-delay-2000 {
  animation-delay: 2s;
}
</style>