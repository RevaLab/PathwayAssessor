<template>
  <div class="intro">
    Comparison of tumors by activities of molecular pathways can help nominate disease driver pathways,
      identify targets for therapeutic intervention, and determine clinically relevant subtypes
      and diagnostic biomarkers. We introduce a new method for calculating overrepresentation and underrepresentation
      scores to assess a pathway’s activation and suppression, respectively. The novelty of this approach is in
      independent assessment of overrepresentation and underrepresentation of pathway’s genes from both top
      and bottom of the ranked gene list of a given sample.
  </div>
</template>

<script>
export default {
    name: 'Intro',
}
</script>

<style scoped>
    .intro {
        background-color: #81D2C7;
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
