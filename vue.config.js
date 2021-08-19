module.exports = {
    publicPath: process.env.NODE_ENV === 'development' 
      ? 'http://localhost:8080' 
      : 'https://calina01.u.hpc.mssm.edu/pathway_assessor/dist',
  };
  