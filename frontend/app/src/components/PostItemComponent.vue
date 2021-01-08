<template>
  <div class="post-item">
    <div v-if="caller === 'home' ">
      {{ post.role + " at " + post.company }}
      <button type="button" @click="$emit('del-post', post.id)" class="del"> &#9747;  </button>
      <button type="button"  v-if="post.status == 'new'" @click="$emit('update-status',  status='applied', post.id,)" class="update-status"> &#9745;</button>
    </div>

    <div class="update-posts" v-if="caller === 'update'">
      <p class="post-info"> {{ post.status }} </p>
      <p> &nbsp; for &nbsp; </p>
      <p class="post-info"> {{ post.role }} </p>
      <p>   &nbsp; at  &nbsp; </p>
      <p class="post-info"> {{ post.company  }}</P>
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
          Update status
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <li><a class="dropdown-item" @click="$emit('update-status',  status='new', post.id)" >New</a></li>
          <li><a class="dropdown-item" @click="$emit('update-status',  status='applied', post.id)" > Applied</a></li>
          <li><a class="dropdown-item" @click="$emit('update-status',  status='progress', post.id)" > In Progress</a></li>
          <li><a class="dropdown-item" @click="$emit('update-status',  status='rejected', post.id)" > Rejected</a></li>
        </ul>
      </div>
      <button type="button" @click="$emit('del-post', post.id)" class="del">Remove</button>
    </div>
  </div>

</template>

<script>
export default {
  name: "PostItem",
  props: ['post', 'caller'],
  methods: {

  }
}
</script>

<style scoped>

  button {
    float: right;
  }

  .post-item {
      color: black;
      padding: 10px;
      border-bottom: 1px #ccc dotted;
      text-align:left ;
      margin-bottom: 0 10px 10px 10px;
      border-bottom: none;
  }

  .del {
      background: none;
      color: rgb(5, 5, 5);
  }
  .del:hover{
    background: #f18f8f;
  }

  .update-status {
      background: none;
      /* font-size: large; */
      color: black;
  }  
  .update-status:hover{
      background: rgb(99, 192, 99);
  }

  .edit {
    background-color: rgb(94, 94, 245);
  }

  .dropdown {
    float: right;
  }

  .post-info {
    font-weight: bold;
  }

  p {
    display: inline-block;
  }


</style>