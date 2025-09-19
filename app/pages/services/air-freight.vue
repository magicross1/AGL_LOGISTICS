<script setup lang="ts">
useSeoMeta({
  title: 'Air Freight Services - AGL LOGISTICS',
  description: 'Fast and reliable air cargo services connecting Australia to global destinations with priority handling and real-time tracking.',
})
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Air Freight Services"
      description="Fast, reliable air cargo solutions connecting Australia to global destinations with priority handling and comprehensive tracking."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Air Freight Video Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <video
            autoplay
            muted
            loop
            playsinline
            class="absolute inset-0 w-full h-full object-cover"
          >
            <source src="/videos/af.mp4" type="video/mp4">
          </video>
          <!-- Dark overlay for better text readability -->
          <div class="absolute inset-0 bg-black/40"></div>
        </div>
      </template>

      <template #title>
        <h1 class="text-white drop-shadow-lg">Air Freight Services</h1>
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
          label="Track Shipment"
          icon="lucide:search"
          size="xl"
          color="white"
          variant="outline"
          to="/contact"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Service Features -->
    <UPageSection
      title="Why Choose Our Air Freight Services"
      description="Experience the fastest and most reliable air cargo solutions with our comprehensive service offerings."
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <UPageCard
          title="Express Delivery"
          description="Priority air freight services with next-flight-out options for urgent shipments."
          icon="lucide:zap"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Global Network"
          description="Extensive network covering major international destinations from all Australian ports."
          icon="lucide:globe"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Real-time Tracking"
          description="Complete visibility of your shipment from pickup to delivery with live updates."
          icon="lucide:map-pin"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Customs Clearance"
          description="Expert handling of all customs documentation and clearance procedures."
          icon="lucide:clipboard-check"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Specialized Cargo"
          description="Handling of temperature-sensitive, hazardous, and high-value cargo with special care."
          icon="lucide:shield-check"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Competitive Rates"
          description="Best-in-market pricing with flexible payment terms and volume discounts."
          icon="lucide:dollar-sign"
          :ui="{ icon: { base: 'text-primary' } }"
        />
      </div>
    </UPageSection>

    <!-- Service Process -->
    <UPageSection
      title="Our Air Freight Process"
      description="Simple, efficient, and transparent process from booking to delivery."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-4 gap-8">
        <div class="text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon name="lucide:phone" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-2">1. Book & Quote</h3>
          <p class="text-sm text-muted-foreground">Contact us for instant quotes and booking confirmation.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon name="lucide:package" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-2">2. Pickup</h3>
          <p class="text-sm text-muted-foreground">We collect your cargo from your location with proper handling.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon name="lucide:plane" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-2">3. Transport</h3>
          <p class="text-sm text-muted-foreground">Fast air transport with real-time tracking and updates.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon name="lucide:check-circle" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-2">4. Delivery</h3>
          <p class="text-sm text-muted-foreground">Safe delivery to destination with proof of delivery.</p>
        </div>
      </div>
    </UPageSection>

    <!-- Contact CTA -->
    <UPageCTA
      title="Ready to ship with air freight?"
      description="Get competitive quotes for your air cargo needs. Our experts are ready to help you choose the best shipping solution."
      :links="[
        {
          label: 'Get Air Freight Quote',
          to: '/contact',
          color: 'primary'
        },
        {
          label: 'Call +61 2 9999 0000',
          to: 'tel:+61299990000',
          variant: 'outline'
        }
      ]"
    />
  </div>
</template>
