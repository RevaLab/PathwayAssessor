<template>
  <div class="input-container">
    <div v-if="!sent">
        <div class="instructions">
            <u>Directions:</u><br>
            Upload a gene expression data file in tab-delimited format.
            The file should contain a matrix with genes in rows and samples in columns.
            Rows should be labeled with gene symbols.
            <div>
            Example input file can be downloaded <a v-on:click="downloadExample">here</a>.
            </div>
        </div>
        <div class="submitForm">
                <b-field label="Email">
                    <b-input type="email"
                        v-model="email">
                    </b-input>
                </b-field>
                <b-field 
                    type="is-warning"
                    :label="`Expression table (Max size: 50MB)`"
                >
                    <b-upload v-model="file" class="file-label">
                        <span class="file-cta">
                            <b-icon class="file-icon" icon="upload"></b-icon>
                            <span class="file-label">Upload</span>
                        </span>
                        <span class="file-name" v-if="file">
                            {{ file.name }}
                        </span>
                    </b-upload>
                    <b-button disabled class="filesize-button" :class="fileSizeValid ? 'is-success' : 'is-danger'" v-if="file">{{ fileSize }} MB</b-button>
                </b-field>
                <b-field label="Pathway database">
                    <b-select required v-model="database">
                        <option value="hallmark">Hallmark</option>
                        <option value="kegg">KEGG</option>
                        <option value="reactome">Reactome</option>
                        <option value="hmdb_smpdb">HMDB/SMPDB</option>
                    </b-select>
                </b-field>
        <b-button 
            @click="submitForm"
            expanded 
            rounded 
            type="is-warning"
            :disabled="!(email && email.length > 0 && emailIsValid && file && fileSizeValid)"
            :loading="loading"
        >
            <b>Submit</b>
        </b-button>
        </div>
    </div>
    <div v-if="sent">
        <div class="instructions" v-if="successful">
            <b>Thank you!</b><br><br>
            Your file has been submitted for analysis. <br>
            When the analysis is finished, you will receive an e-mail with the results attached as downloadable links.<br><br>

            If you have questions regarding your job, please send with this reference number: <b>{{ referenceNumber }}</b>
        </div>
        <div class="instructions" v-else>
            <b>There was an issue sending your file for analysis.<br>Please reach out to anna.calinawan@mssm.edu</b>
        </div>
        <b-button rounded @click="reset">Submit new analysis</b-button>
    </div>
  </div>
</template>

<script>
const apiRoot = 'https://calina01.u.hpc.mssm.edu/pathway_assessor/'

export default {
    name: 'Input',
    data() {
      return {
          database: 'hallmark',
          email: null,
          file: null,
          sent: false,
          successful: null,
          referenceNumber: 'notfound',
          res: null,
          loading: false,
      }
    },
    computed: {
        hashId() {
            return Date.now().toString(36)
        },
        fileSize() {
            return this.file ? this.file.size / 1000000 : ''
        },
        fileSizeValid() {
            return this.file && this.fileSize < 50
        },
        emailIsValid () {
            return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email)
        }
    },
    methods: {
        submitForm() {
            this.loading = true
            let formData = new FormData();
            formData.append('file', this.file)
            formData.append('email', this.email)
            formData.append('database', this.database)
            formData.append('hashId', this.hashId)

            this.axios.post(
                `${apiRoot}/submit`, 
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
            )
            .then(({ data }) => {
                this.res = data;
                this.successful = data.status === 'success';
                this.sent = true;
                this.referenceNumber = data.reference;
                this.loading = false
            })
            .catch((error) => {
                this.sent = true
                this.successful = false
                console.error('frontend error: ',error);
                this.loading = false
            });
        },
        reset() {
            this.file = null
            this.referenceNumber = 'notfound'
            this.res = null
            this.sent = false
            this.successful = null
            this.loading = false
        },
        downloadExample() {
            this.axios.get(
                `${apiRoot}/example`
            )
            .then((response) => {
                const url = window.URL.createObjectURL(new Blob([response.data]))
                const link = document.createElement('a')
                link.href = url
                link.setAttribute('download', 'example-pa-input.tsv')
                document.body.appendChild(link)
                link.click()
            }) 
            .catch((error) => {
                console.error('DOWNLOAD ERROR')
            });
        }
  }
}
</script>

<style scoped>
    .submitForm {
        padding: 1em;
        background-color: #ffffff;
        border: solid 3px #ffcc78;
    }

    .input-container {
        background-color: #E0E0E2;
        padding: 20px 60px;
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

    .filesize-button {
        margin-left: 10px;
    }
</style>
