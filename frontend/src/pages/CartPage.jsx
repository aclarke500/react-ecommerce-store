import { useCart } from "../store/CartContext";
// import "../styles/CartPage.scss"; // Assuming you have some CSS for styling

export default function CartPage() {
    const { products: cart, removeFromCart } = useCart(); // Adjust according to your CartContext

    // Calculate the cart total dynamically
    const cartTotal = cart.reduce((total, item) => total + item.price * item.quantity, 0);

    if (cart.length === 0) {
        return <h1 className="cart-page">Your cart is empty</h1>;
    }

    return (
        <div className="cart-page">
            <h1>Your Cart</h1>
            <ul className="cart-items">
                {cart.map((item) => (
                    <li key={item.id} className="cart-item">
                        <span className="cart-item-name">{item.name}</span>
                        <div className="cart-item-details">
                            <span>
                                ${item.price.toFixed(2)} x {item.quantity}
                            </span>
                            <button
                                className="remove-button"
                                onClick={() => removeFromCart(item.id)}
                            >
                                Remove
                            </button>
                        </div>
                    </li>
                ))}
            </ul>
            <div className="cart-total">
                <h3>Total: ${cartTotal.toFixed(2)}</h3>
            </div>
        </div>
    );
}
