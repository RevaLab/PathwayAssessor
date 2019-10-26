<template>
  <div id="app">
    <Intro />
    <WebtoolExplanation />
    <Input />
  </div>
</template>

<script>
import Input from './components/Input.vue'
import Intro from './components/Intro.vue'
import WebtoolExplanation from './components/WebtoolExplanation.vue'

export default {
  name: 'app',
  components: {
    Input,
    Intro,
    WebtoolExplanation,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  /*margin-top: 60px;*/
}
</style>
