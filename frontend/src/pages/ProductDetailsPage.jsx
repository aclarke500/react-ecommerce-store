import { useParams, useNavigate } from "react-router-dom";
import { useCart } from "../store/CartContext";
import { useState, useEffect } from "react";
import CartButton from "../components/CartButton";
import Spinner from '../components/Spinner'
import "../styles/ProductDetailsPage.scss";
import { getProductFromId, getProductImageFromId } from "../backend/product";


export default function ProductDetailsPage() {
    const navigate = useNavigate();
    const { id } = useParams(); // Extract the 'id' parameter
    const { addToCart } = useCart();
    const [product, setProduct] = useState(false);
    const [isLoading, setIsLoading] = useState(true);
    const [imageSrc, setImageSrc] = useState(null);


    const search = () => {
        navigate('/'); // Replace '/new-url' with your target path
    };

    useEffect(() => {
        const fetchProduct = async () => {
            try {
                const productObjFromDatabase = await getProductFromId(id);
                setProduct(productObjFromDatabase);
            } catch (error) {
                console.error("Failed to fetch product:", error);
            } finally {
                setIsLoading(false)
                console.log(product)
            }
        };

        fetchProduct();
    }, [id]);

    useEffect(() => {
        async function fetchImage() {
            try {
                const imageUrl = await getProductImageFromId(id);
                setImageSrc(imageUrl);
            } catch (error) {
                console.error("Error fetching product image:", error);
            }
        }

        fetchImage();
    }, [id]);


    return <>

        <div className="cart-btn-container">
            <div className="empty-space"></div>
            <div className="cart-button-container" id='search' onClick={search}>
                <i className="fa-solid fa-magnifying-glass item" ></i>
            </div>
            <CartButton className="shopping-cart item" />
        </div>

        {isLoading && <div className="product-spinner-container">
            <Spinner className="spinner" />
            <h3>Fetching your product from our database...</h3>
        </div>
        }
        {!isLoading && <div className="product-details-page" >
            <div className="product-display-container">
                <div className="product-display">
                    <img
                        // src={product.image}
                        src={imageSrc}
                        alt={product.name}
                        className="product-image"
                    />
                    <h3 style={{ justifyContent: "flex-end", marginTop: "2rem" }}>{product.name}</h3>
                </div>
                <div className="product-meta-data">

                    <button
                        className="add-to-cart-button"
                        onClick={() => addToCart(product)}
                    >
                        Add to Cart 🛒
                    </button>

                    <h3>Price: ${product.price}</h3>
                    <p>{product.description}</p>
                    <p>Stock: {product.quantity}</p>
                    <p>Category: {product.category}</p>
                </div>
            </div>
        </div >
        }
    </>
}
