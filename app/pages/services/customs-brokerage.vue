<script setup lang="ts">
useSeoMeta({
  title: 'Customs Brokerage Services - AGL LOGISTICS',
  description: 'Expert customs clearance services ensuring compliant and efficient processing of imports and exports across Australia.',
})
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Customs Brokerage Services"
      description="Expert customs clearance and compliance services ensuring smooth and efficient processing of your imports and exports."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Customs Brokerage Video Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <video
            autoplay
            muted
            loop
            playsinline
            class="absolute inset-0 w-full h-full object-cover"
          >
            <source src="/videos/clear.mp4" type="video/mp4">
          </video>
          <!-- Dark overlay for better text readability -->
          <div class="absolute inset-0 bg-black/40"></div>
        </div>
      </template>

      <template #title>
        <h1 class="text-white drop-shadow-lg">Customs Brokerage Services</h1>
      </template>

      <template #links>
        <UButton
          label="Get Customs Quote"
          icon="lucide:arrow-right"
          trailing
          color="primary"
          to="/contact"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="Duty Calculator"
          icon="lucide:calculator"
          size="xl"
          color="white"
          variant="outline"
          to="/contact"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Services Overview -->
    <UPageSection
      title="Comprehensive Customs Services"
      description="Full-service customs brokerage with expert knowledge of Australian import and export regulations."
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <UPageCard
          title="Import Clearance"
          description="Complete import customs clearance including duty calculation, permit processing, and compliance verification."
          icon="lucide:package-open"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Export Documentation"
          description="Expert preparation of export documentation including certificates of origin and export permits."
          icon="lucide:file-text"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Duty Optimization"
          description="Strategic duty planning and tariff classification to minimize costs and ensure compliance."
          icon="lucide:trending-down"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Quarantine Services"
          description="AQIS coordination and biosecurity compliance for agricultural and food products."
          icon="lucide:shield-alert"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Trade Compliance"
          description="Ongoing compliance monitoring and advice on changing trade regulations and requirements."
          icon="lucide:book-open"
          :ui="{ icon: { base: 'text-primary' } }"
        />
        <UPageCard
          title="Audit Support"
          description="Customs audit preparation and representation with comprehensive record management."
          icon="lucide:search-check"
          :ui="{ icon: { base: 'text-primary' } }"
        />
      </div>
    </UPageSection>

    <!-- Documentation Services -->
    <UPageSection
      title="Documentation & Compliance"
      description="Expert handling of all customs documentation and regulatory requirements."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-2 gap-12">
        <div>
          <h3 class="text-xl font-semibold mb-6">Import Documentation</h3>
          <div class="space-y-3">
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Import Declarations (N10)</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Customs Value Declarations</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Import Permits & Licenses</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Quarantine Certificates</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Duty Deferral Applications</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">FTA Preference Claims</span>
            </div>
          </div>
        </div>

        <div>
          <h3 class="text-xl font-semibold mb-6">Export Documentation</h3>
          <div class="space-y-3">
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Export Declarations (EXD)</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Certificates of Origin</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Export Permits & Licenses</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Phytosanitary Certificates</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Health Certificates</span>
            </div>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:check" class="text-primary" />
              <span class="text-sm">Commercial Invoices</span>
            </div>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- Compliance Programs -->
    <UPageSection
      title="Trade Compliance Programs"
      description="Specialized programs to streamline your customs processes and ensure ongoing compliance."
    >
      <div class="grid md:grid-cols-2 gap-8">
        <UCard>
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:zap" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Trusted Trader Program</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <p class="text-muted-foreground">Streamlined customs processing for compliant businesses with enhanced security measures.</p>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Benefits:</h4>
              <ul class="text-sm space-y-1 text-muted-foreground">
                <li>• Reduced examination rates</li>
                <li>• Priority processing</li>
                <li>• Simplified procedures</li>
                <li>• Account management support</li>
                <li>• Mutual recognition benefits</li>
              </ul>
            </div>

            <UButton variant="outline" size="sm">
              Learn More
            </UButton>
          </div>
        </UCard>

        <UCard>
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:building" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Warehouse Licensing</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <p class="text-muted-foreground">Licensed warehouse facilities for duty-free storage and manufacturing operations.</p>
            
            <div class="space-y-2">
              <h4 class="font-semibold">Services:</h4>
              <ul class="text-sm space-y-1 text-muted-foreground">
                <li>• Bonded warehouse operations</li>
                <li>• Manufacturing in bond</li>
                <li>• Duty deferral programs</li>
                <li>• Re-export facilitation</li>
                <li>• Value-added services</li>
              </ul>
            </div>

            <UButton variant="outline" size="sm">
              View Facilities
            </UButton>
          </div>
        </UCard>
      </div>
    </UPageSection>

    <!-- Process Timeline -->
    <UPageSection
      title="Customs Clearance Process"
      description="Our streamlined process ensures fast and compliant customs clearance for your shipments."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="relative">
        <!-- Timeline -->
        <div class="grid md:grid-cols-5 gap-8">
          <div class="text-center">
            <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
              1
            </div>
            <h3 class="font-semibold mb-2">Document Review</h3>
            <p class="text-sm text-muted-foreground">Review and verify all shipping documents and commercial invoices.</p>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
              2
            </div>
            <h3 class="font-semibold mb-2">Classification</h3>
            <p class="text-sm text-muted-foreground">Accurate tariff classification and duty calculation.</p>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
              3
            </div>
            <h3 class="font-semibold mb-2">Declaration</h3>
            <p class="text-sm text-muted-foreground">Electronic lodgment of customs declarations.</p>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
              4
            </div>
            <h3 class="font-semibold mb-2">Assessment</h3>
            <p class="text-sm text-muted-foreground">Customs assessment and examination (if required).</p>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
              5
            </div>
            <h3 class="font-semibold mb-2">Release</h3>
            <p class="text-sm text-muted-foreground">Cargo release and delivery coordination.</p>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- Contact CTA -->
    <UPageCTA
      title="Need expert customs brokerage?"
      description="Our licensed customs brokers are ready to handle your import and export clearance requirements. Get compliant, efficient service every time."
      :links="[
        {
          label: 'Get Customs Quote',
          to: '/contact',
          color: 'primary'
        },
        {
          label: 'Broker Consultation',
          to: 'tel:+61299990000',
          variant: 'outline'
        }
      ]"
    />
  </div>
</template>
