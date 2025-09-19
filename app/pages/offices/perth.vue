<script setup lang="ts">
useSeoMeta({
  title: 'Perth Office - AGL LOGISTICS',
  description: 'Our Perth office expanding soon to serve Western Australia with mining and resources logistics expertise.',
})

const office = {
  city: 'Perth',
  status: 'coming_soon' as const,
  isHeadquarters: false,
  address: 'Coming Soon',
  phone: '+61 2 8747 3069', // Redirect to Sydney for now
  email: 'ops@agllogistics.com.au',
  description: 'Western Australia operations expanding soon to serve mining and resources sector.',
  services: [
    'Mining and resources expertise',
    'Bulk cargo handling',
    'International freight services',
    'Customs and quarantine',
    'Heavy machinery transport',
    'Remote area delivery'
  ],
  businessHours: {
    weekdays: 'Opening Soon',
    saturday: 'Opening Soon',
    sunday: 'Opening Soon'
  },
  manager: 'TBA',
  specialties: [
    'Mining sector logistics',
    'Heavy equipment transport',
    'Remote area services',
    'Bulk cargo handling',
    'Resources industry expertise'
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
        <!-- Perth City Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <img
            src="/images/per.png"
            alt="Perth skyline"
            class="absolute inset-0 w-full h-full object-cover scale-105 transition-transform duration-[20s] hover:scale-110 grayscale-[30%]"
          />
          <!-- Special overlay for coming soon status -->
          <div class="absolute inset-0 bg-gradient-to-b from-yellow-900/60 via-black/50 to-black/70"></div>
          <!-- Animated particles overlay -->
          <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC41Ij48Y2lyY2xlIGN4PSIzMCIgY3k9IjMwIiByPSIxIi8+PC9nPjwvZz48L3N2Zz4=')] opacity-20 animate-pulse"></div>
        </div>
      </template>

      <template #title>
        <div class="flex items-center justify-center gap-4 mb-4">
          <UIcon name="lucide:clock" class="text-yellow-400 text-3xl animate-pulse" />
          <h1 class="text-white drop-shadow-lg">{{ office.city }} Office</h1>
          <span class="bg-yellow-500/20 text-yellow-300 px-3 py-1 rounded-full text-sm font-medium">COMING SOON</span>
        </div>
      </template>

      <template #links>
        <UButton
          label="Contact Sydney Office"
          :to="`tel:${office.phone}`"
          icon="lucide:phone"
          size="xl"
          color="primary"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="Email Us"
          :to="`mailto:${office.email}`"
          icon="lucide:mail"
          size="xl"
          color="white"
          variant="outline"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Coming Soon Notice -->
    <UPageSection>
      <div class="text-center mb-12">
        <div class="inline-flex items-center gap-3 bg-yellow-100 dark:bg-yellow-900/30 text-yellow-800 dark:text-yellow-200 px-6 py-3 rounded-full font-semibold text-lg mb-6">
          <UIcon name="lucide:clock" class="w-5 h-5" />
          Coming Soon
        </div>
        <h2 class="text-3xl font-bold mb-4">Perth Office Opening Soon</h2>
        <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
          We're expanding our operations to Western Australia to better serve the mining and resources sector. 
          In the meantime, our Sydney headquarters can assist with all your Perth-area logistics needs.
        </p>
      </div>
    </UPageSection>

    <!-- Office Details -->
    <UPageSection>
      <div class="grid lg:grid-cols-2 gap-12">
        <!-- Office Information -->
        <div class="space-y-8">
          <div>
            <h2 class="text-2xl font-bold mb-6">Future Office Information</h2>

            <!-- Contact Details -->
            <div class="space-y-6">
              <div class="flex items-start gap-4">
                <UIcon name="lucide:map-pin" class="text-yellow-500 text-xl mt-1 flex-shrink-0" />
                <div>
                  <h3 class="font-semibold text-lg mb-2">Address</h3>
                  <p class="text-muted-foreground">{{ office.address }}</p>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <UIcon name="lucide:phone" class="text-primary text-xl mt-1 flex-shrink-0" />
                <div>
                  <h3 class="font-semibold text-lg mb-2">Phone (Sydney HQ)</h3>
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
                <UIcon name="lucide:user" class="text-yellow-500 text-xl mt-1 flex-shrink-0" />
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
                <UIcon name="lucide:clock" class="text-yellow-500" />
                <span class="text-muted-foreground">{{ office.businessHours.weekdays }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Services & Specialties -->
        <div class="space-y-8">
          <!-- Planned Services -->
          <div>
            <h2 class="text-2xl font-bold mb-6">Planned Services</h2>
            <div class="grid gap-3">
              <div
                v-for="service in office.services"
                :key="service"
                class="flex items-center gap-3 p-3 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg"
              >
                <UIcon name="lucide:clock" class="text-yellow-500 flex-shrink-0" />
                <span class="font-medium">{{ service }}</span>
              </div>
            </div>
          </div>

          <!-- Specialties -->
          <div>
            <h3 class="text-xl font-semibold mb-4">Planned Specialties</h3>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="specialty in office.specialties"
                :key="specialty"
                class="bg-yellow-100 dark:bg-yellow-900/30 text-yellow-800 dark:text-yellow-200 px-3 py-1 rounded-full text-sm font-medium"
              >
                {{ specialty }}
              </span>
            </div>
          </div>

          <!-- Current Actions -->
          <div>
            <h3 class="text-xl font-semibold mb-4">Contact Us Now</h3>
            <p class="text-muted-foreground mb-4">
              While our Perth office is being established, our Sydney headquarters is ready to assist with all your Western Australia logistics needs.
            </p>
            <div class="grid sm:grid-cols-2 gap-4">
              <UButton
                :to="`tel:${office.phone}`"
                variant="outline"
                block
                size="lg"
              >
                <UIcon name="lucide:phone" class="mr-2" />
                Call Sydney
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
          src="/images/ctp_per.png"
          alt="Perth logistics services"
          class="absolute inset-0 w-full h-full object-cover scale-105"
        />
        <div class="absolute inset-0 bg-gradient-to-br from-yellow-900/20 via-orange-900/30 to-black/50"></div>
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
                title="Need Perth logistics now?"
                description="Our Sydney team can handle your Western Australia logistics requirements while we establish our Perth presence."
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
