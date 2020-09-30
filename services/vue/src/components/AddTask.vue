<template>
  <div class="container">
    <form class="myform" @submit="addTask">
      <b-form-textarea
      name="task"
      v-model="addTaskForm.task"
      placeholder="Ask a question about Coronavirus..."
      rows="2"
      max-rows="5"
      style="width:100%">
      </b-form-textarea>
    <br>
  
      <label for="range-2">Please select a number of articles to display:</label>
      <b-form-input id="range-2" v-model="value" type="range" min="1" max="10" step="1" style="width:80%"></b-form-input>
      <p class="mt-2">Number of article(s): {{ value }}</p>

    <b-button 
        block variant="primary"
        type="submit"
        style="width:100%">
        Search for articles
    </b-button>

    <br>
    <p v-if="currentTask.length">
      Your question: {{currentTask}}
    </p>
    <p v-if="loading">
    <img alt="progress gif" src="../assets/progress.gif" width="100">
    </p>
      <b-list-group v-if="results.length">
        <b-list-group-item
            v-for="(item,index) in results" 
            :key="index"
            :class="[selectedIndex === index ? 'selected' : '' ]"
            :href="item.link" target="_blank"
            >
            {{item.title}}
        </b-list-group-item>
      </b-list-group>  
    <br>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'AddTask',
  data() {
    return {
      task: '',
      value: '2',
      results: [],
      addTaskForm: {
        task: ''
      },
      currentTask: '',
      loading: false,
    };
  },
  methods: {
    getTask() {
      const path = 'http://localhost:5000/task';
      axios.get(path)
        .then((response) => {
          this.task = response.data.task;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    updateTask(newTask) {
      const path = 'http://localhost:5000/task'
      axios.post(path, newTask)
      .then(() => {
        this.getTask();
      })
      .catch((error) => {
     // eslint-disable-next-line
          console.log(error);
          this.getTask();
        });
    },
    getResults() {
      const path = 'http://localhost:5000/articles';
      axios.get(path)
        .then((res) => {
          this.results = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.$emit('new-result', this.results);
    },
    initForm() {
      this.addTaskForm.task = '' ;
      this.loading = false;
    },
    addTask(e) {
      e.preventDefault();
      this.results=[]
      this.currentTask=this.addTaskForm.task
      this.loading=true;
      const newTask = {
        task: this.addTaskForm.task,
        numberArticles: this.value
      }
      this.updateTask(newTask);
      this.$emit('add-task', newTask);
      setTimeout(function () { this.getResults() }.bind(this), this.value*2000);
      setTimeout(function () { this.initForm() }.bind(this), this.value*2000);
    }
  },
}  
</script>


<style scoped>
    .container {
      margin: 0 auto;
      display: flex;
      justify-content: center;
    }
    .myform {
      display: inline-block;
    }
    .list-group-item:hover {
    background: rgba(211, 211, 211, 1);
    color: rgb(0, 60, 255);
    cursor: pointer;
    }
</style>

