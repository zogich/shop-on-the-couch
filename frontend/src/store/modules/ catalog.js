import api from "../api";

const catalogModule = {
    state: () => ({
        categories: null
    }),
    mutations: {
        setCategories(state, catg){
            state.categories = catg;
        }
    },
    actions: {
        async fetchCategories(context){
            await api.get('/api/category/').then( response => {
                context.commit('setCategories', response.data)
            }
            )
        }
    },
    getters: {},
}

export default catalogModule