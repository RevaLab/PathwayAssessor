<template>
  <div class="input">
    <div v-if="!sent">
        <div class="instructions">
            <u>Directions:</u>
            Upload a gene expression data file in tab-delimited format.
            An example gene expression data file is available here.
            The file should contain a matrix with genes in rows and samples in columns.
            Rows should be labeled with gene symbols.
        </div>
        <div class="submitForm">
            <div class="fieldset">
                <label for="file">Expression table</label>
                <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
            </div>
            <div class="fieldset">
                <label for="email">Email</label>
                <input type="email" id="email" v-model="email"/>
            </div>
            <div class="fieldset">
                <label for="db">Pathway Database</label>
                <select id="db" v-model="db">
                    <option value="kegg">KEGG</option>
                    <option value="reactome">Reactome</option>
                    <option value="hmdb_smpdb">HMDB/SMPDB</option>
                    <option value="hallmark">Hallmark</option>
                </select>
            </div>
            <div class="fieldset">
                <label for="mode">
                    Mode
                </label>
                <select id="mode" v-model="mode">
                    <option value="geometric">geometric</option>
                    <option value="harmonic">harmonic</option>
                    <option value="min_p_val">min_p_val</option>
                </select>
            </div>
            <div class="fieldset">
                <label for="direction">Direction</label>
                <select id="direction" v-model="sortBy">
                    <option value="asc">ascending</option>
                    <option value="desc">descending</option>
                </select>
            </div>
            <div class="fieldset">
                <button v-on:click="submitFile()">Submit</button>
            </div>
        </div>
    </div>
    <div v-if="sent">
        <div class="instructions">
        <b>Thank you!</b>
        Your file has been sent to our server.
        When the analysis is finished, you will receive an e-mail with the results attached as a tab-separated file.
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'Input',
    data() {
      return {
          email: '',
          sent: false,
          sentSuccessful: false,
          db: 'kegg',
          sortBy: 'asc',
          mode: 'harmonic',
      }
    },
    methods: {
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
        },
        submitFile() {
            let formData = new FormData();
            formData.append('file', this.file);
            formData.append('email', this.email);
            formData.append('db', this.db);
            formData.append('sortBy', this.sortBy);
            formData.append('mode', this.mode);
            axios.post( 'http://localhost:5000/uploader',
              formData,
              {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then((res) => {
                this.sent = true;
                return res.data['file_id'];
            }).then((fileID) => {
                axios.get(`http://localhost:5000/process/${fileID}`)
                    .then((res) => {
                        console.log('RESULT FROM PROCESS: ', res)
                    })
                    .catch(() => {
                        console.log('FAILURE FROM PROCESS')
                    })
            })
            .catch(() => {
                console.log('FAILURE!!');
            });
        },
    }
}
</script>

<style scoped>
    .submitForm {
        padding: 1em;
        background-color: #ffffff;
    }

    .fieldset {
        /*background: white;*/
        font-weight: bold;
    }

    .fieldset label, button {
        margin: .2em .5em;
    }

    .fieldset label {
        font-size: .9em;
    }

    .input {
        background-color: #E0E0E2;
        padding: 20px 60px;
        /*font-weight: bold;*/
        margin: 10px auto;
    }

    .instructions {
        margin: 10px auto;
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
