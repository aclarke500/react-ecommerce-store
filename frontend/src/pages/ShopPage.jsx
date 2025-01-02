import ProductCard from '../components/ProductCard'
// import { useProducts } from '../store/ProductContext';
import {useState, useEffect} from 'react'
import { getAllProducts } from '../backend/product';
import '../styles/ShopPage.scss'

export default function ShopPage() {
    const [products, setProducts] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetchProducts() {
            try {
                const fetchedProducts = await getAllProducts();
                setProducts(fetchedProducts);
            } catch (err) {
                console.error("Error fetching products:", err);
                setError(err.message);
            }
        }

        fetchProducts();
    }, []); // Empty dependency array to run only once


    return <div className="shop-page">
        <h1 className='title'> Shop Products</h1>
        <div className="product-container">
            {products.map((product, index) => (
                <ProductCard key={index} product={product} />
            ))}
        </div>
    </div>

}
