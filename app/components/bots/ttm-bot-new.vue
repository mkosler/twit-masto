<template>
    <div>
        <form @submit.prevent>
            <fieldset>
                <legend>New Bot</legend>
                <label for="username">Username: </label>
                <input type="text" name="username" v-model="username" @keyup.enter="submit">
            </fieldset>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: null,
        };
    },
    methods: {
        submit() {
            this.$http.post('/bots', { username: this.username }).then(response => {
                this.$router.push(`/bots/${response.body.id}`);
            });
        }
    }
}
</script>
