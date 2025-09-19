<script setup lang="ts">
useSeoMeta({
  title: 'Sydney Office - AGL LOGISTICS',
  description: 'Our Sydney headquarters providing comprehensive freight forwarding and logistics services across NSW and eastern Australia.',
})

// Sydney office data
const office = {
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
  ],
  businessHours: {
    weekdays: 'Monday - Friday: 8:00 AM - 6:00 PM',
    saturday: 'Saturday: 9:00 AM - 2:00 PM',
    sunday: 'Sunday: Closed'
  },
  manager: 'Sarah Johnson',
  specialties: [
    'International freight forwarding',
    'Customs brokerage and compliance',
    'Project cargo management',
    'Emergency logistics support',
    'Supply chain consulting'
  ]
}
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      :title="`${office.city} Office`"
      :description="office.description"
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Sydney City Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <img
            src="/images/syd.png"
            alt="Sydney skyline"
            class="absolute inset-0 w-full h-full object-cover scale-105 transition-transform duration-[20s] hover:scale-110"
          />
          <!-- Gradient overlay for better text readability -->
          <div class="absolute inset-0 bg-gradient-to-b from-black/50 via-black/40 to-black/60"></div>
          <!-- Animated particles overlay -->
          <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4xIj48Y2lyY2xlIGN4PSIzMCIgY3k9IjMwIiByPSIxIi8+PC9nPjwvZz48L3N2Zz4=')] opacity-30 animate-pulse"></div>
        </div>
      </template>

      <template #title>
        <div class="flex items-center justify-center gap-4 mb-4">
          <UIcon name="lucide:star" class="text-yellow-400 text-3xl animate-pulse" />
          <h1 class="text-white drop-shadow-lg">{{ office.city }} Office</h1>
          <span class="bg-primary/20 text-primary px-3 py-1 rounded-full text-sm font-medium">HEAD OFFICE</span>
        </div>
      </template>

      <template #links>
        <UButton
          :label="`Call ${office.city}`"
          :to="`tel:${office.phone}`"
          icon="lucide:phone"
          size="xl"
          color="primary"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          :label="`Email ${office.city}`"
          :to="`mailto:${office.email}`"
          icon="lucide:mail"
          size="xl"
          color="white"
          variant="outline"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Office Details -->
    <UPageSection>
      <div class="grid lg:grid-cols-2 gap-12">
        <!-- Office Information -->
        <div class="space-y-8">
          <div>
            <h2 class="text-2xl font-bold mb-6">Office Information</h2>
            
            <!-- Head Office Badge -->
            <div v-if="office.isHeadquarters" class="mb-6">
              <span class="inline-flex items-center gap-2 bg-primary/10 text-primary px-4 py-2 rounded-full font-semibold">
                <UIcon name="lucide:star" class="w-4 h-4" />
                Head Office
              </span>
            </div>

            <!-- Contact Details -->
            <div class="space-y-6">
              <div class="flex items-start gap-4">
                <UIcon name="lucide:map-pin" class="text-primary text-xl mt-1 flex-shrink-0" />
                <div>
                  <h3 class="font-semibold text-lg mb-2">Address</h3>
                  <p class="text-muted-foreground">{{ office.address }}</p>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <UIcon name="lucide:phone" class="text-primary text-xl mt-1 flex-shrink-0" />
                <div>
                  <h3 class="font-semibold text-lg mb-2">Phone</h3>
                  <a :href="`tel:${office.phone}`" class="text-primary hover:underline text-lg">
                    {{ office.phone }}
                  </a>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <UIcon name="lucide:mail" class="text-primary text-xl mt-1 flex-shrink-0" />
                <div>
                  <h3 class="font-semibold text-lg mb-2">Email</h3>
                  <a :href="`mailto:${office.email}`" class="text-primary hover:underline text-lg">
                    {{ office.email }}
                  </a>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <UIcon name="lucide:user" class="text-primary text-xl mt-1 flex-shrink-0" />
                <div>
                  <h3 class="font-semibold text-lg mb-2">Office Manager</h3>
                  <p class="text-muted-foreground text-lg">{{ office.manager }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Business Hours -->
          <div>
            <h3 class="text-xl font-semibold mb-4">Business Hours</h3>
            <div class="space-y-2">
              <div class="flex items-center gap-3">
                <UIcon name="lucide:clock" class="text-primary" />
                <span>{{ office.businessHours.weekdays }}</span>
              </div>
              <div class="flex items-center gap-3">
                <UIcon name="lucide:clock" class="text-primary" />
                <span>{{ office.businessHours.saturday }}</span>
              </div>
              <div class="flex items-center gap-3">
                <UIcon name="lucide:clock" class="text-primary" />
                <span>{{ office.businessHours.sunday }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Services & Specialties -->
        <div class="space-y-8">
          <!-- Services -->
          <div>
            <h2 class="text-2xl font-bold mb-6">Our Services</h2>
            <div class="grid gap-3">
              <div
                v-for="service in office.services"
                :key="service"
                class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-800 rounded-lg"
              >
                <UIcon name="lucide:check-circle" class="text-green-500 flex-shrink-0" />
                <span class="font-medium">{{ service }}</span>
              </div>
            </div>
          </div>

          <!-- Specialties -->
          <div>
            <h3 class="text-xl font-semibold mb-4">Specialties</h3>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="specialty in office.specialties"
                :key="specialty"
                class="bg-primary/10 text-primary px-3 py-1 rounded-full text-sm font-medium"
              >
                {{ specialty }}
              </span>
            </div>
          </div>

          <!-- Quick Actions -->
          <div>
            <h3 class="text-xl font-semibold mb-4">Quick Actions</h3>
            <div class="grid sm:grid-cols-2 gap-4">
              <UButton
                :to="`tel:${office.phone}`"
                variant="outline"
                block
                size="lg"
              >
                <UIcon name="lucide:phone" class="mr-2" />
                Call Now
              </UButton>
              <UButton
                :to="`mailto:${office.email}`"
                variant="outline"
                block
                size="lg"
              >
                <UIcon name="lucide:mail" class="mr-2" />
                Send Email
              </UButton>
              <UButton
                to="/contact"
                variant="outline"
                block
                size="lg"
              >
                <UIcon name="lucide:message-circle" class="mr-2" />
                Contact Form
              </UButton>
              <UButton
                to="/services/air-freight"
                variant="outline"
                block
                size="lg"
              >
                <UIcon name="lucide:truck" class="mr-2" />
                Our Services
              </UButton>
            </div>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- CTA Section -->
    <UPageSection class="relative bg-gray-50 dark:bg-gray-900 overflow-hidden">
      <!-- CTA Background Image -->
      <div class="absolute inset-0 w-full h-full">
        <img
          src="/images/ctp_syd.png"
          alt="Sydney logistics services"
          class="absolute inset-0 w-full h-full object-cover scale-105"
        />
        <div class="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-purple-900/30 to-black/50"></div>
      </div>
      
      <div class="relative z-10">
        <div class="max-w-4xl mx-auto text-center">
          <!-- 玻璃拟态容器 -->
          <div class="relative backdrop-blur-xl bg-white/80 border border-white/50 rounded-3xl p-8 md:p-12 shadow-2xl">
            <!-- 光效边框 -->
            <div class="absolute inset-0 rounded-3xl bg-gradient-to-r from-white/40 via-transparent to-white/40 p-[1px]">
              <div class="h-full w-full rounded-3xl bg-transparent"></div>
            </div>
            
            <!-- 内容 -->
            <div class="relative">
              <UPageCTA
                title="Ready to ship with us?"
                description="Get in touch with our Sydney team for personalized logistics solutions."
                :links="[
                  {
                    label: 'Get Quote',
                    to: '/contact',
                    size: 'lg'
                  },
                  {
                    label: 'View All Offices',
                    to: '/contact',
                    variant: 'outline',
                    size: 'lg'
                  }
                ]"
                :ui="{
                  title: 'text-gray-900 font-bold',
                  description: 'text-gray-700 font-medium',
                  container: 'p-0'
                }"
              />
            </div>
          </div>
        </div>
      </div>
    </UPageSection>
  </div>
</template>
