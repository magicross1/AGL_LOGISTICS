<script setup lang="ts">
interface Props {
  type?: 'organization' | 'website' | 'service' | 'office'
  data?: Record<string, any>
}

const props = withDefaults(defineProps<Props>(), {
  type: 'organization'
})

// Base organization data
const organizationData = {
  '@context': 'https://schema.org',
  '@type': 'Organization',
  name: 'AGL LOGISTICS PTY LTD',
  alternateName: 'AGL LOGISTICS',
  url: 'https://agllogistics.com.au',
  logo: 'https://agllogistics.com.au/images/logo.png',
  image: 'https://agllogistics.com.au/og-image.svg',
  description: 'Leading Australian freight forwarder providing comprehensive air freight, sea freight, customs brokerage, and storage solutions across Sydney, Melbourne, Brisbane & Perth.',
  foundingDate: '2000',
  numberOfEmployees: '50-100',
  industry: 'Freight Forwarding and Logistics',
  areaServed: {
    '@type': 'Country',
    name: 'Australia'
  },
  contactPoint: [
    {
      '@type': 'ContactPoint',
      telephone: '+61-2-8747-3069',
      contactType: 'customer service',
      areaServed: 'AU',
      availableLanguage: ['English', 'Mandarin']
    },
    {
      '@type': 'ContactPoint',
      telephone: '+61-2-8747-3069',
      contactType: 'emergency',
      areaServed: 'AU',
      availableLanguage: 'English',
      hoursAvailable: '24/7'
    }
  ],
  address: [
    {
      '@type': 'PostalAddress',
      streetAddress: '6 Ladbroke Street',
      addressLocality: 'Milperra',
      addressRegion: 'NSW',
      postalCode: '2214',
      addressCountry: 'AU'
    },
    {
      '@type': 'PostalAddress',
      streetAddress: '12 Hawthorn Avenue',
      addressLocality: 'Sunshine North',
      addressRegion: 'VIC',
      postalCode: '3020',
      addressCountry: 'AU'
    },
    {
      '@type': 'PostalAddress',
      streetAddress: 'U2/26 Navigator Pl',
      addressLocality: 'Hendra',
      addressRegion: 'QLD',
      postalCode: '4011',
      addressCountry: 'AU'
    }
  ],
  sameAs: [
    'https://www.linkedin.com/company/agl-logistics',
    'https://www.facebook.com/agllogistics',
    'https://twitter.com/agllogistics'
  ],
  hasOfferCatalog: {
    '@type': 'OfferCatalog',
    name: 'Logistics Services',
    itemListElement: [
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Air Freight Services',
          description: 'Fast and reliable air cargo services connecting Australia to global destinations'
        }
      },
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Sea Freight Services',
          description: 'Cost-effective ocean freight solutions for FCL and LCL shipments'
        }
      },
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Customs Brokerage',
          description: 'Expert customs clearance services ensuring compliant processing'
        }
      },
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Special Transports',
          description: 'Specialized handling for oversized, hazardous, and high-value cargo'
        }
      },
      {
        '@type': 'Offer',
        itemOffered: {
          '@type': 'Service',
          name: 'Storage Solutions',
          description: 'Modern warehouse facilities with climate control and security systems'
        }
      }
    ]
  }
}

// Website structured data
const websiteData = {
  '@context': 'https://schema.org',
  '@type': 'WebSite',
  name: 'AGL LOGISTICS PTY LTD',
  url: 'https://agllogistics.com.au',
  description: 'Professional freight forwarding and logistics services across Australia',
  publisher: {
    '@type': 'Organization',
    name: 'AGL LOGISTICS PTY LTD'
  },
  potentialAction: {
    '@type': 'SearchAction',
    target: 'https://agllogistics.com.au/search?q={search_term_string}',
    'query-input': 'required name=search_term_string'
  }
}

// Service page structured data
const serviceData = {
  '@context': 'https://schema.org',
  '@type': 'Service',
  provider: {
    '@type': 'Organization',
    name: 'AGL LOGISTICS PTY LTD'
  },
  areaServed: {
    '@type': 'Country',
    name: 'Australia'
  },
  ...props.data
}

// Office/Local Business structured data
const officeData = {
  '@context': 'https://schema.org',
  '@type': 'LocalBusiness',
  '@id': `https://agllogistics.com.au/offices/${props.data?.city?.toLowerCase()}`,
  name: `AGL LOGISTICS ${props.data?.city} Office`,
  parentOrganization: {
    '@type': 'Organization',
    name: 'AGL LOGISTICS PTY LTD'
  },
  ...props.data
}

const getStructuredData = () => {
  switch (props.type) {
    case 'website':
      return websiteData
    case 'service':
      return { ...serviceData, ...props.data }
    case 'office':
      return { ...officeData, ...props.data }
    default:
      return organizationData
  }
}

const structuredData = computed(() => getStructuredData())

useHead({
  script: [
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify(structuredData.value)
    }
  ]
})
</script>

<template>
  <!-- This component only provides structured data, no visual output -->
</template>
