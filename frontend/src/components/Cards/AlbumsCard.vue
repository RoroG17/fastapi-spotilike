<template>
    <q-card class="q-ma-md q-pa-md shadow-2 rounded-borders cursor-pointer" style="max-width: 300px;" @click="handleClick()">
        <!-- Image et titre de l'album -->
        <q-card-section class="q-pa-none">
            <q-img 
            :src="`/images/covers/${props.album.cover}`"
            alt="Album Cover"
            style="width: 200px; height: 200px;"
            />
            <div class="text-h6 text-center q-mt-sm">{{ props.album.title }}</div>
            <div class="text-subtitle3 text-grey-5 text-center">{{ formatDate(props.album.release_year)}}</div>
        </q-card-section>

        <q-separator class="bg-primary q-my-sm"/>

        <!-- Infos supplémentaires -->
        <q-card-section class="column q-gutter-sm">
            <div class="text-subtitle1">
                <q-img 
                    :src="`/images/artists/${getArtistAvatar(props.album.artist_id)}`"
                    alt="Artist Avatar"
                    height="50px"
                    width="50px"
                    style="border-radius: 50%; margin-right: 1em;"
                />
                {{ getArtistName(props.album.artist_id) }}
            </div>
        </q-card-section>
    </q-card>
</template>

<script setup lang="ts">
import type { AlbumsType } from 'src/components/Types/AlbumsType';
import type { ArtistsType } from '../Types/ArtistsType';
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps<{
    album: AlbumsType,
    artists : Array<ArtistsType>
}>();

function formatDate(date: string): string {
    const dateObj = new Date(date);
    return dateObj.toLocaleDateString('fr-FR', {
        day: '2-digit',
        month: 'short',
        year: 'numeric'
    })
}

async function handleClick() {
    await router.push(`/albums/${props.album.id}`)
}

function getArtistName(artistId: number): string {
    const artist = props.artists.find(artist => artist.id === artistId);
    return artist ? artist.name : 'Unknown Artist';
}

function getArtistAvatar(artistId: number): string {
    const artist = props.artists.find(artist => artist.id === artistId);
    return artist ? artist.avatar : 'https://picsum.photos/50';
}
</script>