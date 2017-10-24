<template>
    <div>
        <p v-if="loading">Loading...</p>
        <p v-if="error">{{ error }}</p>
        <div v-if="!loading && bot">
            <h3 v-if="!updating" @dblclick="updating = true">
                {{ bot.username }}
            </h3>
            <input v-else type="text" v-model="bot.username" @keyup.enter="update">
            <h3>{{ bot.created_at | datetime }}</h3>
        </div>
        <div v-if="lists">
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>URL</th>
                        <th>Created At</th>
                        <th>Member Count</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody v-for="l in lists" v-show="!l.chosen" :key="l.id">
                    <tr @click="select(l)">
                        <td>{{ l.name }}</td>
                        <td>{{ l.uri }}</td>
                        <td>{{ l.created_at | datetime }}</td>
                        <td>{{ l.member_count }}</td>
                        <td>
                            <button @click.stop="choose(l)">
                                <span class="fa fa-check"></span>
                            </button>
                        </td>
                    </tr>
                    <tr v-show="l.selected">
                        <td colspan="5">
                            <div v-for="status in l.statuses" :key="status.id">
                                @{{ status.user.screen_name }}
                                {{ status.text }}
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
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
            lists: null,
            updating: false,
            chosenLists: []
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

            Promise.all([
                this.$http.get(`/bots/${this.botId}`).then(response => {
                    this.bot = response.body;
                }),
                this.$http.get('/twitter-api/lists').then(response => {
                    this.lists = response.body.lists;
                })
            ]).then(() => {
                this.loading = false;
            }, response => {
                this.loading = false;
                this.error = response;
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
        },
        select(l) {
            this.$set(l, 'selected', !l.selected);

            if (!l.statuses) {
                this.$http.get('/twitter-api/lists/statuses', {
                    params: {
                        count: 5,
                        owner_id: l.user.id,
                        slug: l.slug
                    }
                }).then(response => {
                    this.$set(l, 'statuses', response.body.statuses);
                });
            }
        },
        choose(l) {
            this.$set(l, 'chosen', true);
            this.chosenLists.push(l);
        }
    }
}
</script>

<style scoped>
table {
    border-collapse: collapse;
    border-spacing: 0px;
    width: 100%;
}

table, th, td {
    padding: 5px;
}

th {
    border-bottom: 1px solid black;
}

td {
    border-top: 1px solid #ccc;
}

tbody > tr:hover {
    background-color: #eee;
}
</style>

