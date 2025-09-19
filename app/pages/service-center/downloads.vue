<script setup lang="ts">
useSeoMeta({
  title: 'Downloads & Resources - AGL LOGISTICS',
  description: 'Access essential forms, guides, rate sheets, and documentation for your logistics needs from AGL LOGISTICS.',
})

// Mock downloads data
const downloads = [
  {
    id: 1,
    title: 'Air Freight Booking Form',
    description: 'Complete air freight booking form with all required fields for international and domestic shipments.',
    category: 'Forms',
    fileType: 'PDF',
    fileSize: '245 KB',
    lastUpdated: '2024-12-01',
    downloadCount: 1250,
    featured: true
  },
  {
    id: 2,
    title: 'Sea Freight Rate Guide 2024',
    description: 'Comprehensive rate guide for sea freight services including FCL and LCL rates to major destinations.',
    category: 'Rate Guides',
    fileType: 'PDF',
    fileSize: '1.2 MB',
    lastUpdated: '2024-11-15',
    downloadCount: 890,
    featured: true
  },
  {
    id: 3,
    title: 'Dangerous Goods Declaration Form',
    description: 'IATA compliant dangerous goods declaration form for air freight shipments.',
    category: 'Forms',
    fileType: 'PDF',
    fileSize: '180 KB',
    lastUpdated: '2024-12-10',
    downloadCount: 567,
    featured: true
  },
  {
    id: 4,
    title: 'Customs Brokerage Service Brochure',
    description: 'Detailed brochure outlining our customs brokerage services and capabilities.',
    category: 'Brochures',
    fileType: 'PDF',
    fileSize: '3.4 MB',
    lastUpdated: '2024-10-20',
    downloadCount: 423,
    featured: false
  },
  {
    id: 5,
    title: 'Warehouse Storage Application',
    description: 'Application form for warehouse storage services including bonded and climate-controlled options.',
    category: 'Forms',
    fileType: 'PDF',
    fileSize: '320 KB',
    lastUpdated: '2024-11-30',
    downloadCount: 234,
    featured: false
  },
  {
    id: 6,
    title: 'Insurance Coverage Guide',
    description: 'Comprehensive guide to cargo insurance options and coverage details.',
    category: 'Guides',
    fileType: 'PDF',
    fileSize: '890 KB',
    lastUpdated: '2024-09-15',
    downloadCount: 678,
    featured: false
  },
  {
    id: 7,
    title: 'Special Transport Request Form',
    description: 'Specialized form for oversized, hazardous, or high-value cargo transport requests.',
    category: 'Forms',
    fileType: 'PDF',
    fileSize: '275 KB',
    lastUpdated: '2024-11-25',
    downloadCount: 156,
    featured: false
  },
  {
    id: 8,
    title: 'Compliance Checklist - Import/Export',
    description: 'Essential checklist for import and export compliance requirements.',
    category: 'Compliance',
    fileType: 'PDF',
    fileSize: '450 KB',
    lastUpdated: '2024-12-05',
    downloadCount: 789,
    featured: false
  },
  {
    id: 9,
    title: 'Customer Portal User Guide',
    description: 'Step-by-step guide for using our online customer portal and tracking system.',
    category: 'Guides',
    fileType: 'PDF',
    fileSize: '1.8 MB',
    lastUpdated: '2024-11-28',
    downloadCount: 345,
    featured: false
  },
  {
    id: 10,
    title: 'Air Freight Transit Time Guide',
    description: 'Detailed transit times for air freight services to major global destinations.',
    category: 'Guides',
    fileType: 'PDF',
    fileSize: '650 KB',
    lastUpdated: '2024-10-30',
    downloadCount: 512,
    featured: false
  }
]

const categories = [
  { value: 'all', label: 'All Categories', icon: 'lucide:folder' },
  { value: 'Forms', label: 'Forms', icon: 'lucide:file-text' },
  { value: 'Rate Guides', label: 'Rate Guides', icon: 'lucide:calculator' },
  { value: 'Brochures', label: 'Brochures', icon: 'lucide:book' },
  { value: 'Guides', label: 'Guides', icon: 'lucide:help-circle' },
  { value: 'Compliance', label: 'Compliance', icon: 'lucide:shield-check' }
]

const selectedCategory = ref('all')
const searchQuery = ref('')

const filteredDownloads = computed(() => {
  let filtered = downloads

  if (selectedCategory.value !== 'all') {
    filtered = filtered.filter(item => item.category === selectedCategory.value)
  }

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(item => 
      item.title.toLowerCase().includes(query) || 
      item.description.toLowerCase().includes(query)
    )
  }

  return filtered
})

const featuredDownloads = computed(() => downloads.filter(item => item.featured))

