<template>
  <q-page class="text-white q-pa-md">
    <AlbumsList :albums="albums" :artists="artists" />
  </q-page>
</template>

<script setup lang="ts">
import AlbumsList  from 'components/Lists/AlbumsList.vue';
import { api } from 'src/boot/axios';
import type { AlbumsType } from 'src/components/Types/AlbumsType';
import type { ArtistsType } from 'src/components/Types/ArtistsType';
import { ref,  onMounted } from 'vue';

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


</script>
