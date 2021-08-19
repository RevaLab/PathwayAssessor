<template>
  <div id="app">
    <HeaderLogo onClick="window.location.reload();"/>
    <BetaWarning />
    <Intro />
    <WebtoolExplanation />
    <Input />
    <references />
  </div>
</template>

<script>
import BetaWarning from './components/BetaWarning.vue'
import HeaderLogo from './components/HeaderLogo.vue'
import Input from './components/Input.vue'
import Intro from './components/Intro.vue'
import References from './components/References.vue'
import WebtoolExplanation from './components/WebtoolExplanation.vue'


export default {
  name: 'App',
  components: {
    BetaWarning,
    HeaderLogo,
    Input,
    Intro,
    References,
    WebtoolExplanation,
  },
}
</script>
,
    References
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 1000px;
  margin: 0 auto;
}
</style>
