<template>
  <q-page class="text-white q-pa-md">
    <!-- Liste des cartes -->
    <div class="row q-col-gutter-md q-gutter-md justify-center">
        <ArtistsCard
            v-for="artist in paginatedArtists"
            :key="artist.id"
            :artist="artist"
        />
    </div>

    <!-- Pagination -->
    <div class="row justify-center q-mt-lg">
      <q-pagination
        v-model="currentPage"
        :max="totalPages"
        color="primary"
        boundary-numbers
        direction-links
      />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import ArtistsCard  from 'components/Cards/ArtistsCard.vue';
import { api } from 'src/boot/axios';
import type { ArtistsType } from 'src/components/Types/ArtistsType';
import { ref, computed, onMounted } from 'vue';

const artists = ref<ArtistsType[]>([]);

onMounted(async () => {
    try {
        const responseArtists = await api.get<ArtistsType[]>('/artists');
        artists.value = responseArtists.data.map(artist => ({
            ...artist
        }));

        console.log('Fetched artists:', artists.value);

    } catch (error) {
        console.error('Error fetching albums:', error);
    }
});

// --- Pagination ---
const itemsPerPage = 10
const currentPage = ref(1)

const totalPages = computed(() => Math.ceil(artists.value.length / itemsPerPage))

const paginatedArtists = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return artists.value.slice(start, start + itemsPerPage)
})

</script>
