<template>
    <nav>
        <ul>
            <li v-for="n in navs" :key="n.to">
                <router-link :to="n.to">{{ n.name }}</router-link>
            </li>
        </ul>
    </nav>
</template>

<script>
export default {
    data() {
        return {
            navs: [
                { to: "/", name: 'Home' },
                { to: '/new', name: 'New' },
                { to: '/bots', name: 'Bots' }
            ]
        };
    }
}
</script>
