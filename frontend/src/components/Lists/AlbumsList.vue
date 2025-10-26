<template>
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
</template>

<script setup lang="ts">
import AlbumsCard from 'components/Cards/AlbumsCard.vue';
import type { AlbumsType } from 'src/components/Types/AlbumsType';
import type { ArtistsType } from 'src/components/Types/ArtistsType';
import { ref, computed } from 'vue';

const props = defineProps<{
  albums: AlbumsType[],
  artists: ArtistsType[]
}>();

const itemsPerPage = 10
const currentPage = ref(1)

const totalPages = computed(() => Math.ceil(props.albums.length / itemsPerPage))

const paginatedAlbums = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return props.albums.slice(start, start + itemsPerPage)
})
</script>
