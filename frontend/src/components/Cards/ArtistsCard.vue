<template>
    <q-card class="q-ma-md q-pa-md shadow-2 rounded-borders cursor-pointer" style="max-width: 300px;" @click="handleClick()">
        <!-- Image et titre de l'album -->
        <q-card-section class="q-pa-none">
            <q-img 
            :src="`/images/artists/${props.artist.avatar}`"
            alt="Album Cover"
            style="width: 200px; height: 200px; border-radius: 50%;"
            />
            <div class="text-h6 text-center q-mt-sm">{{ props.artist.name }}</div>
        </q-card-section>
    </q-card>
</template>

<script setup lang="ts">
import type { ArtistsType } from '../Types/ArtistsType';
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps<{
    artist: ArtistsType
}>();

async function handleClick() {
    await router.push(`/artists/${props.artist.id}`)
}
</script>