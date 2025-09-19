<script setup lang="ts">
useSeoMeta({
  title: 'Service Center - AGL LOGISTICS',
  description: 'Access the latest news, notices, downloads, and resources from AGL LOGISTICS. Stay updated with industry insights and company announcements.',
})
</script>

<template>
  <div class="relative">
    <!-- Hero Section -->
    <UPageHero
      title="Service Center"
      description="Stay informed with the latest news, important notices, and access essential resources and downloads."
      :ui="{
        container: 'md:pt-24 lg:pt-32 pb-24 lg:pb-32 relative z-10',
        title: 'max-w-4xl mx-auto text-white',
        description: 'max-w-3xl mx-auto text-white/90 text-lg',
        links: 'justify-center gap-4'
      }"
      class="relative min-h-[80vh] flex items-center"
    >
      <template #top>
        <!-- Service Center Background -->
        <div class="absolute inset-0 w-full h-full overflow-hidden">
          <img
            src="/images/sc.png"
            alt="Service center"
            class="absolute inset-0 w-full h-full object-cover scale-105 transition-transform duration-[20s] hover:scale-110"
          />
          <!-- Gradient overlay for better text readability -->
          <div class="absolute inset-0 bg-gradient-to-b from-gray-900/40 via-black/50 to-black/70"></div>
          <!-- Animated particles overlay -->
          <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4xIj48Y2lyY2xlIGN4PSIzMCIgY3k9IjMwIiByPSIxIi8+PC9nPjwvZz48L3N2Zz4=')] opacity-30 animate-pulse"></div>
        </div>
      </template>

      <template #title>
        <div class="flex items-center justify-center gap-4 mb-4">
          <UIcon name="lucide:settings" class="text-primary text-3xl" />
          <h1 class="text-white drop-shadow-lg">Service Center</h1>
        </div>
      </template>

      <template #links>
        <UButton
          label="Subscribe to Updates"
          icon="lucide:bell"
          trailing
          color="primary"
          to="#subscribe"
          size="xl"
          class="bg-primary hover:bg-primary/90 text-white font-semibold px-8 py-4 shadow-lg"
        />
        <UButton
          label="Contact Support"
          icon="lucide:headphones"
          size="xl"
          color="white"
          variant="outline"
          to="/contact"
          class="border-white text-white hover:bg-white hover:text-gray-900 font-semibold px-8 py-4 shadow-lg"
        />
      </template>
    </UPageHero>

    <!-- Quick Access -->
    <UPageSection
      title="Quick Access"
      description="Find what you need quickly with our organized service center categories."
    >
      <div class="grid md:grid-cols-3 gap-8">
        <UCard class="hover:shadow-lg transition-shadow">
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:newspaper" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Latest News</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <p class="text-muted-foreground">Stay updated with company news, industry insights, and logistics market developments.</p>
            
            <div class="space-y-2">
              <div class="text-sm">
                <span class="font-semibold">Recent Topics:</span>
                <ul class="mt-1 space-y-1 text-muted-foreground">
                  <li>• New route announcements</li>
                  <li>• Service expansions</li>
                  <li>• Industry partnerships</li>
                  <li>• Technology updates</li>
                </ul>
              </div>
            </div>

            <UButton to="/service-center/news" variant="outline" size="sm" block>
              View All News
            </UButton>
          </div>
        </UCard>

        <UCard class="hover:shadow-lg transition-shadow">
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:alert-circle" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Important Notices</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <p class="text-muted-foreground">Critical updates, service disruptions, regulatory changes, and important operational notices.</p>
            
            <div class="space-y-2">
              <div class="text-sm">
                <span class="font-semibold">Notice Types:</span>
                <ul class="mt-1 space-y-1 text-muted-foreground">
                  <li>• Service disruptions</li>
                  <li>• Regulatory updates</li>
                  <li>• Holiday schedules</li>
                  <li>• Emergency procedures</li>
                </ul>
              </div>
            </div>

            <UButton to="/service-center/notices" variant="outline" size="sm" block>
              View All Notices
            </UButton>
          </div>
        </UCard>

        <UCard class="hover:shadow-lg transition-shadow">
          <template #header>
            <div class="flex items-center gap-3">
              <UIcon name="lucide:download" class="text-2xl text-primary" />
              <h3 class="text-xl font-semibold">Downloads</h3>
            </div>
          </template>
          
          <div class="space-y-4">
            <p class="text-muted-foreground">Access forms, guides, rate sheets, and other essential documents for your logistics needs.</p>
            
            <div class="space-y-2">
              <div class="text-sm">
                <span class="font-semibold">Available Resources:</span>
                <ul class="mt-1 space-y-1 text-muted-foreground">
                  <li>• Shipping forms</li>
                  <li>• Rate guides</li>
                  <li>• Service brochures</li>
                  <li>• Compliance documents</li>
                </ul>
              </div>
            </div>

            <UButton to="/service-center/downloads" variant="outline" size="sm" block>
              View All Downloads
            </UButton>
          </div>
        </UCard>
      </div>
    </UPageSection>

    <!-- Featured Content -->
    <UPageSection
      title="Featured Updates"
      description="Highlighted news and important announcements from AGL LOGISTICS."
      class="bg-gray-50 dark:bg-gray-900"
    >
      <div class="grid md:grid-cols-2 gap-8">
        <!-- Featured News -->
        <div>
          <h3 class="text-xl font-semibold mb-6">Latest News</h3>
          <div class="space-y-6">
            <article class="border-l-4 border-primary pl-4">
              <div class="flex items-center gap-2 text-sm text-muted-foreground mb-2">
                <UIcon name="lucide:calendar" />
                <time>December 15, 2024</time>
              </div>
              <h4 class="font-semibold mb-2">AGL LOGISTICS Expands Air Freight Network to Southeast Asia</h4>
              <p class="text-sm text-muted-foreground">New direct routes now available to Singapore, Malaysia, and Thailand with competitive rates and faster transit times.</p>
              <UButton variant="ghost" size="xs" class="mt-2 p-0">
                Read More →
              </UButton>
            </article>

            <article class="border-l-4 border-primary pl-4">
              <div class="flex items-center gap-2 text-sm text-muted-foreground mb-2">
                <UIcon name="lucide:calendar" />
                <time>December 10, 2024</time>
              </div>
              <h4 class="font-semibold mb-2">New Climate-Controlled Warehouse Opens in Brisbane</h4>
              <p class="text-sm text-muted-foreground">State-of-the-art facility adds 5,000 sqm of temperature-controlled storage capacity for pharmaceutical and perishable goods.</p>
              <UButton variant="ghost" size="xs" class="mt-2 p-0">
                Read More →
              </UButton>
            </article>

            <article class="border-l-4 border-primary pl-4">
              <div class="flex items-center gap-2 text-sm text-muted-foreground mb-2">
                <UIcon name="lucide:calendar" />
                <time>December 5, 2024</time>
              </div>
              <h4 class="font-semibold mb-2">Partnership with Leading Mining Companies</h4>
              <p class="text-sm text-muted-foreground">AGL LOGISTICS announces strategic partnerships to enhance mining logistics and heavy equipment transport services.</p>
              <UButton variant="ghost" size="xs" class="mt-2 p-0">
                Read More →
              </UButton>
            </article>
          </div>
        </div>

        <!-- Important Notices -->
        <div>
          <h3 class="text-xl font-semibold mb-6">Important Notices</h3>
          <div class="space-y-6">
            <div class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-4">
              <div class="flex items-center gap-2 text-sm text-red-600 dark:text-red-400 mb-2">
                <UIcon name="lucide:alert-triangle" />
                <span class="font-semibold">Service Alert</span>
              </div>
              <h4 class="font-semibold mb-2">Port of Melbourne Congestion Notice</h4>
              <p class="text-sm text-muted-foreground">Extended delays expected due to industrial action. Alternative routing via Adelaide available.</p>
              <p class="text-xs text-muted-foreground mt-2">Updated: December 18, 2024</p>
            </div>

            <div class="bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 rounded-lg p-4">
              <div class="flex items-center gap-2 text-sm text-blue-600 dark:text-blue-400 mb-2">
                <UIcon name="lucide:info" />
                <span class="font-semibold">Holiday Schedule</span>
              </div>
              <h4 class="font-semibold mb-2">Christmas & New Year Operating Hours</h4>
              <p class="text-sm text-muted-foreground">Modified operating hours from December 22 - January 2. Emergency services remain available 24/7.</p>
              <p class="text-xs text-muted-foreground mt-2">Posted: December 1, 2024</p>
            </div>

            <div class="bg-green-50 dark:bg-green-900/20 border border-green-200 dark:border-green-800 rounded-lg p-4">
              <div class="flex items-center gap-2 text-sm text-green-600 dark:text-green-400 mb-2">
                <UIcon name="lucide:check-circle" />
                <span class="font-semibold">System Update</span>
              </div>
              <h4 class="font-semibold mb-2">Enhanced Tracking System Now Live</h4>
              <p class="text-sm text-muted-foreground">New features include real-time GPS tracking, automated notifications, and mobile app integration.</p>
              <p class="text-xs text-muted-foreground mt-2">Launched: November 28, 2024</p>
            </div>
          </div>
        </div>
      </div>
    </UPageSection>

    <!-- Newsletter Signup -->
    <UPageSection
      id="subscribe"
      title="Stay Updated"
      description="Subscribe to our newsletter and never miss important updates, news, or service announcements."
    >
      <UContainer class="max-w-2xl">
        <UCard>
          <template #header>
            <div class="text-center">
              <UIcon name="lucide:mail" class="text-3xl text-primary mx-auto mb-2" />
              <h3 class="text-xl font-semibold">Newsletter Subscription</h3>
              <p class="text-sm text-muted-foreground">Get the latest updates delivered to your inbox</p>
            </div>
          </template>

          <UForm class="space-y-4">
            <div class="grid sm:grid-cols-2 gap-4">
              <UFormField name="firstName" label="First Name" required>
                <UInput placeholder="John" />
              </UFormField>
              <UFormField name="lastName" label="Last Name" required>
                <UInput placeholder="Doe" />
              </UFormField>
            </div>
            
            <UFormField name="email" label="Email Address" required>
              <UInput type="email" placeholder="john@company.com" />
            </UFormField>
            
            <UFormField name="company" label="Company (Optional)">
              <UInput placeholder="Your Company Ltd" />
            </UFormField>
            
            <UFormField name="interests" label="Interests">
              <div class="space-y-2">
                <label class="flex items-center gap-2">
                  <input type="checkbox" class="rounded">
                  <span class="text-sm">General news and updates</span>
                </label>
                <label class="flex items-center gap-2">
                  <input type="checkbox" class="rounded">
                  <span class="text-sm">Service disruption alerts</span>
                </label>
                <label class="flex items-center gap-2">
                  <input type="checkbox" class="rounded">
                  <span class="text-sm">New service announcements</span>
                </label>
                <label class="flex items-center gap-2">
                  <input type="checkbox" class="rounded">
                  <span class="text-sm">Industry insights and trends</span>
                </label>
              </div>
            </UFormField>
            
            <UButton type="submit" size="lg" block>
              Subscribe to Newsletter
            </UButton>
            
            <p class="text-xs text-muted-foreground text-center">
              By subscribing, you agree to receive marketing communications from AGL LOGISTICS. You can unsubscribe at any time.
            </p>
          </UForm>
        </UCard>
      </UContainer>
    </UPageSection>
  </div>
</template>
