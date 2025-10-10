<template>
  <q-page class="text-white q-pa-md">
    <!-- Liste des cartes -->
    <div class="row q-col-gutter-md q-gutter-md justify-center">
      <AlbumsCard
        v-for="album in paginatedAlbums"
        :key="album.id"
        :album="album"
        :artists="artists"
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
import AlbumsCard  from 'components/Cards/AlbumsCard.vue';
import { api } from 'src/boot/axios';
import type { AlbumsType } from 'src/components/Types/AlbumsType';
import type { ArtistsType } from 'src/components/Types/ArtistsType';
import { ref, computed, onMounted } from 'vue';

const albums = ref<AlbumsType[]>([]);
const artists = ref<ArtistsType[]>([]);

onMounted(async () => {
    try {
        const response = await api.get<AlbumsType[]>('/albums');
        albums.value = response.data.map(album => ({
            ...album
        }));

        const responseArtists = await api.get<ArtistsType[]>('/artists');
        artists.value = responseArtists.data.map(artist => ({
            ...artist
        }));

        console.log('Fetched albums:', albums.value);
    } catch (error) {
        console.error('Error fetching albums:', error);
    }
});

// --- Pagination ---
const itemsPerPage = 10
const currentPage = ref(1)

const totalPages = computed(() => Math.ceil(albums.value.length / itemsPerPage))

const paginatedAlbums = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return albums.value.slice(start, start + itemsPerPage)
})

</script>
