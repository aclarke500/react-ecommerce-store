import ProductCard from '../components/ProductCard'
// import { useProducts } from '../store/ProductContext';
import { useState, useEffect } from 'react'
import { getAllProducts } from '../backend/product';
import { useParams } from 'react-router-dom';
import '../styles/ShopPage.scss'
import Spinner from '../components/Spinner';


export default function ShopPage() {
    const { tableName } = useParams();
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


    return <>
        {!products.length && <div className='shop-page-spinner'>
                <Spinner className='spinner'/>
                <p>Fetching our products from our server... hang tight!</p>
            </div>}
        {products.length && <div className="shop-page">
        <h1 className='title'> Shop Products</h1>
        <div className="product-container">
            {products.map((product, index) => (
                <ProductCard key={index} product={product} />
            ))}
        </div>
    </div>}
    </>
}
