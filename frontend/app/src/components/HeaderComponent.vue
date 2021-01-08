<template>
    <header class="header"> 
        <ul>
            <li><router-link to="/">Home</router-link> </li>
            <li><router-link to="/update">All Posts</router-link> </li>
            <!-- <li><router-link to="/about">About</router-link> </li> -->
            <!-- <button class="float-right">Logout</button> -->
            <!-- <li class="float-right" @click="logoutUser"><router-link to="/">Logout</router-link> </li>  -->
        </ul>
    </header>
</template>

<script>
export default {
    name: 'HeaderComponent',
    methods: {
        // logoutUser(){
        //     localStorage.removeItem('token');
        // }
    }
}
</script>

<style scoped>
    /* .header{
        background: rgb(113, 135, 141);
        text-align: center;
        padding: 1px;        
    } */
/* 
    .header h1 {
        color:#fff;
    }

    .header a {
        color: #fff;
        padding-right: 5px;
        text-decoration: none;
    }

    #nav {
        padding: 10px;
    }

    #nav a {
        font-weight: bold;
        color:#fff;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    } */
    .header{
        background: #9fd0e9;
    }

    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color:rgb(253, 253, 253);
    }

    li {
        float: left;
    }

    li a {
        display: block;
        color:rgb(35, 35, 86);
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }

    li a:hover:not(.active) {
        background-color: rgb(35, 35, 86);
        color: white;
    }

    .active {
        background-color: #9c9cac;
    }

    .float-right {
        float: right;
    }
</style>