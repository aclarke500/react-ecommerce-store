const devUrlPrefix = 'http://localhost:5001/';
const prodUrlPrefix = 'https://react-rag-store.onrender.com/';

let urlPrefix;
const isDev = false;
if (isDev) urlPrefix = devUrlPrefix;
else urlPrefix = prodUrlPrefix;

export default urlPrefix;
