<template>
  <div class="beta-warning">
    Please note that this web portal is still in alpha mode. To report bugs, please e-mail anna.calinwan@mssm.edu or submit a pull request to github.com/annapamma/PathwayAssessor.
  </div>
</template>

<script>
export default {
    name: 'BetaWarning',
}
</script>

<style scoped>
    .beta-warning {
        background-color: #ffcc78;
        padding: 20px 60px;
        font-weight: bold;
        margin: 20px auto 10px;
    }

h3 {
  margin: 10px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
