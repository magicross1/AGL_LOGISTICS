<script setup lang="ts">
useSeoMeta({
  title: 'Careers - Join AGL LOGISTICS Team',
  description: 'Join AGL LOGISTICS and build your career in the logistics industry. Explore opportunities in freight forwarding, customs, operations, and more.',
})

const jobOpenings = [
  {
    id: 1,
    title: 'Senior Freight Forwarding Specialist',
    department: 'Operations',
    location: 'Sydney, NSW',
    type: 'Full-time',
    experience: '3-5 years',
    description: 'Lead freight forwarding operations for air and sea cargo, manage customer relationships, and coordinate with international partners.',
    requirements: [
      'Bachelor\'s degree in Logistics, Supply Chain, or related field',
      '3+ years experience in freight forwarding',
      'Knowledge of INCOTERMS and international trade regulations',
      'Strong communication and problem-solving skills',
      'Proficiency in logistics software systems'
    ],
    benefits: [
      'Competitive salary package',
      'Health and dental insurance',
      'Professional development opportunities',
      'Flexible working arrangements'
    ]
  },
  {
    id: 2,
    title: 'Customs Brokerage Officer',
    department: 'Customs & Compliance',
    location: 'Melbourne, VIC',
    type: 'Full-time',
    experience: '2-4 years',
    description: 'Handle customs clearance processes, prepare documentation, and ensure compliance with Australian customs regulations.',
    requirements: [
      'Licensed Customs Broker or working towards license',
      '2+ years experience in customs brokerage',
      'Knowledge of Australian customs procedures',
      'Attention to detail and accuracy',
      'Ability to work under pressure'
    ],
    benefits: [
      'Competitive salary package',
      'Health and dental insurance',
      'Training and certification support',
      'Career progression opportunities'
    ]
  },
  {
    id: 3,
    title: 'Warehouse Operations Manager',
    department: 'Warehousing',
    location: 'Brisbane, QLD',
    type: 'Full-time',
    experience: '5+ years',
    description: 'Oversee warehouse operations, manage inventory systems, and lead a team of warehouse staff.',
    requirements: [
      'Bachelor\'s degree in Logistics or Business Management',
      '5+ years warehouse management experience',
      'Experience with WMS systems',
      'Strong leadership and team management skills',
      'Knowledge of OH&S regulations'
    ],
    benefits: [
      'Management level salary package',
      'Health and dental insurance',
      'Performance bonuses',
      'Company vehicle'
    ]
  },
  {
    id: 4,
    title: 'Graduate Logistics Trainee',
    department: 'Various',
    location: 'Multiple locations',
    type: 'Graduate Program',
    experience: 'Entry level',
    description: 'Join our 12-month graduate program and rotate through different departments to build comprehensive logistics expertise.',
    requirements: [
      'Recent graduate in Logistics, Supply Chain, Business, or related field',
      'Strong academic record',
      'Excellent communication skills',
      'Willingness to learn and adapt',
      'Interest in logistics and international trade'
    ],
    benefits: [
      'Structured learning program',
      'Mentorship opportunities',
      'Health and dental insurance',
      'Clear career pathway'
    ]
  }
]

const benefits = [
  {
    title: 'Competitive Compensation',
    description: 'Market-leading salaries with performance-based bonuses and regular reviews.',
    icon: 'lucide:dollar-sign'
  },
  {
    title: 'Health & Wellness',
    description: 'Comprehensive health insurance, dental coverage, and wellness programs.',
    icon: 'lucide:heart'
  },
  {
    title: 'Professional Development',
    description: 'Training programs, certifications, and career advancement opportunities.',
    icon: 'lucide:graduation-cap'
  },
  {
    title: 'Work-Life Balance',
    description: 'Flexible working arrangements and generous leave policies.',
    icon: 'lucide:balance-scale'
  },
  {
    title: 'Team Culture',
    description: 'Collaborative environment with team events and recognition programs.',
    icon: 'lucide:users'
  },
  {
    title: 'Innovation Focus',
    description: 'Work with cutting-edge logistics technology and contribute to industry innovation.',
    icon: 'lucide:lightbulb'
  }
]

