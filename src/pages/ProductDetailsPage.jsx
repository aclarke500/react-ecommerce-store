import { useParams } from "react-router-dom";
import { useProducts } from "../store/ProductContext";
import { useCart } from "../store/CartContext";
import { useState } from "react";

export default function ProductDetailsPage() {
    const { id } = useParams(); // Extract the 'id' parameter
    const { addToCart } = useCart();
    const product = useProducts().find(p => p.id == id);

    if (!product) {
        return <h1>Product not found</h1>;
    }

    const maxQuantity = Math.min(5, product.stock);
    const [selectedQuantity, setSelectedQuantity] = useState(1);
    const getProductWithQuantity = ()=>{
        product.quantity = selectedQuantity;
        return product;
    }

    return (
        <div className="product-details-page">
            <div className="product-display-container">
                <div className="product-display">
                    <img
                        src={product.image}
                        alt={product.name}
                        className="product-image"
                    />
                    <h3 style={{ justifyContent:"flex-end", marginTop:"2rem"}}>{product.name}</h3>
                </div>
                <div className="product-meta-data">
                    <select 
                        value={selectedQuantity} 
                        className="quantity-select" 
                        onChange={(e) => setSelectedQuantity(Number(e.target.value))}
                    >
                        {[...Array(maxQuantity).keys()].map(i => (
                            <option key={i + 1} value={i + 1}>Quantity: {i + 1}</option>
                        ))}
                    </select>
                    <button className="add-to-cart-button" onClick={() => addToCart(getProductWithQuantity())}>
                        Add to Cart 🛒
                    </button>
                    <h3>Price: ${product.price}</h3>
                    <p>{product.description}</p>
                    <p>Stock: {product.stock}</p>
                    <p>Category: {product.category}</p>
                    <p>Rating: {product.rating} ⭐</p>
                </div>
            </div>
        </div>
    );
}
