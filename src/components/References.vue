<template>
  <div class="references">
      <h3><b>References</b></h3>
      1. KEGG: new perspectives on genomes, pathways, diseases and drugs.
Kanehisa M, Furumichi M, Tanabe M, Sato Y, Morishima K.
Nucleic Acids Res. 2017 Jan 4;45(D1):D353-D361. doi: 10.1093/nar/gkw1092. Epub 2016 Nov 28.
<a href="https://pubmed.ncbi.nlm.nih.gov/27899662/">PMID: 27899662</a><br>
      2. The reactome pathway knowledgebase.
Jassal B, Matthews L, Viteri G, Gong C, Lorente P, Fabregat A, Sidiropoulos K, Cook J, Gillespie M, Haw R, Loney F, May B, Milacic M, Rothfels K, Sevilla C, Shamovsky V, Shorser S, Varusai T, Weiser J, Wu G, Stein L, Hermjakob H, D'Eustachio P.
Nucleic Acids Res. 2020 Jan 8;48(D1):D498-D503. doi: 10.1093/nar/gkz1031.
<a href="https://pubmed.ncbi.nlm.nih.gov/31691815/">PMID: 31691815</a><br>
      3. HMDB 4.0: the human metabolome database for 2018.
Wishart DS, Feunang YD, Marcu A, Guo AC, Liang K, Vázquez-Fresno R, Sajed T, Johnson D, Li C, Karu N, Sayeeda Z, Lo E, Assempour N, Berjanskii M, Singhal S, Arndt D, Liang Y, Badran H, Grant J, Serra-Cayuela A, Liu Y, Mandal R, Neveu V, Pon A, Knox C, Wilson M, Manach C, Scalbert A.
Nucleic Acids Res. 2018 Jan 4;46(D1):D608-D617. doi: 10.1093/nar/gkx1089.
<a href="https://pubmed.ncbi.nlm.nih.gov/29140435/">PMID: 29140435</a><br>
      4. The Molecular Signatures Database (MSigDB) hallmark gene set collection.
Liberzon A, Birger C, Thorvaldsdóttir H, Ghandi M, Mesirov JP, Tamayo P.
Cell Syst. 2015 Dec 23;1(6):417-425. doi: 10.1016/j.cels.2015.12.004.
<a href="https://pubmed.ncbi.nlm.nih.gov/26771021/">PMID: 26771021 </a><br>
  </div>
</template>

<script>
export default {
    name: 'References',
}
</script>

<style scoped>
    .references {
        background-color: #ffffff;
        padding: 20px 60px;
        margin: 20px auto 10px;
        font-size: small;
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
