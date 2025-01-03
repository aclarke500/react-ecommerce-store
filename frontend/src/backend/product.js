/**
 * Gets the product object from the backend given an id
 * @param {Number} id id number corresponding to product
 * @returns {Object} product object
 */
export async function getProductFromId(id){
    const url = `http://localhost:5001/product/${id}`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const product = await response.json();
    return product;
}

/**
 * Fetches the product image from the backend given an id
 * @param {Number} id id number corresponding to the product
 * @returns {Promise<string>} Blob URL of the product image
 */
export async function getProductImageFromId(id) {
    const url = `http://localhost:5001/product_image/${id}`;
    
    const response = await fetch(url, {
        method: 'GET',
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const blob = await response.blob();
    return URL.createObjectURL(blob);
}

/**
 * Fetches all products from the backend
 * @returns {Promise<Array>} Array of product objects
 */
export async function getAllProducts() {
    const url = `http://localhost:5001/products`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const products = await response.json();
    return products;
}