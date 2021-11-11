<template>
    <div id="create">
        <b-progress max="5" v-show="$store.state.step < 5"
                    show-progress animated height="3rem" class="mb-3">
            <b-progress-bar class="bg-info" :value="$store.state.step+1">
                <span>Прогресс: <strong>{{ $store.state.step + 1 }} / 5</strong></span>
            </b-progress-bar>
        </b-progress>
        <!--    Блок обложки    -->
        <template v-if="$store.state.step === 0">
            <h3 class="mb-3">Выберите обложку</h3>
            <b-list-group class="mb-5">
                <b-list-group-item
                        href="#"
                        v-for="cover in $store.state.albumSettings.covers"
                        :key="cover.id"
                        :active="(cover.id === $store.state.albumOrder.cover)"
                        @click="$store.dispatch('setAlbumOrderParam', {param: 'cover', value: cover.id})"
                >{{ cover.cover }}
                </b-list-group-item>
            </b-list-group>
            <b-row class="justify-content-end">
                <b-button class="px-5 btn-info"
                          :disabled="$store.state.albumOrder.cover===0"
                          @click="$store.state.step++"
                >Далее
                </b-button>
            </b-row>
        </template>
        <!--    Блок  орнамента   -->
        <template v-if="$store.state.step === 1">
            <h3 class="mb-3">Выберите орнамент</h3>
            <b-list-group class="mb-5">
                <b-list-group-item
                        href="#"
                        v-for="pattern in $store.state.albumSettings.patterns"
                        :key="pattern.id"
                        :active="(pattern.id === $store.state.albumOrder.pattern)"
                        @click="$store.dispatch('setAlbumOrderParam', {param: 'pattern', value: pattern.id})"
                >{{ pattern.pattern }}
                </b-list-group-item>
            </b-list-group>
            <b-row class="justify-content-between">
                <b-button class="px-5 btn-info"
                          @click="$store.state.step--"
                >Назад
                </b-button>
                <b-button class="px-5 btn-info"
                          :disabled="$store.state.albumOrder.pattern===0"
                          @click="$store.state.step++"
                >Далее
                </b-button>
            </b-row>
        </template>
        <!--    Блок  размеров и количества страниц   -->
        <template v-if="$store.state.step === 2">
            <h3 class="mb-3">Выберите тип страниц и их количество</h3>
            <b-list-group class="mb-3">
                <b-list-group-item
                        href="#"
                        v-for="page in $store.state.albumSettings.pages"
                        :key="page.id"
                        :active="(page.id === $store.state.albumOrder.pagesType)"
                        @click="$store.dispatch('setAlbumOrderParam', {param: 'pagesType', value: page.id})"
                >{{ page.page }}
                </b-list-group-item>
            </b-list-group>
            <template>
                <b-row class="my-1 w-50">
                    <b-col sm="3">
                        <label for="pages-count">Количество страниц:</label>
                    </b-col>
                    <b-col sm="9">
                        <b-form-input id="pages-count" type="number" min="10" v-model="pageCount" step="1"
                                      @change="[pagesCountValidation(),$store.dispatch('setAlbumOrderParam', {param: 'pagesCount', value: pageCount})]"/>
                    </b-col>
                </b-row>
            </template>
            <b-row class="justify-content-between mt-5">
                <b-button class="px-5 btn-info"
                          @click="$store.state.step--"
                >Назад
                </b-button>
                <b-button class="px-5 btn-info"
                          :disabled="$store.state.albumOrder.pagesType===0 || !pagesCountValidation()"
                          @click="$store.state.step++"
                >Далее
                </b-button>
            </b-row>
        </template>
        <!--    Блок размера страниц   -->
        <template v-if="$store.state.step === 3">
            <h3 class="mb-3">Выберите размер альбома</h3>
            <b-list-group class="mb-3">
                <b-list-group-item
                        href="#"
                        v-for="size in $store.state.albumSettings.sizes"
                        :key="size.id"
                        :active="(size.id === $store.state.albumOrder.size)"
                        @click="$store.dispatch('setAlbumOrderParam', {param: 'size', value: size.id})"
                >{{ size.size }}
                </b-list-group-item>
            </b-list-group>
            <b-row class="justify-content-between mt-5">
                <b-button class="px-5 btn-info"
                          @click="$store.state.step--"
                >Назад
                </b-button>
                <b-button class="px-5 btn-info"
                          :disabled="$store.state.albumOrder.size===0"
                          @click="$store.state.step++"
                >Далее
                </b-button>
            </b-row>
        </template>
        <!--    Блок  информации   -->
        <template v-if="$store.state.step === 4">
            <h3 class="mb-3">Введите данные</h3>
            <p>Введите ваше имя и телефон, чтобы наш менеджер мог с вами связаться.</p>
            <b-row class="my-1">
                <b-col sm="3">
                    <label for="person-name">Ваше имя:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input id="person-name" v-model="information.name"/>
                </b-col>
            </b-row>
            <b-row class="my-1">
                <b-col sm="3">
                    <label for="person-surname">Ваша фамилия:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input id="person-surname" v-model="information.surname"/>
                </b-col>
            </b-row>
            <b-row class="my-1">
                <b-col sm="3">
                    <label for="person-tel">Ваш телефон:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input id="person-tel" v-model="information.number"/>
                </b-col>
            </b-row>
            <b-row class="justify-content-between mt-5">
                <b-button class="px-5 btn-info"
                          @click="$store.state.step--"
                >Назад
                </b-button>
                <b-button class="px-5 btn-info"
                          :disabled="!informationValidation()"
                          @click="[$store.state.step++, $store.dispatch('setBuyerOrderParam', information)]"
                >Отправить
                </b-button>
            </b-row>
        </template>
        <!--    Блок  завершения   -->
        <template v-if="$store.state.step === 5">
            <h3 class="mb-3">Cпасибо за заказ!</h3>
            <p>Скоро менеджер свяжется с вами!</p>
            <router-link to="/" tag="b-button" class="bg-info py-3 px-5">Вернуться на главную</router-link>
        </template>
    </div>
</template>

<script>
export default {
    name: 'Create',
    data: () => ({
        pageCount: 10,
        information: {
            name: '',
            surname: '',
            number: '',
        },
    }),
    async mounted() {
        await this.$store.dispatch('getAlbums');
        this.information = this.$store.state.buyerOrder
    },
    methods: {
        pagesCountValidation() {
            return (this.pageCount >= 10 && this.pageCount % 1 === 0);
        },
        informationValidation() {
            const isCorrectName = this.information.name.length > 0;
            const isCorrectSurname = this.information.surname.length > 0;
            const isCorrectTel = this.information.number.length > 10 && this.information.number.length < 13 && this.information.number.match(/^\d+$/);

            return isCorrectSurname && isCorrectName && isCorrectTel;
        },
    },
};
</script>

<style scoped>

</style>
