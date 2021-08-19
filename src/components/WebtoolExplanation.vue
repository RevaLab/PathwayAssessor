<template>
  <div class="webtool-explanation">
    <div class="txt">
        The Inferred Pathway Activity Score makes probabilistic assessments of the observed overrepresentation of pathway genes expression levels in a given expression profile.
        This webtool that performs pathway enrichment analysis from gene expression
        data for several popular pathway databases, including KEGG(1), Reactome (2),
        the Human Metabolome Database (HMDB) and the Small Molecule Pathway Database(SMPDB)(3),
        and Hallmark gene sets from the Broad Institute(4). </div>
  </div>
</template>

<script>
export default {
    name: 'WebtoolExplanation',
}
</script>

<style scoped>
    .webtool-explanation {
        background-color: #416788;
        padding: 20px 60px;
        margin: 10px auto;
        font-weight: bold;
    }

    .txt {
        color: white;
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
