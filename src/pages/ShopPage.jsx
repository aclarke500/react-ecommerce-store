import ProductCard from '../components/ProductCard'
import { useProducts } from '../store/ProductContext';
function ShopPage() {

const products = useProducts();

    return <div className="product-shop">
        <h1>Shop Products</h1>
        <div className="product-container">
            {products.map((product, index) => (
                <ProductCard key={index} product={product} />
            ))}
        </div>
    </div>

}

export default ShopPage;