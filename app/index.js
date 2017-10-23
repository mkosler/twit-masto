import Vue from 'vue';
import VueResource from 'vue-resource';
import VueRouter from 'vue-router';
import moment from 'moment';
import TTMApp from './components/ttm-app.vue';
import TTMBotNew from './components/bots/ttm-bot-new.vue';
import TTMBotList from './components/bots/ttm-bot-list.vue';
import TTMBotDetail from './components/bots/ttm-bot-detail.vue';
import TTMNavbar from './components/ttm-navbar.vue';

const BASE_API = '/api/v1';

Vue.use(VueResource);
Vue.use(VueRouter);

/*
 * Components
 */
Vue.component('ttm-navbar', TTMNavbar);

/*
 * Router
 */
const router = new VueRouter({
    mode: 'history',
    base: __dirname,
    routes: [
        { path: '/', component: TTMApp },
        { path: '/new', component: TTMBotNew },
        { path: '/bots', component: TTMBotList },
        {
            path: '/bots/:id',
            component: TTMBotDetail,
            props: (route) => {
                return {
                    botId: Number(route.params.id)
                };
            }
        }
    ]
});

/*
 * Filters
 */
Vue.filter('datetime', v => {
    if (!v) return;
    return moment(v).format('MMM Do YYYY, h:mm:ss A');
});

/*
 * Interceptors
 */
Vue.http.interceptors.push((req, next) => {
    if (!req.url.startsWith('http')) {
        req.url = BASE_API + req.url;
    }

    next();
});

new Vue({
    router,
    template: `
        <div id="app">
            <h1>TwitMasto</h1>
            <ttm-navbar></ttm-navbar>
            <router-view></router-view>
        </div>
    `
}).$mount('#app');