<script setup lang="ts">
useSeoMeta({
  title: 'News & Updates - AGL LOGISTICS',
  description: 'Stay informed with the latest news, company updates, and industry insights from AGL LOGISTICS.',
})

// Mock news data - in a real app, this would come from a CMS or API
const newsArticles = [
  {
    id: 1,
    title: 'AGL LOGISTICS Expands Air Freight Network to Southeast Asia',
    excerpt: 'New direct routes now available to Singapore, Malaysia, and Thailand with competitive rates and faster transit times.',
    content: 'AGL LOGISTICS is pleased to announce the expansion of our air freight network to include new direct routes to Southeast Asia...',
    date: '2024-12-15',
    category: 'Service Expansion',
    author: 'Marketing Team',
    featured: true,
    image: '/images/news/southeast-asia-expansion.jpg'
  },
  {
    id: 2,
    title: 'New Climate-Controlled Warehouse Opens in Brisbane',
    excerpt: 'State-of-the-art facility adds 5,000 sqm of temperature-controlled storage capacity for pharmaceutical and perishable goods.',
    content: 'Our new Brisbane warehouse facility represents a significant investment in cold chain logistics capabilities...',
    date: '2024-12-10',
    category: 'Infrastructure',
    author: 'Operations Team',
    featured: true,
    image: '/images/news/brisbane-warehouse.jpg'
  },
  {
    id: 3,
    title: 'Partnership with Leading Mining Companies',
    excerpt: 'AGL LOGISTICS announces strategic partnerships to enhance mining logistics and heavy equipment transport services.',
    content: 'We are excited to announce new partnerships with several leading mining companies across Australia...',
    date: '2024-12-05',
    category: 'Partnerships',
    author: 'Business Development',
    featured: false,
    image: '/images/news/mining-partnership.jpg'
  },
  {
    id: 4,
    title: 'Digital Transformation Initiative Completed',
    excerpt: 'Implementation of new warehouse management system and customer portal enhances service efficiency.',
    content: 'After 18 months of development and implementation, our digital transformation initiative has been successfully completed...',
    date: '2024-11-28',
    category: 'Technology',
    author: 'IT Department',
    featured: false,
    image: '/images/news/digital-transformation.jpg'
  },
  {
    id: 5,
    title: 'AGL LOGISTICS Wins Logistics Excellence Award',
    excerpt: 'Recognition for outstanding customer service and innovation in the Australian logistics industry.',
    content: 'We are honored to receive the Logistics Excellence Award from the Australian Logistics Council...',
    date: '2024-11-20',
    category: 'Awards',
    author: 'Executive Team',
    featured: false,
    image: '/images/news/excellence-award.jpg'
  }
]

const categories = ['All', 'Service Expansion', 'Infrastructure', 'Partnerships', 'Technology', 'Awards']
const selectedCategory = ref('All')

const filteredArticles = computed(() => {
  if (selectedCategory.value === 'All') {
    return newsArticles
  }
  return newsArticles.filter(article => article.category === selectedCategory.value)
})

