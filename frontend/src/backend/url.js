const devUrlPrefix = 'http://localhost:5001/';
const prodUrlPrefix = 'https://react-rag-store.onrender.com/';

let isDev = false;
try{
    const env = import.meta.env.VITE_DEV;
    if (env == '1') isDev = true;
} catch{

}


let urlPrefix;

if (isDev) urlPrefix = devUrlPrefix;
else urlPrefix = prodUrlPrefix;

export default urlPrefix;
