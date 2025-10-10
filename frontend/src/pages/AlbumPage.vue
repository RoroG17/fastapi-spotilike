<template>
    <q-page class="q-pa-md column">
        <!-- Ligne avec bouton retour à gauche et contenu centré -->
        <div class="row items-start justify-center q-mb-md" style="position: relative;">
            
            <!-- Bouton retour positionné à gauche absolu -->
            <q-btn
            flat
            round
            icon="arrow_back"
            @click="$router.back()"
            class="bg-primary"
            style="height: 50px; width: 50px; position: absolute; left: 0;"
            />

            <!-- Contenu centré : image + infos -->
            <div class="row items-center">
            <q-img
                v-if="album"
                :src="`/images/covers/${album.cover}`"
                alt="Album Cover"
                style="width: 200px; height: 200px;"
            />
            <div v-if="album" class="column q-ml-md">
                <h1 class="text-h2">{{ album.title }}</h1>
                <h2 class="text-h4 text-primary" style="margin-top: 0;">{{ album.artist_name }}</h2>
            </div>
            </div>
        </div>

        <div class="row items-center justify-center">
            <q-separator class="bg-primary q-mt-md q-mb-md" style="width: 80%;" />
        </div>

        <!-- Liste des musiques centrée -->
        <div class="column items-center">
            <q-card
            v-for="music in musics"
            :key="music.id"
            class="q-mb-sm"
            style="width: 80%; height: 70px;"
            >
            <q-card-section class="row items-center q-gutter-sm">
                <!-- Icône -->
                <q-icon name="music_note" size="32px" />

                <!-- Titre -->
                <div class="text-h6 ellipsis">
                {{ music.title }} ({{ music.genre }})
                </div>

                <!-- Durée alignée à droite -->
                <div class="text-subtitle2 text-grey-6" style="margin-left: auto;">
                {{ music.duration }}
                </div>
            </q-card-section>
            </q-card>
        </div>

    </q-page>

</template>

<script setup lang="ts">
import { api } from 'src/boot/axios';
import type { AlbumsType } from 'src/components/Types/AlbumsType';
import type { MusicsType } from 'src/components/Types/MusicsType';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router'

const route = useRoute()

const album = ref<AlbumsType>();
const musics = ref<MusicsType[]>([]);
const id = route.params.id;

onMounted(async () => {
    const response = await api.get<AlbumsType>('/albums/:id'.replace(':id', String(id)));
    album.value = response.data;

    const responseMusics = await api.get<MusicsType[]>('/albums/:id/songs'.replace(':id', String(id)));
    musics.value = responseMusics.data;


});
</script>