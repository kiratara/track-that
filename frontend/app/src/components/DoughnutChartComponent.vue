<template>
    <div>
        <canvas id="donut-chart"></canvas>
    </div>
</template>
<script>
import axios from 'axios';
import Chart from 'chart.js';
export default {

    name: 'DonutChartComponent',
    props: ['chartUpdate'],
    created(){
        this.setData()
    },
    mounted() {
        // var source = "mounted"
        // this.getStatusCounts(source)
        this.createChart();
    },
    data() {
        return {
            posts : [],
        }
    },
    watch: {
        chartUpdate: function() {
            this.setData()
        }
    },
    computed: {
        statusCounts: function () {
            var counts = this.posts.reduce((c, { status: key }) => (c[key] = (c[key] || 0) + 1, c), {});
            // console.log("STATUS COUNTS")
            // console.log(Object.keys(counts));
            // console.log(Object.values(counts));
            return counts
        },
        chartDatas: function(){
            var data = Object.values(this.statusCounts)
            // console.log("data" + data)
            return data
        },
        chartLabel: function(){
            var data = Object.keys(this.statusCounts)
            // console.log("labels" + data)
            return data
        }
    },
    methods: {
        setData(){
            axios.get('http://127.0.0.1:5000/posts', {
                headers: {
                    Authorization: localStorage.getItem('token')
                }
            })
            .then(res => {
                // console.log(res.data)
                this.posts = res.data.posts;
                console.log("from created")
                console.log(this.posts)
                this.createChart();
            })
        .catch(err => console.log(err));
        },
        createChart() {
            const ctx = document.getElementById("donut-chart");
            console.log("here, below is value of chartLabel from createCharts method")
            const data = this.createDataSet()
            console.log(data.labels)
            console.log("prining from createchart - below is value of data from createDataSet method")
            console.log(data.labels)
            // const options = this.createOptions()
            new Chart(ctx, {
            type: "doughnut",
            data: data,
            options: {},
            });
        },

        createDataSet(){
            var counts = this.posts.reduce((c, { status: key }) => (c[key] = (c[key] || 0) + 1, c), {});
            var chartData = Object.values(counts)
            var chartLabel = Object.keys(counts)
            return {
                labels: chartLabel,
                datasets: [
                    {
                        data: chartData,//[4, 3, 4],
                        // data: this.chartDatas,
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],              
                    }
                ],
            } 
        },
        createOptions(){
            return {

            }
        }

    }
}
</script>

<style  scoped>

</style>