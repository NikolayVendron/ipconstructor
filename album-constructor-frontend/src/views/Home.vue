<template>
    <div id="home"
         class="text-center"
    >
        <p>
            Создайте лучшую фотокнигу, в которой будут храниться ваши фотографии!
        </p>
        <router-link to="/create" tag="b-button" class="bg-info py-3 px-5">Заказать альбом</router-link>
    </div>
</template>

<script>


export default {
    name: 'Home',
};
</script>
