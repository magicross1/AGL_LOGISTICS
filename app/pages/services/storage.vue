<script setup lang="ts">
useSeoMeta({
  title: 'Storage & Warehousing Services - AGL LOGISTICS',
  description: 'Modern warehouse facilities with climate control and security systems for safe cargo storage and distribution across Australia.',
})
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Storage & Warehousing"
      description="Modern warehouse facilities with advanced security, climate control, and distribution services across major Australian cities."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Storage & Warehousing Video Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <video
            autoplay
            muted
            loop
            playsinline
            class="absolute inset-0 w-full h-full object-cover"
          >
            <source src="/videos/storage.mp4" type="video/mp4">
          </video>
          <!-- Dark overlay for better text readability -->
          <div class="absolute inset-0 bg-black/40"></div>
        </div>
      </template>

      <template #title>
        <h1 class="text-white drop-shadow-lg">Storage & Warehousing</h1>
      </template>

      <template #links>
        <UButton
          label="Get Storage Quote"
          icon="lucide:arrow-right"
          trailing
          color="primary"
          to="/contact"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="Tour Our Facilities"
          icon="lucide:camera"
          size="xl"
          color="white"
          variant="outline"
          to="/contact"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Storage Solutions -->
    <UPageSection
      title="Comprehensive Storage Solutions"
      description="Flexible warehousing options designed to meet diverse storage and distribution requirements."
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <UPageCard
          title="General Warehousing"
          description="Secure dry storage for general cargo with flexible short-term and long-term options."
          icon="lucide:warehouse"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Climate Controlled"
          description="Temperature and humidity controlled environments for sensitive and perishable goods."
          icon="lucide:thermometer"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Bonded Storage"
          description="Customs bonded facilities for duty-free storage of imported goods awaiting clearance."
          icon="lucide:shield-check"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Hazmat Storage"
          description="Licensed dangerous goods storage facilities with specialized handling and safety systems."
          icon="lucide:alert-triangle"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Cross Docking"
          description="Efficient transfer and consolidation services to minimize storage time and costs."
          icon="lucide:shuffle"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Distribution Services"
          description="Last-mile delivery and distribution services from our strategically located facilities."
          icon="lucide:truck"
          :ui="{ icon: { base: 'text-primary' } }"
        />
      </div>
    </UPageSection>

    <!-- Facility Features -->
    <UPageSection
      title="State-of-the-Art Facilities"
      description="Modern warehouse infrastructure with advanced technology and security systems."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-2 gap-12">
        <div>
          <h3 class="text-xl font-semibold mb-6">Security & Safety</h3>
          <div class="space-y-4">
            <div class="flex items-start gap-3">
              <UIcon name="lucide:shield" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">24/7 Security Monitoring</h4>
                <p class="text-sm text-muted-foreground">CCTV surveillance, alarm systems, and on-site security personnel.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:key" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Access Control</h4>
                <p class="text-sm text-muted-foreground">Biometric access systems and visitor management protocols.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:flame" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Fire Protection</h4>
                <p class="text-sm text-muted-foreground">Advanced sprinkler systems and smoke detection throughout facilities.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:hard-hat" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Safety Compliance</h4>
                <p class="text-sm text-muted-foreground">Full OH&S compliance with regular safety audits and training.</p>
              </div>
            </div>
          </div>
        </div>

        <div>
          <h3 class="text-xl font-semibold mb-6">Technology & Equipment</h3>
          <div class="space-y-4">
            <div class="flex items-start gap-3">
              <UIcon name="lucide:scan" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Warehouse Management System</h4>
                <p class="text-sm text-muted-foreground">Real-time inventory tracking with barcode and RFID technology.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:forklift" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Material Handling</h4>
                <p class="text-sm text-muted-foreground">Modern forklifts, reach trucks, and automated handling equipment.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:monitor" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Environmental Monitoring</h4>
                <p class="text-sm text-muted-foreground">Continuous temperature and humidity monitoring with alerts.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <UIcon name="lucide:wifi" class="text-primary mt-1" />
              <div>
                <h4 class="font-semibold">Connectivity</h4>
                <p class="text-sm text-muted-foreground">High-speed internet and EDI connectivity for seamless operations.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- Facility Locations -->
    <UPageSection
      title="Warehouse Locations"
      description="Strategic locations across Australia providing comprehensive coverage and quick access to major ports and transport networks."
    >
      <div class="grid md:grid-cols-2 gap-8">
        <UCard>
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:map-pin" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Sydney Facility</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <div class="grid grid-cols-2 gap-4 text-sm">
              <div>
                <span class="font-semibold">Total Area:</span>
                <p>15,000 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Climate Control:</span>
                <p>5,000 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Bonded Storage:</span>
                <p>3,000 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Loading Docks:</span>
                <p>20 bays</p>
              </div>
            </div>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Features:</h4>
              <ul class="text-sm space-y-1 text-muted-foreground">
                <li>• Rail siding access</li>
                <li>• 24/7 operations</li>
                <li>• Dangerous goods licensed</li>
                <li>• 15 minutes from Port Botany</li>
              </ul>
            </div>
          </div>
        </UCard>

        <UCard>
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:map-pin" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Melbourne Facility</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <div class="grid grid-cols-2 gap-4 text-sm">
              <div>
                <span class="font-semibold">Total Area:</span>
                <p>12,000 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Climate Control:</span>
                <p>4,000 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Bonded Storage:</span>
                <p>2,500 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Loading Docks:</span>
                <p>16 bays</p>
              </div>
            </div>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Features:</h4>
              <ul class="text-sm space-y-1 text-muted-foreground">
                <li>• Container storage yard</li>
                <li>• Cross-docking facilities</li>
                <li>• Pharmaceutical GDP certified</li>
                <li>• 20 minutes from Port of Melbourne</li>
              </ul>
            </div>
          </div>
        </UCard>

        <UCard>
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:map-pin" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Brisbane Facility</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <div class="grid grid-cols-2 gap-4 text-sm">
              <div>
                <span class="font-semibold">Total Area:</span>
                <p>10,000 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Climate Control:</span>
                <p>3,500 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Bonded Storage:</span>
                <p>2,000 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Loading Docks:</span>
                <p>12 bays</p>
              </div>
            </div>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Features:</h4>
              <ul class="text-sm space-y-1 text-muted-foreground">
                <li>• Reefer plug-in points</li>
                <li>• Quarantine approved</li>
                <li>• Mining equipment storage</li>
                <li>• 25 minutes from Port of Brisbane</li>
              </ul>
            </div>
          </div>
        </UCard>

        <UCard>
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:map-pin" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Perth Facility</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <div class="grid grid-cols-2 gap-4 text-sm">
              <div>
                <span class="font-semibold">Total Area:</span>
                <p>8,000 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Climate Control:</span>
                <p>2,500 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Bonded Storage:</span>
                <p>1,500 sqm</p>
              </div>
              <div>
                <span class="font-semibold">Loading Docks:</span>
                <p>10 bays</p>
              </div>
            </div>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Features:</h4>
              <ul class="text-sm space-y-1 text-muted-foreground">
                <li>• Heavy machinery storage</li>
                <li>• Bulk commodity handling</li>
                <li>• Mining logistics hub</li>
                <li>• 30 minutes from Fremantle Port</li>
              </ul>
            </div>
          </div>
        </UCard>
      </div>
    </UPageSection>

    <!-- Contact CTA -->
    <UPageCTA
      title="Need secure storage solutions?"
      description="Our modern warehouse facilities provide the perfect storage environment for your cargo. Contact us to discuss your specific requirements."
      :links="[
        {
          label: 'Get Storage Quote',
          to: '/contact',
          color: 'primary'
        },
        {
          label: 'Schedule Facility Tour',
          to: 'tel:+61299990000',
          variant: 'outline'
        }
      ]"
    />
  </div>
</template>
