<script setup lang="ts">
useSeoMeta({
  title: 'Special Transports - AGL LOGISTICS',
  description: 'Specialized handling for oversized, hazardous, and high-value cargo with expert project management and custom solutions.',
})
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Special Transports"
      description="Expert handling of oversized, hazardous, and high-value cargo with specialized equipment and dedicated project management."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Special Transports Video Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <video
            autoplay
            muted
            loop
            playsinline
            class="absolute inset-0 w-full h-full object-cover"
          >
            <source src="/videos/truck.mp4" type="video/mp4">
          </video>
          <!-- Dark overlay for better text readability -->
          <div class="absolute inset-0 bg-black/40"></div>
        </div>
      </template>

      <template #title>
        <h1 class="text-white drop-shadow-lg">Special Transports</h1>
      </template>

      <template #links>
        <UButton
          label="Get Specialized Quote"
          icon="lucide:arrow-right"
          trailing
          color="primary"
          to="/contact"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="View Case Studies"
          icon="lucide:folder"
          size="xl"
          color="white"
          variant="outline"
          to="/contact"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Service Categories -->
    <UPageSection
      title="Specialized Transport Solutions"
      description="Comprehensive handling of complex cargo requiring specialized equipment, permits, and expertise."
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <UPageCard
          title="Oversized Cargo"
          description="Heavy lift and out-of-gauge cargo transport with specialized equipment and route planning."
          icon="lucide:truck"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Dangerous Goods"
          description="IATA/IMDG compliant handling of hazardous materials with certified dangerous goods experts."
          icon="lucide:alert-triangle"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="High-Value Cargo"
          description="Secure transport of valuable goods with enhanced security measures and insurance coverage."
          icon="lucide:gem"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Temperature Controlled"
          description="Reefer and pharmaceutical cargo transport with precise temperature monitoring and control."
          icon="lucide:thermometer"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Project Cargo"
          description="End-to-end project logistics for industrial equipment, machinery, and infrastructure projects."
          icon="lucide:construction"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Live Animals"
          description="Specialized livestock and pet transport with animal welfare compliance and veterinary coordination."
          icon="lucide:heart"
          :ui="{ icon: { base: 'text-primary' } }"
        />
      </div>
    </UPageSection>

    <!-- Capabilities -->
    <UPageSection
      title="Our Special Transport Capabilities"
      description="Advanced equipment and expertise to handle your most challenging shipping requirements."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-2 gap-12">
        <div>
          <h3 class="text-xl font-semibold mb-6">Equipment & Resources</h3>
          <div class="space-y-4">
            <div class="flex items-start gap-3">
              <UIcon name="lucide:check-circle" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Heavy Lift Equipment</h4>
                <p class="text-sm text-muted-foreground">Cranes, forklifts, and specialized handling equipment up to 500 tons capacity.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:check-circle" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Specialized Trailers</h4>
                <p class="text-sm text-muted-foreground">Low-bed, extendable, and multi-axle trailers for oversized cargo transport.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:check-circle" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Climate Control</h4>
                <p class="text-sm text-muted-foreground">Temperature and humidity controlled environments for sensitive cargo.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:check-circle" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Security Systems</h4>
                <p class="text-sm text-muted-foreground">GPS tracking, armed escorts, and secure facilities for high-value shipments.</p>
              </div>
            </div>
          </div>
        </div>

        <div>
          <h3 class="text-xl font-semibold mb-6">Compliance & Certifications</h3>
          <div class="space-y-4">
            <div class="flex items-start gap-3">
              <UIcon name="lucide:shield-check" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Dangerous Goods Certified</h4>
                <p class="text-sm text-muted-foreground">IATA and IMDG certified staff for hazardous material handling.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:shield-check" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Heavy Haulage Permits</h4>
                <p class="text-sm text-muted-foreground">All necessary permits and approvals for oversized cargo movement.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:shield-check" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Animal Welfare Compliance</h4>
                <p class="text-sm text-muted-foreground">IATA Live Animals Regulations and veterinary partnerships.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:shield-check" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Pharmaceutical GDP</h4>
                <p class="text-sm text-muted-foreground">Good Distribution Practice compliance for pharmaceutical logistics.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- Process -->
    <UPageSection
      title="Special Transport Process"
      description="Our systematic approach ensures safe and compliant handling of your specialized cargo."
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon name="lucide:search" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-2">1. Assessment</h3>
          <p class="text-sm text-muted-foreground">Detailed cargo assessment and feasibility study for transport requirements.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon name="lucide:map" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-2">2. Planning</h3>
          <p class="text-sm text-muted-foreground">Route planning, permit acquisition, and equipment selection.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon name="lucide:settings" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-2">3. Execution</h3>
          <p class="text-sm text-muted-foreground">Professional handling and transport with dedicated project management.</p>
        </div>
        <div class="text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon name="lucide:check-circle-2" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-2">4. Delivery</h3>
          <p class="text-sm text-muted-foreground">Safe delivery with comprehensive documentation and reporting.</p>
        </div>
      </div>
    </UPageSection>

    <!-- Contact CTA -->
    <UPageCTA
      title="Need specialized transport solutions?"
      description="Our special transport experts are ready to handle your most challenging cargo. Contact us for a detailed consultation and custom solution."
      :links="[
        {
          label: 'Discuss Your Project',
          to: '/contact',
          color: 'primary'
        },
        {
          label: 'Emergency Hotline',
          to: 'tel:+61299990000',
          variant: 'outline'
        }
      ]"
    />
  </div>
</template>
