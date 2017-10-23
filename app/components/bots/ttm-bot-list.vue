<template>
    <div>
        <p v-if="loading">Loading...</p>
        <p v-if="error">{{ error }}</p>
        <div v-if="bots">
            <section v-for="b in bots" :key="b.id">
                {{ b.id }}: <router-link :to="'/bots/' + b.id">{{ b.username }}</router-link>
            </section>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';

export default {
    data() {
        return {
            loading: false,
            bots: null,
            error: null
        };
    },
    created() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            this.error = null;
            this.bots = null;
            this.loading = true;

            this.$http.get('/bots').then(response => {
                this.bots = response.body.bots.sort((a, b) => {
                    return a.id - b.id;
                });
                this.loading = false;
            }, response => {
                this.loading = false;
                this.error = response.statusText;
            });
        }
    }
}
</script>
