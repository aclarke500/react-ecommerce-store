import { useCart } from "../store/CartContext";
export default function CartPage() {
    const { cart, removeFromCart, cartTotal } = useCart();
  
    if (cart.length === 0) {
      return <h1 className="cart-page">Your cart is empty</h1>;
    }
  
    return (
      <div className="cart-page">
        <h1>Your Cart</h1>
        <ul className="cart-items">
          {cart.map((item) => (
            <li key={item.id}>
              <span className="cart-item-name">{item.name}</span>
              <div className="cart-item-details">
                <span>${item.price} x {item.quantity}</span>
                <button onClick={() => removeFromCart(item.id)}>Remove</button>
              </div>
            </li>
          ))}
        </ul>
        <div className="cart-total">
          Total: ${cartTotal.toFixed(2)}
        </div>
      </div>
    );
  }
  