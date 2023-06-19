import api from "../api";

const articleModule = {
    state: () => ({
        categories: [],
        articles: []
    }),
    mutations: {
        setCategories(state, catg){
            state.categories = catg;
        },
        setArticles(state, articl){
            state.articles = articl;
        }
    },
    actions: {
        async fetchCategories(context){
            await api.get('/api/category/').then( response => {
                context.commit('setCategories', response.data)
            }
            )
        },

        async fetchAllArticles(context){
            await api.get('/api/article/').then(response =>{
                context.commit('setArticles', response.data)
            })
        }
    },
    getters: {},
}

export default articleModule