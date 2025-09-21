<script setup lang="ts">
interface EmailTemplate {
  id: string
  name: string
  subject: string
  body: string
  category: string
  icon: string
  description: string
}

interface Props {
  onSelectTemplate?: (template: EmailTemplate) => void
}

const props = defineProps<Props>()

const templates = ref<EmailTemplate[]>([
  {
    id: 'newsletter-subscription',
    name: 'Newsletter Subscription',
    subject: 'Newsletter Subscription Request - [Your Company Name]',
    body: `Dear AGL LOGISTICS Team,

I would like to subscribe to your newsletter to stay updated with the latest news and service announcements.

**Subscription Details:**
- Company Name: [Your Company]
- Contact Person: [Your Name]
- Email: [Your Email Address]
- Phone: [Your Phone Number]

**Interests (please specify):**
- [ ] General news and company updates
- [ ] Service disruption alerts and notifications
- [ ] New service announcements and route updates
- [ ] Industry insights and logistics trends
- [ ] Special offers and promotions

**Additional Information:**
- Industry/Business Type: [Your Industry]
- Preferred Communication Frequency: [Weekly/Monthly/As needed]

Please add me to your mailing list and confirm my subscription.

Thank you for keeping us informed about your services and industry developments.

Best regards,
[Your Name]
[Your Position]
[Your Company]
[Your Contact Details]`,
    category: 'newsletter',
    icon: 'lucide:mail',
    description: 'Subscribe to AGL LOGISTICS newsletter and updates'
  },
  {
    id: 'service-alert-subscription',
    name: 'Service Alert Subscription',
    subject: 'Service Alert Subscription - [Your Routes/Services]',
    body: `Dear AGL LOGISTICS Operations Team,

I would like to subscribe to service alerts and notifications for specific routes and services that are critical to our business operations.

**Alert Subscription Details:**
- Company Name: [Your Company]
- Contact Person: [Your Name]
- Email: [Your Email]
- Phone/SMS: [Your Phone] (for urgent alerts)

**Routes/Services of Interest:**
- [ ] Sydney - Melbourne route
- [ ] Sydney - Brisbane route
- [ ] Melbourne - Brisbane route
- [ ] Air freight services
- [ ] Sea freight services
- [ ] Customs clearance updates
- [ ] Port congestion notices
- [ ] Holiday schedule changes

**Notification Preferences:**
- [ ] Email notifications
- [ ] SMS alerts for urgent disruptions
- [ ] WhatsApp updates
- [ ] Phone calls for critical issues

**Business Impact Information:**
- Peak shipping periods: [Specify months/seasons]
- Critical delivery requirements: [Time-sensitive cargo details]

Please ensure we receive timely notifications about any service disruptions or changes that may affect our shipments.

Thank you for your proactive communication.

Best regards,
[Your Name]
[Your Company]
[Your Contact Information]`,
    category: 'alerts',
    icon: 'lucide:bell',
    description: 'Subscribe to service alerts and disruption notifications'
  },
  {
    id: 'industry-insights-request',
    name: 'Industry Insights Request',
    subject: 'Industry Insights and Market Updates Subscription',
    body: `Dear AGL LOGISTICS Business Intelligence Team,

I am interested in receiving industry insights and market updates to help inform our business decisions and logistics planning.

**Company Information:**
- Company Name: [Your Company]
- Industry: [Your Industry Sector]
- Contact Person: [Your Name]
- Email: [Your Email]

**Areas of Interest:**
- [ ] Australian logistics market trends
- [ ] International trade developments
- [ ] Freight rate fluctuations
- [ ] Regulatory changes and compliance updates
- [ ] Technology advancements in logistics
- [ ] Sustainability and environmental initiatives
- [ ] Economic factors affecting logistics

**Specific Interests:**
- Business Focus: [Import/Export/Domestic/All]
- Key Markets: [Countries/regions you trade with]
- Cargo Types: [General/Specialized cargo types]

**Preferred Format:**
- [ ] Monthly industry report
- [ ] Quarterly market analysis
- [ ] Weekly brief updates
- [ ] Special event notifications

Please include me in your industry insights distribution list.

Thank you for sharing your expertise and market knowledge.

Best regards,
[Your Name]
[Your Position]
[Your Company]
[Your Contact Details]`,
    category: 'insights',
    icon: 'lucide:trending-up',
    description: 'Request industry insights and market intelligence updates'
  },
  {
    id: 'unsubscribe-request',
    name: 'Unsubscribe Request',
    subject: 'Unsubscribe Request - [Your Email Address]',
    body: `Dear AGL LOGISTICS Team,

I would like to unsubscribe from your mailing list and newsletter.

**Unsubscribe Details:**
- Email to remove: [Your Email Address]
- Company Name: [Your Company]
- Contact Person: [Your Name]

**Reason for Unsubscribing (optional):**
- [ ] No longer need the service
- [ ] Too frequent communications
- [ ] Content not relevant to our business
- [ ] Changed email address (please specify new one below)
- [ ] Other: [Please specify]

**New Email Address (if applicable):**
[New email if you want to resubscribe with different address]

Please confirm the removal of my email address from all mailing lists and ensure no further communications are sent.

If you need to send any final confirmation, please do so within 7 days.

Thank you for your cooperation.

Best regards,
[Your Name]
[Your Company]`,
    category: 'unsubscribe',
    icon: 'lucide:user-x',
    description: 'Unsubscribe from newsletters and communications'
  }
])

