import { defineStore } from 'pinia'
import * as urls from '../urls.js'
import api from '../api.js'

const useTokenStore = defineStore('tokenStore', {
    state: () =>({
        isAuthenticated: false,
        userData: null,

    }),
    actions: {
        async login(payload) {
            await api.post(urls.OBTAIN_TOKEN_URL,
        { username: payload.username, password: payload.password }).then(
                response => {
                    if (response.data.access && response.data.refresh) {
                        localStorage.setItem('access', response.data.access);
                        localStorage.setItem('refresh', response.data.refresh);
                        }
                }
                ).catch( error =>{
                    return Promise.reject(error)
                    })

            if (String(localStorage.getItem('access'))) {
            await api.get(urls.PROTECTED_USER_DATA_URL).then(
                    response => {
                        this.userData = response.data;
                        this.isAuthenticated = true;
                    })
            }
        },
        async logout() {
            await api.post(
                    urls.BLACKLIST_TOKEN_URL,
                { refresh: localStorage.getItem('refresh') }
            ).then(response => {
            localStorage.setItem('access', '');
            localStorage.setItem('refresh', '');
            this.isAuthenticated = false;
            });
        }
    },
})

export default useTokenStore