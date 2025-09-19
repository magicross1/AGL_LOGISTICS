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
    id: 'quote-request',
    name: 'Quote Request',
    subject: 'Freight Quote Request - [Your Company Name]',
    body: `Dear AGL LOGISTICS Team,

I hope this email finds you well. I am writing to request a quote for freight forwarding services.

**Shipment Details:**
- Origin: [City, Country]
- Destination: [City, Country]
- Cargo Type: [Description]
- Weight: [kg]
- Dimensions: [L x W x H cm]
- Value: [Currency Amount]
- Preferred Service: [Air Freight/Sea Freight/Special Transport]
- Required Delivery Date: [Date]

**Additional Requirements:**
- [ ] Customs clearance required
- [ ] Insurance coverage needed
- [ ] Door-to-door delivery
- [ ] Special handling requirements

**Company Information:**
- Company Name: [Your Company]
- Contact Person: [Your Name]
- Phone: [Your Phone]
- Email: [Your Email]

Please provide a detailed quote including all applicable charges and estimated transit times.

Thank you for your time and I look forward to your response.

Best regards,
[Your Name]
[Your Position]
[Your Company]`,
    category: 'quotes',
    icon: 'lucide:calculator',
    description: 'Request freight forwarding quotes with detailed specifications'
  },
  {
    id: 'shipment-tracking',
    name: 'Shipment Tracking Inquiry',
    subject: 'Tracking Request - Reference: [Your Reference Number]',
    body: `Dear AGL LOGISTICS Team,

I would like to inquire about the status of my shipment.

**Shipment Information:**
- Reference Number: [Your Reference]
- Booking Number: [If available]
- Date Shipped: [Date]
- Origin: [City, Country]
- Destination: [City, Country]

**Inquiry:**
Could you please provide an update on the current status and expected delivery date?

If there are any delays or issues, please let me know so I can inform my customers accordingly.

Thank you for your assistance.

Best regards,
[Your Name]
[Your Company]
[Your Phone]`,
    category: 'tracking',
    icon: 'lucide:map-pin',
    description: 'Track existing shipments and get status updates'
  },
  {
    id: 'customs-inquiry',
    name: 'Customs & Documentation',
    subject: 'Customs Clearance Inquiry - [Product/Shipment Type]',
    body: `Dear Customs Team,

I need assistance with customs clearance and documentation requirements.

**Product/Shipment Details:**
- Product Description: [Detailed description]
- HS Code: [If known]
- Country of Origin: [Country]
- Destination: [Australian city/state]
- Commercial Value: [Amount]
- Quantity: [Number of units]

**Specific Questions:**
- What documents are required for clearance?
- Are there any special permits needed?
- What are the applicable duties and taxes?
- Estimated clearance timeframe?

**Additional Information:**
- Importer Details: [Company name and ABN]
- Preferred Port of Entry: [Port name]
- Urgency Level: [Normal/Urgent]

Please advise on the complete process and requirements.

Thank you for your expertise.

Best regards,
[Your Name]
[Your Company]
[Your Contact Details]`,
    category: 'customs',
    icon: 'lucide:clipboard-check',
    description: 'Get help with customs procedures and documentation'
  },
  {
    id: 'warehouse-inquiry',
    name: 'Storage & Warehousing',
    subject: 'Warehouse Services Inquiry - [Storage Requirements]',
    body: `Dear Warehousing Team,

I am interested in your storage and warehousing services.

**Storage Requirements:**
- Product Type: [Description]
- Storage Duration: [Short-term/Long-term/Specific dates]
- Quantity: [Volume/pallets/containers]
- Special Requirements: [Temperature control/Security/Handling]
- Location Preference: [Sydney/Melbourne/Brisbane]

**Services Needed:**
- [ ] Receiving and inspection
- [ ] Inventory management
- [ ] Pick and pack services
- [ ] Distribution services
- [ ] Cross-docking
- [ ] Value-added services

**Additional Information:**
- Expected start date: [Date]
- Budget considerations: [If any]
- Integration requirements: [WMS/EDI systems]

Could you please provide information on availability, pricing, and service capabilities?

Thank you for your time.

Best regards,
[Your Name]
[Your Company]
[Your Contact Information]`,
    category: 'warehouse',
    icon: 'lucide:warehouse',
    description: 'Inquire about storage and distribution services'
  },
  {
    id: 'partnership',
    name: 'Partnership Opportunity',
    subject: 'Partnership Opportunity - [Your Company Name]',
    body: `Dear AGL LOGISTICS Business Development Team,

I hope this message finds you well. I am reaching out to explore potential partnership opportunities between our companies.

**Our Company:**
- Company Name: [Your Company]
- Industry: [Your Industry]
- Location: [Your Location]
- Website: [Your Website]

**Partnership Interest:**
- Type of Partnership: [Agent/Supplier/Joint Venture/Other]
- Geographic Focus: [Regions/Countries]
- Service Areas: [Specific logistics services]
- Expected Volume: [Annual shipments/revenue]

**Our Value Proposition:**
[Describe what you bring to the partnership]

**Next Steps:**
I would welcome the opportunity to discuss this further. Would you be available for a call or meeting in the coming weeks?

Thank you for considering this opportunity.

Best regards,
[Your Name]
[Your Position]
[Your Company]
[Your Contact Details]`,
    category: 'business',
    icon: 'lucide:handshake',
    description: 'Explore business partnership opportunities'
  },
  {
    id: 'complaint',
    name: 'Service Complaint',
    subject: 'Service Complaint - Reference: [Your Reference]',
    body: `Dear Customer Service Team,

I am writing to formally report an issue with a recent service experience.

**Shipment/Service Details:**
- Reference Number: [Your Reference]
- Service Date: [Date]
- Service Type: [Air/Sea/Customs/Storage]
- Origin: [Location]
- Destination: [Location]

**Issue Description:**
[Detailed description of the problem]

**Impact:**
[How this affected your business/customers]

**Resolution Sought:**
[What outcome you're looking for]

**Supporting Documentation:**
[List any attached documents/photos]

I trust that AGL LOGISTICS will investigate this matter promptly and provide a satisfactory resolution.

Please confirm receipt of this complaint and provide an expected timeframe for resolution.

Thank you for your attention to this matter.

Regards,
[Your Name]
[Your Company]
[Your Contact Information]`,
    category: 'support',
    icon: 'lucide:alert-triangle',
    description: 'Report service issues and seek resolution'
  }
])

const selectedCategory = ref('all')
const searchQuery = ref('')

const categories = computed(() => [
  { value: 'all', label: 'All Templates', icon: 'lucide:grid-3x3' },
  { value: 'quotes', label: 'Quotes', icon: 'lucide:calculator' },
  { value: 'tracking', label: 'Tracking', icon: 'lucide:map-pin' },
  { value: 'customs', label: 'Customs', icon: 'lucide:clipboard-check' },
  { value: 'warehouse', label: 'Warehouse', icon: 'lucide:warehouse' },
  { value: 'business', label: 'Business', icon: 'lucide:handshake' },
  { value: 'support', label: 'Support', icon: 'lucide:alert-triangle' }
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
        Choose from our pre-written templates to quickly compose <span class="text-primary font-semibold">professional emails</span>
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
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
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
