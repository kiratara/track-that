
<template>
  <div class='div-scroll'>
    <div :key="post.id" v-for="post in posts">
      <PostItemComponent :post='post' :caller="caller" v-on:del-post="$emit('del-post', post.id)" v-on:update-status="update_status"/>
    </div>
 </div> 
</template>

<script>
import PostItemComponent from './PostItemComponent.vue';
export default {
  name: "PostListComponent",
  components: {
    PostItemComponent
  },
  props: ['posts', 'caller'],
  methods: {
    update_status(status, id){
      this.$emit('update-status', status, id)
    }
  }
}
</script>

<style scoped>
  .div-scroll{
    height: 20em;
    overflow-y: scroll;
  }
</style>