const selectedCategory = ref('all')
const searchQuery = ref('')

const categories = computed(() => [
  { value: 'all', label: 'All Templates', icon: 'lucide:grid-3x3' },
  { value: 'newsletter', label: 'Newsletter', icon: 'lucide:mail' },
  { value: 'alerts', label: 'Service Alerts', icon: 'lucide:bell' },
  { value: 'insights', label: 'Industry Insights', icon: 'lucide:trending-up' },
  { value: 'unsubscribe', label: 'Unsubscribe', icon: 'lucide:user-x' }
])

const filteredTemplates = computed(() => {
  let filtered = templates.value
  
  if (selectedCategory.value !== 'all') {
    filtered = filtered.filter(template => template.category === selectedCategory.value)
  }
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(template => 
      template.name.toLowerCase().includes(query) ||
      template.description.toLowerCase().includes(query) ||
      template.subject.toLowerCase().includes(query)
    )
  }
  
  return filtered
})

function selectTemplate(template: EmailTemplate) {
  // Create mailto link with pre-filled content
  const emailBody = encodeURIComponent(template.body)
  const emailSubject = encodeURIComponent(template.subject)
  const mailtoLink = `mailto:ops@agllogistics.com.au?subject=${emailSubject}&body=${emailBody}`
  
  // Open email client
  window.location.href = mailtoLink
  
  if (props.onSelectTemplate) {
    props.onSelectTemplate(template)
  }
}

function copyToClipboard(template: EmailTemplate) {
  const fullEmailText = `To: ops@agllogistics.com.au
Subject: ${template.subject}

${template.body}`
  
  navigator.clipboard.writeText(fullEmailText)
  
  // Show success notification (if toast is available in the parent)
  if (typeof useToast === 'function') {
    const toast = useToast()
    toast.add({
      title: 'Email Template Copied!',
      description: `${template.name} template copied to clipboard with recipient address.`,
      color: 'green'
    })
  }
}
</script>

<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="text-center">
      <h3 class="text-2xl md:text-3xl font-black mb-3 tracking-tight">Email Templates</h3>
      <p class="text-base md:text-lg text-gray-600 dark:text-gray-400 font-medium leading-relaxed">
        Use our <span class="text-primary font-semibold">pre-written templates</span> to quickly compose emails for newsletter subscriptions and service center inquiries
      </p>
    </div>

    <!-- Search and Filter -->
    <div class="flex flex-col md:flex-row gap-4">
      <div class="flex-1">
        <UInput
          v-model="searchQuery"
          placeholder="Search templates..."
          icon="lucide:search"
          size="lg"
        />
      </div>
      <div class="md:w-48">
        <USelect
          v-model="selectedCategory"
          :options="categories"
          size="lg"
          placeholder="Category"
        />
      </div>
    </div>

    <!-- Templates Grid -->
    <div class="grid md:grid-cols-2 gap-6">
      <UCard
        v-for="template in filteredTemplates"
        :key="template.id"
        class="group cursor-pointer hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
        @click="selectTemplate(template)"
      >
        <template #header>
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-primary/10 rounded-lg flex items-center justify-center">
              <UIcon :name="template.icon" class="text-primary text-xl" />
            </div>
            <div class="flex-1">
              <h4 class="font-black text-base md:text-lg tracking-tight">{{ template.name }}</h4>
              <p class="text-sm text-gray-500 capitalize font-medium">{{ template.category }}</p>
            </div>
          </div>
        </template>

        <div class="space-y-4">
          <p class="text-sm md:text-base text-gray-600 dark:text-gray-400 line-clamp-2 font-medium leading-relaxed">
            {{ template.description }}
          </p>
          
          <div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-xl border border-gray-200/50 dark:border-gray-700/50">
            <p class="text-xs md:text-sm font-bold text-gray-500 mb-2 uppercase tracking-wider">Subject:</p>
            <p class="text-sm md:text-base font-bold line-clamp-1 text-gray-900 dark:text-gray-100">{{ template.subject }}</p>
          </div>

          <div class="flex gap-2">
            <UButton
              size="sm"
              variant="outline"
              block
              @click.stop="selectTemplate(template)"
              class="font-semibold"
            >
              <UIcon name="lucide:mail" class="mr-2" />
              Open in Email
            </UButton>
            <UButton
              size="sm"
              variant="ghost"
              @click.stop="copyToClipboard(template)"
              class="font-semibold"
              title="Copy email template with recipient address"
            >
              <UIcon name="lucide:copy" />
            </UButton>
          </div>
        </div>
      </UCard>
    </div>

    <!-- No Results -->
    <div v-if="filteredTemplates.length === 0" class="text-center py-12">
      <UIcon name="lucide:search-x" class="text-4xl text-gray-400 mb-4" />
      <h4 class="text-xl md:text-2xl font-black text-gray-600 dark:text-gray-400 mb-3 tracking-tight">No templates found</h4>
      <p class="text-base md:text-lg text-gray-500 font-medium">Try adjusting your search or filter criteria</p>
    </div>
  </div>
</template>