const featuredArticles = computed(() => newsArticles.filter(article => article.featured))
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="News & Updates"
      description="Stay informed with the latest news, company updates, and industry insights from AGL LOGISTICS."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- News Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <img
            src="/images/news.png"
            alt="News and updates"
            class="absolute inset-0 w-full h-full object-cover scale-105 transition-transform duration-[20s] hover:scale-110"
          />
          <!-- Gradient overlay for better text readability -->
          <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/50 to-black/70"></div>
          <!-- Animated particles overlay -->
          <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4xIj48Y2lyY2xlIGN4PSIzMCIgY3k9IjMwIiByPSIxIi8+PC9nPjwvZz48L3N2Zz4=')] opacity-30 animate-pulse"></div>
        </div>
      </template>

      <template #title>
        <div class="flex items-center justify-center gap-4 mb-4">
          <UIcon name="lucide:newspaper" class="text-primary text-3xl" />
          <h1 class="text-white drop-shadow-lg">News & Updates</h1>
        </div>
      </template>

      <template #links>
        <UButton
          label="Subscribe to Updates"
          icon="lucide:bell"
          trailing
          color="primary"
          to="/service-center#subscribe"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="View All News"
          icon="lucide:newspaper"
          size="xl"
          color="white"
          variant="outline"
          to="#news"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Featured News -->
    <UPageSection
      title="Featured Stories"
      description="Highlighting our most important news and updates."
    >
      <div class="grid md:grid-cols-2 gap-8">
        <article
          v-for="article in featuredArticles"
          :key="article.id"
          class="group cursor-pointer"
        >
          <UCard class="h-full hover:shadow-lg transition-shadow">
            <template #header>
              <div class="aspect-video bg-gray-200 dark:bg-gray-800 rounded-lg mb-4 flex items-center justify-center">
                <UIcon name="lucide:image" class="text-4xl text-muted-foreground" />
              </div>
              <div class="flex items-center justify-between text-sm text-muted-foreground mb-2">
                <span class="bg-primary/10 text-primary px-2 py-1 rounded text-xs font-medium">
                  {{ article.category }}
                </span>
                <time>{{ new Date(article.date).toLocaleDateString() }}</time>
              </div>
            </template>
            
            <div class="space-y-3">
              <h3 class="text-xl font-semibold group-hover:text-primary transition-colors">
                {{ article.title }}
              </h3>
              <p class="text-muted-foreground">{{ article.excerpt }}</p>
              <div class="flex items-center justify-between">
                <span class="text-sm text-muted-foreground">By {{ article.author }}</span>
                <UButton variant="ghost" size="xs">
                  Read More →
                </UButton>
              </div>
            </div>
          </UCard>
        </article>
      </div>
    </UPageSection>

    <!-- All News -->
    <UPageSection
      title="All News"
      description="Browse all our news and updates by category."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <!-- Category Filter -->
      <div class="mb-8">
        <div class="flex flex-wrap gap-2">
          <UButton
            v-for="category in categories"
            :key="category"
            :variant="selectedCategory === category ? 'solid' : 'outline'"
            size="sm"
            @click="selectedCategory = category"
          >
            {{ category }}
          </UButton>
        </div>
      </div>

      <!-- News Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <article
          v-for="article in filteredArticles"
          :key="article.id"
          class="group cursor-pointer"
        >
          <UCard class="h-full hover:shadow-lg transition-shadow">
            <template #header>
              <div class="aspect-video bg-gray-200 dark:bg-gray-800 rounded-lg mb-4 flex items-center justify-center">
                <UIcon name="lucide:image" class="text-4xl text-muted-foreground" />
              </div>
              <div class="flex items-center justify-between text-sm text-muted-foreground mb-2">
                <span class="bg-primary/10 text-primary px-2 py-1 rounded text-xs font-medium">
                  {{ article.category }}
                </span>
                <time>{{ new Date(article.date).toLocaleDateString() }}</time>
              </div>
            </template>
            
            <div class="space-y-3">
              <h3 class="text-lg font-semibold group-hover:text-primary transition-colors">
                {{ article.title }}
              </h3>
              <p class="text-sm text-muted-foreground line-clamp-3">{{ article.excerpt }}</p>
              <div class="flex items-center justify-between">
                <span class="text-xs text-muted-foreground">By {{ article.author }}</span>
                <UButton variant="ghost" size="xs">
                  Read More →
                </UButton>
              </div>
            </div>
          </UCard>
        </article>
      </div>

      <!-- Load More -->
      <div class="text-center mt-12">
        <UButton variant="outline" size="lg">
          Load More Articles
        </UButton>
      </div>
    </UPageSection>

    <!-- Newsletter CTA -->
    <UPageCTA
      title="Never miss an update"
      description="Subscribe to our newsletter to receive the latest news and updates directly in your inbox."
      :links="[
        {
          label: 'Subscribe Now',
          to: '/service-center#subscribe',
          color: 'primary'
        }
      ]"
    />
  </div>
</template>
