<script setup lang="ts">
const columns = [{
  label: 'Services',
  children: [{
    label: 'Air Freight',
    to: '/services/air-freight'
  }, {
    label: 'Sea Freight',
    to: '/services/sea-freight'
  }, {
    label: 'Special Transports',
    to: '/services/special-transports'
  }, {
    label: 'Customs Brokerage',
    to: '/services/customs-brokerage'
  }, {
    label: 'Storage Solutions',
    to: '/services/storage'
  }]
}, {
  label: 'Offices',
  children: [{
    label: 'Sydney',
    to: '/offices/sydney'
  }, {
    label: 'Melbourne',
    to: '/offices/melbourne'
  }, {
    label: 'Brisbane',
    to: '/offices/brisbane'
  }, {
    label: 'Perth',
    to: '/offices/perth'
  }]
}, {
  label: 'Company',
  children: [{
    label: 'About Us',
    to: '/about'
  }, {
    label: 'Contact',
    to: '/contact'
  }, {
    label: 'Careers',
    to: '/careers'
  }, {
    label: 'News',
    to: '/service-center/news'
  }]
}]

</script>

<template>
  <USeparator
    icon="lucide:truck"
    class="h-px"
  />

  <UFooter :ui="{ top: 'border-b border-default' }">
    <template #top>
      <UContainer>
        <UFooterColumns :columns="columns" />
      </UContainer>
    </template>

    <template #left>
      <p class="text-sm text-muted">
        AGL LOGISTICS • Professional Freight & Logistics Services • © {{ new Date().getFullYear() }}
      </p>
    </template>

    <template #right>
      <UButton
        to="tel:+61-2-9999-0000"
        icon="lucide:phone"
        aria-label="Call AGL Logistics"
        color="neutral"
        variant="ghost"
      />
      <UButton
        to="mailto:info@agllogistics.com.au"
        icon="lucide:mail"
        aria-label="Email AGL Logistics"
        color="neutral"
        variant="ghost"
      />
      <UButton
        to="https://linkedin.com/company/agl-logistics"
        target="_blank"
        icon="i-simple-icons-linkedin"
        aria-label="AGL Logistics on LinkedIn"
        color="neutral"
        variant="ghost"
      />
    </template>
  </UFooter>
</template>
