<template>
  <div class="home">
    <p class="welcome-msg">Hello, {{ userName }}</p>
    <h5 class="msg" v-if="newPosts.length !== 0">You have {{ newPosts.length }} posts you haven't applied to yet.</h5>
    <div class="grid-container">
      <div class="grid-item grid-item-info-box">
        <InfoBoxComponent v-bind:posts='posts'/>
      </div>
      <div class="grid-item grid-item-image-box">
        <h1> Skills</h1>
        <DoughnutChartComponent :chartUpdate="chartUpdate"/>
      </div>
      <div class="grid-item grid-item-new-posts">
          <div class="grid-item-header">
            <h1> New Posts </h1>
            <AddPostComponent class="add-btn" v-on:update-post="getAllPosts"/>
          </div>
          <div class="scroll-div">
            <div class="msg" v-if="newPosts.length === 0">
              <h4>Nice! You have applied to all postings.</h4>
              <p>Explore more.</p>
              </div>
            <ExploreComponent v-if="newPosts.length === 0"/>
            <PostListComponent :key="postListKey" :posts='newPosts' :caller='caller'  v-on:del-post="deletePost" v-on:update-status="updateStatusApplied"/>
          </div>
      </div>
      <div class="grid-item grid-item-in-progress">
        <h1> In Progress</h1>
        <PostListComponent :key="postListKey" :posts='progressPosts' :caller='caller'  v-on:del-post="deletePost" v-on:update-status="updateStatusApplied" v-if="progressPosts.length > 0"/>
        <div class="post-btns" v-if="progressPosts.length === 0">
          <h4>You do not have any application in progress right now.</h4>
          <button type="button" class="view-post-btn">
            <ul>
              <li><router-link to="/update">View All</router-link></li>
            </ul>
          </button>
        </div>
      </div>
      <div class="grid-item grid-item-place-holder">
        <p>placeholder</p>
        </div>
    </div>
    <ExploreComponent/>
  </div>
  
</template>

<script>
//components that make up the home page
import axios from 'axios';
import InfoBoxComponent from '../components/InfoboxComponent.vue';
import PostListComponent from '../components/PostListComponent.vue';
import AddPostComponent from '../components/AddPostComponent.vue';
import ExploreComponent from '../components/ExploreComponent.vue';
import DoughnutChartComponent from '../components/DoughnutChartComponent.vue';
export default {
  name: 'Home',
  components: {
    InfoBoxComponent,
    PostListComponent,
    AddPostComponent,
    ExploreComponent,
    DoughnutChartComponent,
  }, 
  data() {
    return {
      posts: [],
      caller:'home',
      postListKey: 0,
      statusNew: 'statusNew',
      statusProgress: 'statusProgress',
      chartUpdate: 0,
      userName: 'Emma',
    }
  },
  created: function () {
    // console.log(' Hello from  created() method in Home.vue: ');
    axios.get('http://127.0.0.1:5000/user')
    .then(res => console.log("REsponse value when getting user" + res))
    .catch(err => console.log(err));

    axios.get('http://127.0.0.1:5000/posts')
    .then(res => {
      this.posts = res.data.posts;
    })
    .catch(err => console.log(err));
  },
  computed: {
    newPosts: function () {
      if (this.posts && this.posts.length > 0){
        return this.posts.filter(post => post.status === "new");
      } else {
        return []
      }
    },
    progressPosts: function () {
      if (this.posts && this.posts.length > 0){
        return this.posts.filter(post => post.status === "progress");
      } else {
        return []
      }
    }
  },
  // methods 
  methods: {
    getAllPosts(){
      console.log("getAllPost called")
      axios.get('http://127.0.0.1:5000/posts')
      .then(res => {
        console.log("From the get all posts world");
        this.posts = res.data.posts;
        console.log(this.posts)
        this.chartUpdate += 1;
      })
      .catch(err => console.log(err));
     this.postListKey += 1;
      console.log("From the THEN world")
    },
    deletePost(id) {
      axios.delete(`http://127.0.0.1:5000/post/${id}`)
        .then( res => {
          console.log(res)
          this.posts = this.posts.filter(post => post.id !== id)
          this.chartUpdate += 1;
        })
        .catch(err => console.log(err));
    },
    updateStatusApplied(status, id){
      axios.patch(`http://127.0.0.1:5000/post/${id}`, {"status":status})
      .then(res => {
        console.log(res.data)
        this.getAllPosts()
      })
      .catch(err => console.log(err));
    }
  }
}
</script>

<style scoped>
  body{
    background-color: cadetblue;
  }
  .welcome-msg {
    color: black;
    margin-left: 14px;
    padding-bottom: none;
    text-align: left;
    font-size: xx-large;
    font-weight: bold;
  }
  .msg {
    margin-left: 14px;
    text-align: left;
    margin-top: none;
    font-size: 18px;
  }

  .view-post-btn {
    color: steelblue;
    float: center;
    margin: 2em;
  }

  .post-btns > *{
    display: inline-block;
  }

  .view-post-btn {
    box-shadow: 2px 2px 5px grey;
  }
  .view-post-btn:hover {
    box-shadow: 2px 2px 5px grey;
    background-color: rgb(212, 212, 216);
  }

  li a {
      display: block;
      text-align: center;
      text-decoration: none;
  }

  ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }

  .add-btn{
    float: right;
  }
  /* GRID */
  .grid-container {
    display: grid;
    grid-template-columns: 2fr 2fr;
    grid-auto-rows: minmax(100px, auto);
    grid-row-gap: 10px;
    grid-column-gap: 10px;
    padding: 10px;
    margin: 0px 4px 4px 4px;

  }

  .grid-item{
    border-radius: 6px;
    background: rgb(253, 253, 255);
  }
  .grid-item-header{
    overflow:auto;
    color:rgb(35, 35, 86);
  }
  .grid-item-header > h1 {
    float: left;
  }
  .add-btn{
    flex: right;
  }

  .grid-item > h1 {
    border-radius: 10px 10px 0 0;
    text-align: left;
    padding: 10px;
    color:rgb(35, 35, 86);
  }

  .grid-item-info-box{
    background: rgb(35, 35, 86);
    display: inline-block;
    grid-row-start: 1;
    grid-row-end:2;
  }
  .grid-item-image-box{
    grid-row-start: 2;
    grid-row-end: 4;
  }
  .grid-item-new-posts{
    grid-row-start: 1;
    grid-row-end: 3;
  }

  .grid-item-in-progress{
    grid-row-start: 3;
    grid-row-end: 5; 
  }

  .grid-item-place-holder{
    grid-row-start: 4;
    grid-row-end: 5;
  }
  .scroll-div{
    overflow-y: scroll;
  }

  img{
    height: 25em;
    padding-bottom: 15px;
    width: 30em;
  }
  .view-post-btn{
    float: right;
  }
</style>