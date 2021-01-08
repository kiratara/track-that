<template>
    <div>
        <!-- Button to Trigger modal -->
        <button type="button" class="add-post-btn"  data-bs-toggle="modal" data-bs-target="#addPostModal">Add Post</button>
        <!-- Modal -->
        <div class="modal fade" id="addPostModal" tabindex="-1" aria-labelledby="addPostModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="addPostModalLabel">Add new post.</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- Form -->
                    <div class="container">
                        <!-- <form @submit="postNewPost" method="post"> -->
                        <form>
                            <label for="role">Job Role</label>
                            <input type="text" id="role" name="jobRole" v-model="post.role" placeholder="Job Role">
                            <label for="company">Company Name</label>
                            <input type="text" id="company" name="company" v-model="post.company" placeholder="Company name..">
                            <label for="status">Status</label>
                            <select id="status" name="status" v-model="post.status">
                                <option value="new" >new</option>
                                <option value="applied" >applied</option>
                                <option value="progress" >in-progress</option>
                                <option value="rejected" >rejected</option>
                            </select>
                            <!-- <label for="url">Post URL</label>
                            <input type="text" id="url" name="url" v-model="post.url" placeholder="Post URL.."> -->
                            <!-- <input type="submit" value="Submit" data-bs-dismiss="modal"> -->
                            <button class="btn-success" data-bs-dismiss="modal" @click="postNewPost">Add</button>
                        </form>
                    </div>
                    <!-- end of Form -->
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'AddPostComponent',

    data (){
        return {
            // defining the data to be post
            post: {
                role: null,
                company: null,
                status: null,
                url: null,
            }
        }
    },
    computed: {
       
    },
    methods: {
        postNewPost(e){
            e.preventDefault();
            axios.post('http://127.0.0.1:5000/post', this.post)
            .then(res => {
                console.log(res);
                this.$emit('update-post');
            })
            .catch(err => console.log(err));
            
        },
    }
}
</script>

<style scoped>
    body {font-family: Arial, Helvetica, sans-serif;}
    * {box-sizing: border-box;}

    input[type=text], select, textarea {
        width: 100%;
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        margin-top: 6px;
        margin-bottom: 16px;
    resize: vertical;
    }

    input[type=date], select, textarea {
        width: 100%;
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        margin-top: 6px;
        margin-bottom: 16px;
        resize: vertical;
    }


    input[type=submit]:hover {
        background-color: #45a049;
    }

    .container {
    border-radius: 5px;
    background-color: #f2f2f2;
    }

    .add-post-btn {
        float: center;
        margin: 2em;
        background: rgb(14, 167, 238);
        color: white;
    }

    button  {
        color: rgb(240, 240, 245);
        box-shadow: 2px 2px 5px grey;
    }

    button:hover {
        background-color: rgb(212, 212, 216);
    }

</style>