const getFileIcon = (fileType) => {
  switch (fileType.toLowerCase()) {
    case 'pdf': return 'lucide:file-text'
    case 'doc':
    case 'docx': return 'lucide:file-text'
    case 'xls':
    case 'xlsx': return 'lucide:file-spreadsheet'
    default: return 'lucide:file'
  }
}
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Downloads & Resources"
      description="Access essential forms, guides, rate sheets, and documentation for all your logistics needs."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Downloads Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <img
            src="/images/downloads.png"
            alt="Downloads and resources"
            class="absolute inset-0 w-full h-full object-cover scale-105 transition-transform duration-[20s] hover:scale-110"
          />
          <!-- Gradient overlay for better text readability -->
          <div class="absolute inset-0 bg-gradient-to-b from-blue-900/40 via-black/50 to-black/70"></div>
          <!-- Animated particles overlay -->
          <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4xIj48Y2lyY2xlIGN4PSIzMCIgY3k9IjMwIiByPSIxIi8+PC9nPjwvZz48L3N2Zz4=')] opacity-30 animate-pulse"></div>
        </div>
      </template>

      <template #title>
        <div class="flex items-center justify-center gap-4 mb-4">
          <UIcon name="lucide:download" class="text-primary text-3xl" />
          <h1 class="text-white drop-shadow-lg">Downloads & Resources</h1>
        </div>
      </template>

      <template #links>
        <UButton
          label="Request Custom Document"
          icon="lucide:file-plus"
          trailing
          color="primary"
          to="/contact"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="Browse All Files"
          icon="lucide:folder"
          size="xl"
          color="white"
          variant="outline"
          to="#downloads"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Search and Filter -->
    <UPageSection class="pb-0">
      <div class="flex flex-col md:flex-row gap-4 mb-8">
        <div class="flex-1">
          <UInput
            v-model="searchQuery"
            placeholder="Search documents..."
            icon="lucide:search"
            size="lg"
          />
        </div>
        <div class="flex gap-2 overflow-x-auto">
          <UButton
            v-for="category in categories"
            :key="category.value"
            :variant="selectedCategory === category.value ? 'solid' : 'outline'"
            size="sm"
            @click="selectedCategory = category.value"
            class="whitespace-nowrap"
          >
            <UIcon :name="category.icon" class="mr-2" />
            {{ category.label }}
          </UButton>
        </div>
      </div>
    </UPageSection>

    <!-- Featured Downloads -->
    <UPageSection
      title="Popular Downloads"
      description="Most frequently accessed documents and resources."
    >
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="item in featuredDownloads"
          :key="item.id"
          class="group cursor-pointer"
        >
          <UCard class="h-full hover:shadow-lg transition-shadow">
            <template #header>
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                  <UIcon :name="getFileIcon(item.fileType)" class="text-xl text-primary" />
                </div>
                <div class="flex-1">
                  <h3 class="font-semibold group-hover:text-primary transition-colors">{{ item.title }}</h3>
                  <div class="flex items-center gap-2 text-sm text-muted-foreground">
                    <span class="bg-primary/10 text-primary px-2 py-1 rounded text-xs">{{ item.fileType }}</span>
                    <span>{{ item.fileSize }}</span>
                  </div>
                </div>
              </div>
            </template>
            
            <div class="space-y-4">
              <p class="text-sm text-muted-foreground">{{ item.description }}</p>
              
              <div class="flex items-center justify-between text-xs text-muted-foreground">
                <span>Updated: {{ new Date(item.lastUpdated).toLocaleDateString() }}</span>
                <span>{{ item.downloadCount }} downloads</span>
              </div>
              
              <UButton size="sm" block class="group-hover:bg-primary group-hover:text-white transition-colors">
                <UIcon name="lucide:download" class="mr-2" />
                Download
              </UButton>
            </div>
          </UCard>
        </div>
      </div>
    </UPageSection>

    <!-- All Downloads -->
    <UPageSection
      title="All Resources"
      description="Complete library of forms, guides, and documentation."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="space-y-4">
        <div
          v-for="item in filteredDownloads"
          :key="item.id"
          class="bg-white dark:bg-gray-800 rounded-lg p-6 hover:shadow-lg transition-shadow group cursor-pointer"
        >
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
              <UIcon :name="getFileIcon(item.fileType)" class="text-xl text-primary" />
            </div>
            
            <div class="flex-1 min-w-0">
              <div class="flex items-start justify-between mb-2">
                <h3 class="font-semibold text-lg group-hover:text-primary transition-colors">{{ item.title }}</h3>
                <div class="flex items-center gap-2 flex-shrink-0">
                  <span class="bg-primary/10 text-primary px-2 py-1 rounded text-xs font-medium">{{ item.category }}</span>
                  <span class="text-sm text-muted-foreground">{{ item.fileSize }}</span>
                </div>
              </div>
              
              <p class="text-muted-foreground mb-4">{{ item.description }}</p>
              
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-4 text-sm text-muted-foreground">
                  <div class="flex items-center gap-1">
                    <UIcon name="lucide:calendar" />
                    <span>Updated: {{ new Date(item.lastUpdated).toLocaleDateString() }}</span>
                  </div>
                  <div class="flex items-center gap-1">
                    <UIcon name="lucide:download" />
                    <span>{{ item.downloadCount }} downloads</span>
                  </div>
                </div>
                
                <UButton size="sm" class="group-hover:bg-primary group-hover:text-white transition-colors">
                  <UIcon name="lucide:download" class="mr-2" />
                  Download {{ item.fileType }}
                </UButton>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- No Results -->
      <div v-if="filteredDownloads.length === 0" class="text-center py-12">
        <UIcon name="lucide:search-x" class="text-4xl text-muted-foreground mx-auto mb-4" />
        <h3 class="text-lg font-semibold mb-2">No documents found</h3>
        <p class="text-muted-foreground mb-6">Try adjusting your search or filter criteria.</p>
        <UButton @click="searchQuery = ''; selectedCategory = 'all'" variant="outline">
          Clear Filters
        </UButton>
      </div>
    </UPageSection>

    <!-- Custom Request CTA -->
    <UPageCTA
      title="Can't find what you need?"
      description="If you can't find the specific document or resource you're looking for, our team can create custom documentation for your requirements."
      :links="[
        {
          label: 'Request Custom Document',
          to: '/contact',
          color: 'primary'
        },
        {
          label: 'Contact Support',
          to: 'tel:+61299990000',
          variant: 'outline'
        }
      ]"
    />
  </div>
</template>
