<script setup lang="ts">
useSeoMeta({
  title: 'Sea Freight Services - AGL LOGISTICS',
  description: 'Cost-effective ocean freight solutions for FCL and LCL shipments with comprehensive port-to-port services across Australia.',
})
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Sea Freight Services"
      description="Cost-effective ocean freight solutions for both FCL and LCL shipments with comprehensive port-to-port services and global coverage."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Sea Freight Video Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <video
            autoplay
            muted
            loop
            playsinline
            class="absolute inset-0 w-full h-full object-cover"
          >
            <source src="/videos/sf.mp4" type="video/mp4">
          </video>
          <!-- Dark overlay for better text readability -->
          <div class="absolute inset-0 bg-black/40"></div>
        </div>
      </template>

      <template #title>
        <h1 class="text-white drop-shadow-lg">Sea Freight Services</h1>
      </template>

      <template #links>
        <UButton
          label="Get Quote"
          icon="lucide:arrow-right"
          trailing
          color="primary"
          to="/contact"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="Port Schedules"
          icon="lucide:calendar"
          size="xl"
          color="white"
          variant="outline"
          to="/contact"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Service Types -->
    <UPageSection
      title="Sea Freight Solutions"
      description="Choose from our flexible ocean freight options designed to meet your specific shipping requirements."
    >
      <div class="grid md:grid-cols-2 gap-8 mb-12">
        <UCard>
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:container" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Full Container Load (FCL)</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <p class="text-muted-foreground">Dedicated container space for large volume shipments with maximum security and efficiency.</p>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Benefits:</h4>
              <ul class="text-sm space-y-1 text-muted-foreground">
                <li>• Exclusive container use</li>
                <li>• Faster customs clearance</li>
                <li>• Lower risk of damage</li>
                <li>• Cost-effective for large volumes</li>
                <li>• Direct port-to-port delivery</li>
              </ul>
            </div>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Container Sizes:</h4>
              <div class="grid grid-cols-2 gap-2 text-sm">
                <span class="bg-gray-100 dark:bg-gray-800 p-2 rounded">20' Standard</span>
                <span class="bg-gray-100 dark:bg-gray-800 p-2 rounded">40' Standard</span>
                <span class="bg-gray-100 dark:bg-gray-800 p-2 rounded">40' High Cube</span>
                <span class="bg-gray-100 dark:bg-gray-800 p-2 rounded">45' High Cube</span>
              </div>
            </div>
          </div>
        </UCard>

        <UCard>
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:boxes" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Less Container Load (LCL)</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <p class="text-muted-foreground">Shared container space for smaller shipments with flexible consolidation services.</p>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Benefits:</h4>
              <ul class="text-sm space-y-1 text-muted-foreground">
                <li>• Cost-effective for small volumes</li>
                <li>• No minimum volume requirements</li>
                <li>• Regular sailing schedules</li>
                <li>• Professional consolidation</li>
                <li>• Flexible pickup options</li>
              </ul>
            </div>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Consolidation Ports:</h4>
              <div class="grid grid-cols-2 gap-2 text-sm">
                <span class="bg-gray-100 dark:bg-gray-800 p-2 rounded">Sydney</span>
                <span class="bg-gray-100 dark:bg-gray-800 p-2 rounded">Melbourne</span>
                <span class="bg-gray-100 dark:bg-gray-800 p-2 rounded">Brisbane</span>
                <span class="bg-gray-100 dark:bg-gray-800 p-2 rounded">Perth</span>
              </div>
            </div>
          </div>
        </UCard>
      </div>
    </UPageSection>

    <!-- Additional Services -->
    <UPageSection
      title="Additional Sea Freight Services"
      description="Comprehensive support services to ensure smooth ocean freight operations."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        <UPageCard
          title="Port Services"
          description="Complete port handling, documentation, and coordination services."
          icon="lucide:anchor"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Cargo Insurance"
          description="Comprehensive marine insurance coverage for your valuable shipments."
          icon="lucide:shield"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Warehousing"
          description="Secure storage facilities at major ports for consolidation and distribution."
          icon="lucide:warehouse"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Documentation"
          description="Expert handling of bills of lading, certificates, and shipping documentation."
          icon="lucide:file-text"
          :ui="{ icon: { base: 'text-primary' } }"
        />
      </div>
    </UPageSection>

    <!-- Transit Times -->
    <UPageSection
      title="Transit Times & Routes"
      description="Typical transit times from major Australian ports to key international destinations."
    >
      <div class="overflow-x-auto">
        <table class="w-full border-collapse border border-gray-200 dark:border-gray-700">
          <thead>
            <tr class="bg-gray-50 dark:bg-gray-800">
              <th class="border border-gray-200 dark:border-gray-700 p-3 text-left font-semibold">From Australia</th>
              <th class="border border-gray-200 dark:border-gray-700 p-3 text-left font-semibold">To Destination</th>
              <th class="border border-gray-200 dark:border-gray-700 p-3 text-left font-semibold">Transit Time</th>
              <th class="border border-gray-200 dark:border-gray-700 p-3 text-left font-semibold">Frequency</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Sydney/Melbourne</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Shanghai, China</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">18-22 days</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Weekly</td>
            </tr>
            <tr class="bg-gray-25 dark:bg-gray-900">
              <td class="border border-gray-200 dark:border-gray-700 p-3">Brisbane</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Los Angeles, USA</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">14-18 days</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">3x Weekly</td>
            </tr>
            <tr>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Perth</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Rotterdam, Europe</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">28-32 days</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Weekly</td>
            </tr>
            <tr class="bg-gray-25 dark:bg-gray-900">
              <td class="border border-gray-200 dark:border-gray-700 p-3">Sydney</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Singapore</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">12-16 days</td>
              <td class="border border-gray-200 dark:border-gray-700 p-3">Daily</td>
            </tr>
          </tbody>
        </table>
      </div>
    </UPageSection>

    <!-- Contact CTA -->
    <UPageCTA
      title="Ready to ship via sea freight?"
      description="Get competitive ocean freight quotes for FCL and LCL shipments. Our sea freight experts will find the best solution for your needs."
      :links="[
        {
          label: 'Get Sea Freight Quote',
          to: '/contact',
          color: 'primary'
        },
        {
          label: 'Download Rate Guide',
          to: '/service-center/downloads',
          variant: 'outline'
        }
      ]"
    />
  </div>
</template>
