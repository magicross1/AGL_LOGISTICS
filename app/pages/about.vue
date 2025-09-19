<script setup lang="ts">
useSeoMeta({
  title: 'About AGL LOGISTICS - Professional Freight Forwarding',
  description: 'Learn about AGL LOGISTICS, Australia\'s trusted freight forwarding partner with over 20 years of experience in logistics and supply chain solutions.',
})

const stats = [
  { label: 'Years of Experience', value: '30+', icon: 'lucide:calendar' },
  { label: 'Satisfied Customers', value: '5,000+', icon: 'lucide:users' },
  { label: 'Shipments Handled', value: '100K+', icon: 'lucide:package' },
  { label: 'Countries Served', value: '50+', icon: 'lucide:globe' }
]

const team = [
  {
    name: 'Walter Wang',
    position: 'Chief Executive Officer',
    experience: '25 years in logistics',
    bio: 'James founded AGL LOGISTICS with a vision to revolutionize freight forwarding in Australia. His extensive experience in international trade has been instrumental in establishing our global network.',
    image: '/images/team/james-mitchell.jpg',
    linkedin: 'https://linkedin.com/in/james-mitchell'
  },
  {
    name: 'Haze Gao',
    position: 'Chief Operations Officer',
    experience: '20 years in operations',
    bio: 'Sarah oversees all operational aspects of our business, ensuring seamless service delivery across all our facilities. Her expertise in supply chain optimization drives our operational excellence.',
    image: '/images/team/sarah-johnson.jpg',
    linkedin: 'https://linkedin.com/in/sarah-johnson'
  },
  {
    name: 'Queenie Chen',
    position: 'Head of Customs & Compliance',
    experience: '18 years in customs',
    bio: 'Michael leads our customs brokerage division with deep expertise in Australian trade regulations. His team ensures all shipments meet compliance requirements efficiently.',
    image: '/images/team/michael-chen.jpg',
    linkedin: 'https://linkedin.com/in/michael-chen'
  },
  {
    name: 'Emma Wilson',
    position: 'General Manager - Perth',
    experience: '15 years in mining logistics',
    bio: 'Emma specializes in mining and resources logistics, managing our Perth operations and serving the unique needs of Western Australia\'s mining industry.',
    image: '/images/team/emma-wilson.jpg',
    linkedin: 'https://linkedin.com/in/emma-wilson'
  }
]

const values = [
  {
    title: 'Reliability',
    description: 'We deliver on our promises with consistent, dependable service that our customers can count on.',
    icon: 'lucide:shield-check'
  },
  {
    title: 'Innovation',
    description: 'Continuously improving our processes and technology to provide cutting-edge logistics solutions.',
    icon: 'lucide:lightbulb'
  },
  {
    title: 'Customer Focus',
    description: 'Every decision we make is centered around delivering exceptional value to our customers.',
    icon: 'lucide:heart'
  },
  {
    title: 'Integrity',
    description: 'Operating with transparency, honesty, and ethical business practices in all our relationships.',
    icon: 'lucide:scale'
  },
  {
    title: 'Excellence',
    description: 'Striving for the highest standards in everything we do, from service quality to safety.',
    icon: 'lucide:star'
  },
  {
    title: 'Sustainability',
    description: 'Committed to environmentally responsible practices and sustainable logistics solutions.',
    icon: 'lucide:leaf'
  }
]

const milestones = [
  {
    year: '2015',
    title: 'Company Founded',
    description: 'AGL LOGISTICS established in Sydney with a focus on air freight services.'
  },
  {
    year: '2016',
    title: 'Sea Freight Division',
    description: 'Expanded services to include comprehensive sea freight and customs brokerage.'
  },
  {
    year: '2017',
    title: 'National Expansion',
    description: 'Opened offices in Melbourne, Brisbane, and Perth to serve all major Australian markets.'
  },
  {
    year: '2018',
    title: 'Warehouse Network',
    description: 'Launched modern warehouse facilities with specialized storage capabilities.'
  },
  {
    year: '2019',
    title: 'Technology Innovation',
    description: 'Implemented advanced tracking systems and customer portal for enhanced visibility.'
  },
  {
    year: '2020',
    title: 'Special Transport Division',
    description: 'Established specialized transport capabilities for oversized and dangerous goods.'
  },
  {
    year: '2022',
    title: 'Digital Transformation',
    description: 'Completed comprehensive digital transformation with AI-powered logistics solutions.'
  },
  {
    year: '2024',
    title: 'Sustainability Initiative',
    description: 'Launched green logistics program with carbon-neutral shipping options.'
  }
]

