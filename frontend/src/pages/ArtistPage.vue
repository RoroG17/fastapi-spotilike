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
                    v-if="artist"
                    :src="`/images/artists/${artist.avatar}`"
                    alt="Album Cover"
                    style="width: 200px; height: 200px; border-radius: 50%;"
                />
                <div v-if="artist" class="column q-ml-md">
                    <h1 class="text-h2">{{ artist.name }}</h1>
                    <h2 class="text-h4 text-primary" style="margin-top: 0;">{{ artist.bio }}</h2>
                </div>
            </div>
        </div>

        <div class="row items-center justify-center">
            <q-separator class="bg-primary q-mt-md q-mb-md" style="width: 80%;" />
        </div>

        <AlbumsList :albums="albums" :artists="artist ? [artist] : []" />

        <div class="row items-center justify-center">
            <q-separator class="bg-primary q-mt-md q-mb-md" style="width: 80%;" />
        </div>
        
        <div class="column items-center">
            <h1 class="text-h4 q-mb-xl">Morceaux</h1>
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
import { useRoute } from 'vue-router';
import { api } from 'src/boot/axios';
import type { MusicsType } from 'src/components/Types/MusicsType';
import { ref, onMounted } from 'vue';
import type { ArtistsType } from 'src/components/Types/ArtistsType';
import type { AlbumsType } from 'src/components/Types/AlbumsType';
import AlbumsList from 'components/Lists/AlbumsList.vue';

const route = useRoute()
const id = route.params.id;

const artist = ref<ArtistsType>();
const musics = ref<MusicsType[]>([]);
const albums = ref<AlbumsType[]>([]);

onMounted(async () => {
    const response = await api.get<ArtistsType>('/artists/:id'.replace(':id', String(id)));
    artist.value = response.data;

    const responseMusics = await api.get<MusicsType[]>('/artists/:id/songs'.replace(':id', String(id)));
    musics.value = responseMusics.data;

    const responseAlbums = await api.get<AlbumsType[]>('/albums');
    albums.value = responseAlbums.data.filter(album => album.artist_id === Number(id));

    console.log(musics.value);
    console.log(artist.value);
    console.log(albums.value);
});

</script>