const values = [
  {
    title: 'Excellence',
    description: 'We strive for excellence in everything we do, from customer service to operational efficiency.'
  },
  {
    title: 'Innovation',
    description: 'We embrace new technologies and creative solutions to solve logistics challenges.'
  },
  {
    title: 'Collaboration',
    description: 'We work together as one team, supporting each other to achieve common goals.'
  },
  {
    title: 'Integrity',
    description: 'We conduct business with honesty, transparency, and ethical practices.'
  }
]
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Join Our Team"
      description="Build your career with Australia's leading logistics company. Discover opportunities to grow, innovate, and make a real impact in the freight forwarding industry."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Careers Video Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <video
            autoplay
            muted
            loop
            playsinline
            class="absolute inset-0 w-full h-full object-cover"
          >
            <source src="/videos/careers.mp4" type="video/mp4">
          </video>
          <!-- Dark overlay for better text readability -->
          <div class="absolute inset-0 bg-black/40"></div>
        </div>
      </template>

      <template #title>
        <h1 class="text-white drop-shadow-lg">Join Our Team</h1>
      </template>

      <template #links>
        <UButton
          label="View Open Positions"
          icon="lucide:arrow-right"
          trailing
          color="primary"
          to="#jobs"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="Submit Resume"
          icon="lucide:upload"
          size="xl"
          color="white"
          variant="outline"
          to="#apply"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Why Join Us -->
    <UPageSection
      title="Why Choose AGL LOGISTICS"
      description="Join a company that values your growth, innovation, and contribution to the logistics industry."
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="benefit in benefits"
          :key="benefit.title"
          class="text-center"
        >
          <div class="w-16 h-16 mx-auto mb-4 bg-primary/10 rounded-full flex items-center justify-center">
            <UIcon :name="benefit.icon" class="text-2xl text-primary" />
          </div>
          <h3 class="text-lg font-semibold mb-3">{{ benefit.title }}</h3>
          <p class="text-sm text-muted-foreground">{{ benefit.description }}</p>
        </div>
      </div>
    </UPageSection>

    <!-- Our Values -->
    <UPageSection
      title="Our Values"
      description="The principles that guide our work culture and define what it means to be part of the AGL LOGISTICS family."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-2 gap-8">
        <div
          v-for="value in values"
          :key="value.title"
          class="p-6 bg-white dark:bg-gray-800 rounded-lg"
        >
          <h3 class="text-xl font-semibold mb-3 text-primary">{{ value.title }}</h3>
          <p class="text-muted-foreground">{{ value.description }}</p>
        </div>
      </div>
    </UPageSection>

    <!-- Current Openings -->
    <UPageSection
      id="jobs"
      title="Current Openings"
      description="Explore our current job opportunities and find the perfect role to advance your logistics career."
    >
      <div class="space-y-6">
        <div
          v-for="job in jobOpenings"
          :key="job.id"
          class="group"
        >
          <UCard class="hover:shadow-lg transition-shadow">
            <template #header>
              <div class="flex items-start justify-between">
                <div class="flex-1">
                  <h3 class="text-xl font-semibold mb-2">{{ job.title }}</h3>
                  <div class="flex items-center gap-4 text-sm text-muted-foreground">
                    <div class="flex items-center gap-1">
                      <UIcon name="lucide:building" />
                      <span>{{ job.department }}</span>
                    </div>
                    <div class="flex items-center gap-1">
                      <UIcon name="lucide:map-pin" />
                      <span>{{ job.location }}</span>
                    </div>
                    <div class="flex items-center gap-1">
                      <UIcon name="lucide:clock" />
                      <span>{{ job.type }}</span>
                    </div>
                    <div class="flex items-center gap-1">
                      <UIcon name="lucide:briefcase" />
                      <span>{{ job.experience }}</span>
                    </div>
                  </div>
                </div>
                <UButton 
                  size="sm" 
                  color="primary"
                  :to="`mailto:ops@agllogistics.com.au?subject=Job Application - ${job.title}&body=Dear AGL LOGISTICS Hiring Team,%0D%0A%0D%0AI am writing to express my interest in the ${job.title} position in your ${job.department} department located in ${job.location}.%0D%0A%0D%0APosition Details:%0D%0A- Job Title: ${job.title}%0D%0A- Department: ${job.department}%0D%0A- Location: ${job.location}%0D%0A- Employment Type: ${job.type}%0D%0A%0D%0APlease find my resume and cover letter attached. I would welcome the opportunity to discuss how my experience and skills align with your requirements.%0D%0A%0D%0AThank you for your consideration.%0D%0A%0D%0ABest regards,%0D%0A[Your Name]%0D%0A[Your Phone Number]%0D%0A[Your Email Address]`"
                >
                  <UIcon name="lucide:mail" class="mr-2" />
                  Apply Now
                </UButton>
              </div>
            </template>
            
            <div class="space-y-6">
              <div>
                <h4 class="font-semibold mb-2">Role Description</h4>
                <p class="text-muted-foreground">{{ job.description }}</p>
              </div>
              
              <div>
                <h4 class="font-semibold mb-2">Requirements</h4>
                <ul class="space-y-1">
                  <li
                    v-for="requirement in job.requirements"
                    :key="requirement"
                    class="text-sm text-muted-foreground flex items-start gap-2"
                  >
                    <UIcon name="lucide:check" class="text-green-500 mt-0.5 flex-shrink-0" />
                    <span>{{ requirement }}</span>
                  </li>
                </ul>
              </div>
              
              <div>
                <h4 class="font-semibold mb-2">Benefits</h4>
                <ul class="space-y-1">
                  <li
                    v-for="benefit in job.benefits"
                    :key="benefit"
                    class="text-sm text-muted-foreground flex items-start gap-2"
                  >
                    <UIcon name="lucide:star" class="text-primary mt-0.5 flex-shrink-0" />
                    <span>{{ benefit }}</span>
                  </li>
                </ul>
              </div>
            </div>
          </UCard>
        </div>
      </div>
    </UPageSection>

    <!-- Application Process -->
    <UPageSection
      title="Application Process"
      description="Our streamlined hiring process designed to find the best talent for our team."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-4 gap-8">
        <div class="text-center">
          <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
            1
          </div>
          <h3 class="font-semibold mb-2">Apply Online</h3>
          <p class="text-sm text-muted-foreground">Submit your application and resume through our online portal.</p>
        </div>
        <div class="text-center">
          <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
            2
          </div>
          <h3 class="font-semibold mb-2">Initial Review</h3>
          <p class="text-sm text-muted-foreground">Our HR team reviews your application and qualifications.</p>
        </div>
        <div class="text-center">
          <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
            3
          </div>
          <h3 class="font-semibold mb-2">Interview</h3>
          <p class="text-sm text-muted-foreground">Meet with our hiring managers and team members.</p>
        </div>
        <div class="text-center">
          <div class="w-12 h-12 mx-auto mb-4 bg-primary rounded-full flex items-center justify-center text-white font-bold">
            4
          </div>
          <h3 class="font-semibold mb-2">Welcome Aboard</h3>
          <p class="text-sm text-muted-foreground">Join our team and start your logistics career journey.</p>
        </div>
      </div>
    </UPageSection>

    <!-- General Application -->
    <UPageSection
      id="apply"
      class="bg-gradient-to-br from-gray-50 to-blue-50 dark:from-gray-900 dark:to-blue-900/20 relative overflow-hidden"
    >
      <!-- Background Effects -->
      <div class="absolute inset-0">
        <div class="absolute top-20 left-10 w-72 h-72 bg-primary/5 rounded-full blur-3xl animate-pulse"></div>
        <div class="absolute bottom-20 right-10 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl animate-pulse animation-delay-2000"></div>
      </div>

      <UContainer class="relative z-10">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-black text-gray-900 dark:text-white mb-6 leading-tight tracking-tight">
            Don't See the <span class="bg-gradient-to-r from-purple-500 to-pink-500 bg-clip-text text-transparent">Right Role</span>?
          </h2>
          <p class="text-xl md:text-2xl text-gray-600 dark:text-gray-300 max-w-4xl mx-auto leading-relaxed font-medium">
            We're always looking for <span class="text-primary font-semibold">talented individuals</span>. Send us your resume for future opportunities.
          </p>
        </div>

        <div class="max-w-4xl mx-auto">
          <div class="grid md:grid-cols-2 gap-8">
            <!-- General Application -->
            <UCard class="group hover:shadow-2xl transition-all duration-500 hover:-translate-y-2 bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm">
              <template #header>
                <div class="text-center">
                  <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:bg-primary group-hover:text-white transition-all duration-300">
                    <UIcon name="lucide:mail" class="text-3xl text-primary group-hover:text-white" />
                  </div>
                  <h3 class="text-xl md:text-2xl font-black tracking-tight mb-2">Submit General Application</h3>
                  <p class="text-sm md:text-base text-gray-600 dark:text-gray-400 font-medium">Join our talent pool for future opportunities</p>
                </div>
              </template>

              <div class="space-y-6 text-center">
                <div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-xl">
                  <h4 class="font-bold mb-3">What to Include in Your Email:</h4>
                  <div class="space-y-2 text-sm text-left">
                    <div class="flex items-center gap-2">
                      <UIcon name="lucide:check" class="text-green-500 w-4 h-4" />
                      <span>Your current resume/CV (PDF preferred)</span>
                    </div>
                    <div class="flex items-center gap-2">
                      <UIcon name="lucide:check" class="text-green-500 w-4 h-4" />
                      <span>Brief cover letter or introduction</span>
                    </div>
                    <div class="flex items-center gap-2">
                      <UIcon name="lucide:check" class="text-green-500 w-4 h-4" />
                      <span>Areas of interest and expertise</span>
                    </div>
                    <div class="flex items-center gap-2">
                      <UIcon name="lucide:check" class="text-green-500 w-4 h-4" />
                      <span>Preferred location (Sydney/Melbourne/Brisbane)</span>
                    </div>
                  </div>
                </div>

                <UButton 
                  size="lg" 
                  block
                  color="primary"
                  to="mailto:ops@agllogistics.com.au?subject=General Job Application - Future Opportunities&body=Dear AGL LOGISTICS Hiring Team,%0D%0A%0D%0AI am interested in joining your team and would like to be considered for future opportunities that match my skills and experience.%0D%0A%0D%0APersonal Information:%0D%0A- Name: [Your Full Name]%0D%0A- Phone: [Your Phone Number]%0D%0A- Email: [Your Email Address]%0D%0A- Location: [Your Current Location]%0D%0A%0D%0ACareer Interests:%0D%0A- Preferred Department: [Operations/Customs/Warehouse/Customer Service/Sales/IT/Finance/Management]%0D%0A- Experience Level: [Entry/Junior/Mid-Level/Senior/Executive]%0D%0A- Preferred Location: [Sydney/Melbourne/Brisbane/Perth]%0D%0A- Available Start Date: [Date]%0D%0A%0D%0AKey Skills and Experience:%0D%0A[Please describe your relevant experience, skills, and qualifications]%0D%0A%0D%0AWhy AGL LOGISTICS:%0D%0A[Tell us why you're interested in joining our team]%0D%0A%0D%0APlease find my resume attached.%0D%0A%0D%0AThank you for considering my application. I look forward to hearing about future opportunities.%0D%0A%0D%0ABest regards,%0D%0A[Your Name]"
                  class="font-semibold text-lg"
                >
                  <UIcon name="lucide:mail" class="mr-2" />
                  Send Resume via Email
                </UButton>
                
                <p class="text-xs text-gray-500">
                  This will open your email client with a pre-written template. 
                  Don't forget to attach your resume!
                </p>
              </div>
            </UCard>

            <!-- Alternative Contact Methods -->
            <UCard class="group hover:shadow-2xl transition-all duration-500 hover:-translate-y-2 bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm">
              <template #header>
                <div class="text-center">
                  <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:bg-green-600 group-hover:text-white transition-all duration-300">
                    <UIcon name="lucide:message-square" class="text-3xl text-green-600 group-hover:text-white" />
                  </div>
                  <h3 class="text-xl md:text-2xl font-black tracking-tight mb-2">Quick Contact Options</h3>
                  <p class="text-sm md:text-base text-gray-600 dark:text-gray-400 font-medium">Alternative ways to connect with our HR team</p>
                </div>
              </template>

              <div class="space-y-4">
                <!-- WhatsApp -->
                <div class="bg-green-50 dark:bg-green-900/20 p-4 rounded-xl border border-green-200/50 dark:border-green-700/50">
                  <div class="flex items-center gap-3 mb-3">
                    <UIcon name="lucide:message-square" class="text-green-600 text-xl" />
                    <h4 class="font-bold">WhatsApp Business</h4>
                  </div>
                  <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">Quick inquiries about career opportunities</p>
                  <UButton 
                    to="https://wa.me/61287473069?text=Hi%20AGL%20LOGISTICS,%20I'm%20interested%20in%20career%20opportunities%20with%20your%20company.%20Could%20you%20please%20provide%20information%20about%20current%20or%20future%20openings?"
                    target="_blank"
                    color="green"
                    size="sm"
                    block
                    class="font-semibold"
                  >
                    <UIcon name="lucide:message-square" class="mr-2" />
                    Chat on WhatsApp
                  </UButton>
                </div>

                <!-- Phone -->
                <div class="bg-blue-50 dark:bg-blue-900/20 p-4 rounded-xl border border-blue-200/50 dark:border-blue-700/50">
                  <div class="flex items-center gap-3 mb-3">
                    <UIcon name="lucide:phone" class="text-blue-600 text-xl" />
                    <h4 class="font-bold">Direct Phone Line</h4>
                  </div>
                  <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">Speak directly with our HR team</p>
                  <div class="space-y-2">
                    <p class="font-mono text-sm font-bold text-center">+61 2 8747 3069</p>
                    <UButton 
                      to="tel:+61-2-8747-3069"
                      color="blue"
                      size="sm"
                      block
                      class="font-semibold"
                    >
                      <UIcon name="lucide:phone" class="mr-2" />
                      Call HR Department
                    </UButton>
                  </div>
                </div>

                <!-- LinkedIn -->
                <div class="bg-primary/5 p-4 rounded-xl border border-primary/20">
                  <div class="flex items-center gap-3 mb-3">
                    <UIcon name="i-simple-icons-linkedin" class="text-primary text-xl" />
                    <h4 class="font-bold">LinkedIn</h4>
                  </div>
                  <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">Connect with us professionally</p>
                  <UButton 
                    to="https://linkedin.com/company/agl-logistics"
                    target="_blank"
                    color="primary"
                    size="sm"
                    block
                    variant="outline"
                    class="font-semibold"
                  >
                    <UIcon name="i-simple-icons-linkedin" class="mr-2" />
                    Follow on LinkedIn
                  </UButton>
                </div>
              </div>
            </UCard>
          </div>
        </div>
      </UContainer>
    </UPageSection>

    <!-- Contact CTA -->
    <UPageCTA
      title="Questions about careers at AGL LOGISTICS?"
      description="Our HR team is here to help you understand opportunities and answer any questions about working with us."
      :links="[
        {
          label: 'Contact HR Team',
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