const certifications = [
  {
    name: 'ISO 9001:2015',
    description: 'Quality Management Systems',
    icon: 'lucide:award'
  },
  {
    name: 'IATA Cargo Agent',
    description: 'International Air Transport Association',
    icon: 'lucide:plane'
  },
  {
    name: 'Customs Broker License',
    description: 'Australian Border Force Licensed',
    icon: 'lucide:shield'
  },
  {
    name: 'Dangerous Goods Certified',
    description: 'IATA/IMDG Compliance',
    icon: 'lucide:alert-triangle'
  }
]
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="About AGL LOGISTICS"
      description="Australia's trusted freight forwarding partner with over 20 years of experience delivering comprehensive logistics and supply chain solutions."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- About Video Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <video
            autoplay
            muted
            loop
            playsinline
            class="absolute inset-0 w-full h-full object-cover"
          >
            <source src="/videos/about.mp4" type="video/mp4">
          </video>
          <!-- Dark overlay for better text readability -->
          <div class="absolute inset-0 bg-black/40"></div>
        </div>
      </template>

      <template #title>
        <h1 class="text-white drop-shadow-lg">About AGL LOGISTICS</h1>
      </template>

      <template #links>
        <UButton
          label="Our Services"
          icon="lucide:arrow-right"
          trailing
          color="primary"
          to="/services/air-freight"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="Contact Us"
          icon="lucide:phone"
          size="xl"
          color="white"
          variant="outline"
          to="/contact"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Company Stats -->
    <UPageSection>
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div
          v-for="stat in stats"
          :key="stat.label"
          class="text-center"
        >
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon :name="stat.icon" class="text-2xl text-primary" />
          </div>
          <div class="text-3xl font-bold text-primary mb-2">{{ stat.value }}</div>
          <div class="text-muted-foreground">{{ stat.label }}</div>
        </div>
      </div>
    </UPageSection>

    <!-- Our Story -->
    <UPageSection
      title="Our Story"
      description="From humble beginnings to Australia's leading logistics provider."
      class="relative overflow-hidden"
    >
      <!-- Story Background -->
      <div class="absolute inset-0">
        <img
          src="/images/story.png"
          alt="Our story and company history"
          class="absolute inset-0 w-full h-full object-cover opacity-10"
        />
        <div class="absolute inset-0 bg-gradient-to-br from-white/95 to-gray-50/95 dark:from-gray-900/95 dark:to-gray-800/95"></div>
      </div>

      <UContainer class="relative z-10">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div class="relative">
            <div class="aspect-video rounded-2xl overflow-hidden shadow-2xl border border-gray-200/50 dark:border-gray-700/50">
              <img
                src="/images/story.png"
                alt="AGL LOGISTICS company story"
                class="w-full h-full object-cover hover:scale-105 transition-transform duration-[10s]"
              />
              <!-- Subtle overlay -->
              <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
            </div>

            <!-- Decorative elements -->
            <div class="absolute -top-4 -left-4 w-8 h-8 bg-primary rounded-full opacity-60 animate-pulse"></div>
            <div class="absolute -bottom-4 -right-4 w-6 h-6 bg-blue-500 rounded-full opacity-40 animate-pulse animation-delay-1000"></div>
          </div>

          <div class="space-y-8">
            <div class="relative">
              <div class="flex items-center gap-3 mb-4">
                <UIcon name="lucide:award" class="text-primary text-2xl" />
                <h3 class="text-2xl md:text-3xl font-black tracking-tight">Founded on Excellence</h3>
              </div>
              <p class="text-base md:text-lg text-gray-700 dark:text-gray-300 leading-relaxed font-medium">
                With over 30 years of international freight forwarding experience, AGL Logistics was established in Sydney in 2015. Our team brings <span class="text-primary font-semibold">deep expertise</span>, global perspective, and a commitment to delivering seamless transport solutions.
              </p>
            </div>

            <div class="relative">
              <div class="flex items-center gap-3 mb-4">
                <UIcon name="lucide:trending-up" class="text-primary text-2xl" />
                <h3 class="text-2xl md:text-3xl font-black tracking-tight">Growing with Australia</h3>
              </div>
              <p class="text-base md:text-lg text-gray-700 dark:text-gray-300 leading-relaxed font-medium">
                Our multilingual and highly trained staff work hand-in-hand with leading shipping lines, air cargo agents, and trucking companies. By building <span class="text-primary font-semibold">long-term partnerships</span>, we secure dependable and cost-efficient logistics solutions tailored to Australian businesses and their global connections.
              </p>
            </div>

            <div class="relative">
              <div class="flex items-center gap-3 mb-4">
                <UIcon name="lucide:cpu" class="text-primary text-2xl" />
                <h3 class="text-2xl md:text-3xl font-black tracking-tight">Innovation & Technology</h3>
              </div>
              <p class="text-base md:text-lg text-gray-700 dark:text-gray-300 leading-relaxed font-medium">
                We operate beyond traditional business hours to match global supply chain demands. Combining industry knowledge with proactive service and <span class="text-primary font-semibold">cutting-edge technology</span>, we ensure efficiency, flexibility, and a customer-first experience every step of the way.
              </p>
            </div>
          </div>
        </div>
      </UContainer>
    </UPageSection>

    <!-- Our Values -->
    <UPageSection
      title="Our Values"
      description="The principles that guide everything we do at AGL LOGISTICS."
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="value in values"
          :key="value.title"
          class="text-center"
        >
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon :name="value.icon" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-3">{{ value.title }}</h3>
          <p class="text-sm text-muted-foreground">{{ value.description }}</p>
        </div>
      </div>
    </UPageSection>

    <!-- Leadership Team -->
    <UPageSection
      title="Leadership Team"
      description="Meet the experienced professionals leading AGL LOGISTICS into the future."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-2 gap-8">
        <div
          v-for="member in team"
          :key="member.name"
          class="group"
        >
          <UCard class="h-full hover:shadow-lg transition-shadow">
            <template #header>
              <div class="flex items-start gap-4">
                <div class="w-20 h-20 bg-gray-200 dark:bg-gray-700 rounded-full flex items-center justify-center flex-shrink-0">
                  <UIcon name="lucide:user" class="text-2xl text-muted-foreground" />
                </div>
                <div class="flex-1">
                  <h3 class="text-xl font-semibold mb-1">{{ member.name }}</h3>
                  <p class="text-primary font-medium mb-1">{{ member.position }}</p>
                  <p class="text-sm text-muted-foreground">{{ member.experience }}</p>
                </div>
              </div>
            </template>

            <div class="space-y-4">
              <p class="text-sm text-muted-foreground">{{ member.bio }}</p>

              <UButton
                :to="member.linkedin"
                target="_blank"
                variant="outline"
                size="sm"
                icon="i-simple-icons-linkedin"
              >
                Connect on LinkedIn
              </UButton>
            </div>
          </UCard>
        </div>
      </div>
    </UPageSection>

    <!-- Company Timeline -->
    <UPageSection
      title="Our Journey"
      description="Key milestones in the growth and development of AGL LOGISTICS."
    >
      <div class="relative">
        <!-- Timeline line -->
        <div class="absolute left-4 top-0 bottom-0 w-0.5 bg-gray-200 dark:bg-gray-700"></div>

        <div class="space-y-8">
          <div
            v-for="(milestone, index) in milestones"
            :key="milestone.year"
            class="relative pl-12"
          >
            <!-- Timeline dot -->
            <div class="absolute left-0 w-8 h-8 bg-primary rounded-full flex items-center justify-center text-white text-sm font-bold">
              {{ index + 1 }}
            </div>

            <div>
              <div class="flex items-center gap-3 mb-2">
                <span class="text-2xl font-bold text-primary">{{ milestone.year }}</span>
                <h3 class="text-xl font-semibold">{{ milestone.title }}</h3>
              </div>
              <p class="text-muted-foreground">{{ milestone.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- Certifications -->
    <UPageSection
      title="Certifications & Compliance"
      description="Our commitment to quality and compliance is recognized through industry certifications."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div
          v-for="cert in certifications"
          :key="cert.name"
          class="text-center p-6 bg-white dark:bg-gray-800 rounded-lg"
        >
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon :name="cert.icon" class="text-2xl text-primary" />
          </div>
          <h3 class="font-semibold mb-2">{{ cert.name }}</h3>
          <p class="text-sm text-muted-foreground">{{ cert.description }}</p>
        </div>
      </div>
    </UPageSection>

    <!-- Sustainability -->
    <UPageSection
      title="Sustainability Commitment"
      description="Building a greener future through responsible logistics practices."
      class="bg-gradient-to-br from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20 relative overflow-hidden"
    >
      <!-- Environmental Background -->
      <div class="absolute inset-0">
        <img
          src="/images/ep.png"
          alt="Environmental protection and sustainability"
          class="absolute inset-0 w-full h-full object-cover opacity-15"
        />
        <div class="absolute inset-0 bg-gradient-to-br from-green-50/90 to-blue-50/90 dark:from-green-900/90 dark:to-blue-900/90"></div>
      </div>

      <UContainer class="relative z-10">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div class="space-y-8">
            <div class="relative">
              <div class="flex items-center gap-3 mb-4">
                <UIcon name="lucide:earth" class="text-green-600 text-2xl" />
                <h3 class="text-2xl md:text-3xl font-black tracking-tight text-green-800 dark:text-green-200">Environmental Responsibility</h3>
              </div>
              <p class="text-base md:text-lg text-gray-700 dark:text-gray-300 leading-relaxed font-medium">
                We're committed to reducing our environmental impact through <span class="text-green-600 font-semibold">innovative green logistics solutions</span>, carbon-neutral shipping options, and sustainable warehouse operations.
              </p>
            </div>

            <div class="relative">
              <div class="flex items-center gap-3 mb-4">
                <UIcon name="lucide:leaf" class="text-green-600 text-2xl" />
                <h3 class="text-2xl md:text-3xl font-black tracking-tight text-green-800 dark:text-green-200">Green Initiatives</h3>
              </div>
              <ul class="space-y-3">
                <li class="flex items-center gap-3 p-3 bg-white/60 dark:bg-gray-800/60 rounded-lg backdrop-blur-sm">
                  <UIcon name="lucide:calculator" class="text-green-500 w-5 h-5 flex-shrink-0" />
                  <span class="text-gray-700 dark:text-gray-300 font-medium">Carbon footprint measurement and offset programs</span>
                </li>
                <li class="flex items-center gap-3 p-3 bg-white/60 dark:bg-gray-800/60 rounded-lg backdrop-blur-sm">
                  <UIcon name="lucide:zap" class="text-green-500 w-5 h-5 flex-shrink-0" />
                  <span class="text-gray-700 dark:text-gray-300 font-medium">Energy-efficient warehouse facilities</span>
                </li>
                <li class="flex items-center gap-3 p-3 bg-white/60 dark:bg-gray-800/60 rounded-lg backdrop-blur-sm">
                  <UIcon name="lucide:file-text" class="text-green-500 w-5 h-5 flex-shrink-0" />
                  <span class="text-gray-700 dark:text-gray-300 font-medium">Paperless documentation systems</span>
                </li>
                <li class="flex items-center gap-3 p-3 bg-white/60 dark:bg-gray-800/60 rounded-lg backdrop-blur-sm">
                  <UIcon name="lucide:route" class="text-green-500 w-5 h-5 flex-shrink-0" />
                  <span class="text-gray-700 dark:text-gray-300 font-medium">Route optimization to reduce emissions</span>
                </li>
                <li class="flex items-center gap-3 p-3 bg-white/60 dark:bg-gray-800/60 rounded-lg backdrop-blur-sm">
                  <UIcon name="lucide:handshake" class="text-green-500 w-5 h-5 flex-shrink-0" />
                  <span class="text-gray-700 dark:text-gray-300 font-medium">Partnership with eco-friendly transport providers</span>
                </li>
              </ul>
            </div>
          </div>

          <div class="relative">
            <div class="aspect-video rounded-2xl overflow-hidden shadow-2xl border border-green-200/50 dark:border-green-700/50">
              <img
                src="/images/ep.png"
                alt="Environmental protection initiatives"
                class="w-full h-full object-cover hover:scale-105 transition-transform duration-[10s]"
              />
              <!-- Green overlay -->
              <div class="absolute inset-0 bg-gradient-to-t from-green-900/30 to-transparent"></div>
            </div>

            <!-- Decorative elements -->
            <div class="absolute -top-4 -left-4 w-8 h-8 bg-green-500 rounded-full opacity-60 animate-pulse"></div>
            <div class="absolute -bottom-4 -right-4 w-6 h-6 bg-blue-500 rounded-full opacity-40 animate-pulse animation-delay-1000"></div>

            <!-- Floating badge -->
            <div class="absolute top-4 right-4 bg-green-600 text-white px-3 py-1 rounded-full text-sm font-bold">
              ECO-FRIENDLY
            </div>
          </div>
        </div>
      </UContainer>
    </UPageSection>

    <!-- CTA -->
    <UPageCTA
      title="Ready to work with Australia's logistics leaders?"
      description="Join thousands of satisfied customers who trust AGL LOGISTICS for their freight forwarding needs. Experience the difference that 20 years of expertise makes."
      :links="[
        {
          label: 'Get Started Today',
          to: '/contact',
          color: 'primary'
        },
        {
          label: 'View Our Services',
          to: '/services/air-freight',
          variant: 'outline'
        }
      ]"
    />
  </div>
</template>

<style scoped>
.animation-delay-1000 {
  animation-delay: 1s;
}
</style>
