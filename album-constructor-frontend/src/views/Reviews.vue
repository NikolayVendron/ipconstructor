<template>
    <div id="reviews">
        <b-row class="my-1 w-50">
            <b-col sm="3">
                <label for="input-name">Поиск по имени:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input id="input-name" v-model="inputs.name" placeholder="Для поиска введите текст"
                              @input="Search"
                />
            </b-col>
        </b-row>
        <b-row class="my-1 w-50">
            <b-col sm="3">
                <label for="input-text">Поиск по тексту:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input id="input-text" v-model="inputs.text" placeholder="Для поиска введите текст"
                              @input="Search"
                />
            </b-col>
        </b-row>

        <hr>
        <template v-if="allReviewsFiltered.length>0">
            <div class="card"
                 v-for="review in allReviewsFiltered"
                 :key="review.id"
            >
                <div class="card-body">
                    <h5 class="card-title">Отзыв</h5>
                    <h6 class="card-subtitle text-black-50">Пользователь: {{ review.buyer }}</h6>
                    <hr>
                    <p class="card-text">{{ review.text }}</p>
                </div>
            </div>
        </template>
        <template v-else>
            Отзывов нет :(
        </template>
    </div>
</template>

<script>
export default {
    name: 'Reviews',
    data: () => ({
        allReviews: [],
        allReviewsFiltered: [],
        inputs: {
            text: '',
            name: ''
        }
    }),
    async mounted() {
        await this.$store.dispatch('getReviews')

        const reviews = this.$store.state.reviews
        for (let review of reviews){
            await this.$store.dispatch('getBuyer', review.id)
            const buyer = this.$store.state.buyer
            review.buyer = buyer.name + ' ' + buyer.surname
        }
        this.allReviews = reviews
        this.allReviewsFiltered = reviews
    },
    methods: {
        Search(){
            this.allReviewsFiltered = this.allReviews.filter(review => (
              (review.buyer.toLowerCase()).includes(this.inputs.name.toLowerCase()) &&
              (review.text.toLowerCase()).includes(this.inputs.text.toLowerCase())
              )
            )
        }
    }
};
</script>

<style scoped>

</style>
