<template>
    <div id="app">
        <b-navbar type="dark" variant="dark">
            <b-navbar-brand tag="h1" class="mb-0 text- mr-5 h-25 text-info">Фотоальбомы.ру</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item
                        v-for="link in routerLinks"
                        :key="link.link"
                >
                    <router-link :to="link.link"
                                 class="text-decoration-none text-white">
                        {{ link.title }}
                    </router-link>
                </b-nav-item>
            </b-navbar-nav>
        </b-navbar>
        <main>
            <div class="container my-5">
                <router-view/>
            </div>
        </main>
    </div>
</template>

<script>
export default {
    name: 'App',
    data: () => ({
        routerLinks: [
            {
                link: '/',
                title: 'Главная',
            },
            {
                link: 'reviews',
                title: 'Отзывы',
            },
            {
                link: 'about',
                title: 'О нас',
            },
        ],
    }),
};
</script>

<style lang="scss">

</style>
