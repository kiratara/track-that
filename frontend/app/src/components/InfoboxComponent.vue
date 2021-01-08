<template>
    <!-- Each card holds count of all posts applied to, in progress and those waiting on after applying to -->
    <div class="container">
    <div class="row infobox">
        <div class="col-sm">
            <div class="card">
                <a bind-on:href='https://www.google.com'>
                <div class="card-body">
                    <h5 class="card-title appliedTitle">Total Applied</h5>
                    <p class="infoCount"> {{ allAppliedCount.length }}</p>
                    <!-- <a href="#" class="btn btn-light"> View </a> -->
                </div>
                </a>
            </div>
        </div>
        <div class="col-sm">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title progressTitle">In Progress</h5>
                    <p class="infoCount"> {{ progressCount.length }}</p>
                    <!-- <a href="#" class="btn btn-light">View</a> -->
                </div>
            </div>
        </div>
        <!-- <div class="col-sm">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title waitingTitle">Waiting On</h5>
                    <p class="infoCount">{{ waitingCount.length }}</p>
                </div>
            </div>
        </div> -->
    </div>
    </div>
</template>

<script>
export default {
    name: 'InfoBoxComponent',
    components: {

    },
    props: ['posts'],
    data() {
        return {
            //
        }
    },
  computed: {
    allAppliedCount: function () {
      return this.posts.filter(post => post.status !== 'new');
    },
    progressCount: function (){
        return this.posts.filter(post => post.status === 'progress');
    },
    waitingCount: function(){
        return this.posts.filter(post => post.status === 'applied');       
    }
  },


}
</script>

<style scoped>
    .infobox {
        padding: 1em;
    }

    .infoCount {
        font-weight: bold;
        font-size: 3em;
        color: white;
    }

    .card {
        background: rgb(35, 35, 86);
        border: none;
        /* height: 10em;
        border-radius: 30px 30px;
        box-shadow: 6px 6px 10px grey;
        width: 20em;
        display: inline-block;
        float: none;  */
    }

    .card-title {
        padding: 0px;
        margin: 0px;
        color: white;
    }

    /* .appliedTitle {
        color: rgb(88, 142, 185);
    }

    .progressTitle {
        color: rgb(88, 142, 185);
    } */


</style>