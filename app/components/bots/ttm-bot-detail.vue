<template>
    <div>
        <p v-if="loading">Loading...</p>
        <p v-if="error">{{ error }}</p>
        <div v-if="bot">
            <h3 v-if="!updating" @dblclick="updating = true">
                {{ bot.username }}
            </h3>
            <input v-else type="text" v-model="bot.username" @keyup.enter="update">
            <h3>{{ bot.created_at | datetime }}</h3>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        botId: {
            type: Number,
            required: true
        },
        initialBot: Object
    },
    data() {
        return {
            loading: false,
            error: null,
            bot: null,
            updating: false
        }
    },
    created() {
        if (this.initialBot) this.bot = this.initialBot;
        else this.fetchData();
    },
    methods: {
        fetchData() {
            this.error = null;
            this.loading = true;
            this.bot = null;

            this.$http.get(`/bots/${this.botId}`).then(response => {
                this.bot = response.body;
                this.loading = false;
            }, response => {
                this.error = response.statusText;
                this.loading = false;
            });
        },
        update() {
            this.updating = false;
            this.loading = true;

            this.$http.put('/bots', this.bot).then(response => {
                this.loading = false;
            }, response => {
                this.loading = false;
                this.error = response.statusText;
            });
        }
    }
}
</script>
