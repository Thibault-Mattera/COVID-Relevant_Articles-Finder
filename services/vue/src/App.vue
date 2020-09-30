<template>
<body>
  <div id="app">
    <div class="finder">
    <img alt="Virus Research" src="./assets/magnifying_glass.png">
    <Header />
    <br>
    <b-container class="bv-example-row" style="width:70%">
      <b-row>
        <AddTask v-on:add-task="addTask"/>
        <br>
      </b-row>
    </b-container>
    </div>
  </div>
  </body>
</template>

<script>
import Header from './components/Header.vue'
import AddTask from './components/AddTask.vue';

export default {
  name: 'App',
  data() {
    return {
      tasks: ''
  } 
  },
  components: {
    Header,
    AddTask
  },
  methods: {
    addTask(newTask) {
    this.tasks = [...this.tasks, newTask];
  }
}
}
</script>

<style>
body, html {
  height: 100%;
  margin: 0;
  background-image: url("https://techcrunch.com/wp-content/uploads/2020/03/GettyImages-1209679043.jpg");
  height: 100%;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 5px;
}
.finder {
  width: 700px;
  display: inline-block;
  margin-top: 10px;
  margin-bottom: 0px;
}
img {
  width: 100px;
  background-image: none;
  color: white;
  margin-bottom: 5px;
}
</style>
