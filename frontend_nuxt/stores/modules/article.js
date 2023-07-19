import api from '../api.js'
import { defineStore } from 'pinia'

const useArticleStore =defineStore('articleModule', {
    state: () => ({
        categories: [],
        articles: [],
    }),
    actions: {
        async fetchCategories(){
            await api.get('/api/category/').then( response => {
                this.categories = response.data
            }
            )
        },

        async fetchAllArticles(){
            await api.get('/api/article/').then(response =>{
                this.articles = response.data
            })
        }
    },
    getters: {
        getAllArticles(state){
            return state.articles
        },
        getAllCategories(state){
            return state.categories
        }
    },
})

export default useArticleStore