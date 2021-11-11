import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    reviews: [],
    buyers: [],
    buyer: {},
    albumSettings: {
      sizes: [],
      covers: [],
      patterns: [],
      pages: []
    },
    albumOrder: {
      size: 0,
      cover: 0,
      pattern: 0,
      pagesType: 0,
      pagesCount: 10,
    },
    buyerOrder:{
      name: '',
      surname: '',
      number: ''
    },
    step: 0
  },
  mutations: {
    updateReviews(state, reviews) {
      state.reviews = reviews
    },
    updateBuyers(state, buyers) {
      state.buyers.push(buyers)
    },
    updateBuyer(state, buyer) {
      state.buyer = buyer
    },
    updateAlbums(state, albums) {
      state.albumSettings = albums
    },
    updateAlbumOrder(state, param) {
      state.albumOrder[param.param] = param.value
    },
    updateBuyerOrder(state, buyer){
      state.buyerOrder = buyer
    },
    async sendData(state){
      axios.post('buyer/',state.buyerOrder)
      axios.get('buyer/').then((resp)=> {
        state.albumOrder.buyer = resp.data[resp.data.length-1].id
        state.albumOrder.status = 'В обработке'
        axios.post('order/',state.albumOrder)
      })
    }
  },
  actions: {
    async getReviews(action) {
      const reviews = (await (axios.get('review/'))).data
      action.commit('updateReviews', reviews)
    },
    async getBuyers(action) {
      const buyers = (await axios.get('buyer/')).data
      action.commit('updateBuyers', buyers)
    },
    async getBuyer(action, id) {
      const buyer = (await axios.get('buyer/'+id+'/')).data
      action.commit('updateBuyer', buyer)
    },
    async getAlbums(action) {
      const sizes = (await axios.get('size/')).data
      const covers = (await axios.get('cover/')).data
      const patterns = (await axios.get('pattern/')).data
      const pages = (await axios.get('page/')).data

      const albums = {sizes,covers,patterns,pages}
      action.commit('updateAlbums', albums)
    },
    setAlbumOrderParam(action, param){
      action.commit('updateAlbumOrder', param)
    },
    setBuyerOrderParam(action, buyer){
      action.commit('updateBuyerOrder', buyer)
      action.commit('sendData')
    }
  },
  modules: {
  }
})
