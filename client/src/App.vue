<template>
  <div id="app">
    <HeaderLogo onClick="window.location.reload();"/>
    <BetaWarning />
    <Intro />
    <WebtoolExplanation />
    <Input />
  </div>
</template>

<script>
import Input from './components/Input.vue'
import BetaWarning from './components/BetaWarning.vue'
import HeaderLogo from './components/HeaderLogo.vue'
import Intro from './components/Intro.vue'
import WebtoolExplanation from './components/WebtoolExplanation.vue'

export default {
  name: 'app',
  components: {
    BetaWarning,
    HeaderLogo,
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
  max-width: 1000px;
  margin: 0 auto;
  /*margin-top: 60px;*/
}
</style>
