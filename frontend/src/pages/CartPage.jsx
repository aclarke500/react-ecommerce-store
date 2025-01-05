import React from 'react';
import { useCart } from '../store/CartContext';
import '../styles/CartPage.scss'; // Link the styles here

const CartComponent = () => {
  const { products, addToCart, removeFromCart } = useCart();

  const totalPrice = products.reduce((sum, product) => sum + product.price, 0);

  return (
    <div className="cart-container">
      <h1>Your Cart</h1>
      {products.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <ul className="cart-items">
          {products.map((product, index) => (
            <li key={index} className="cart-item">
              <span className="cart-item-name">{product.name}</span>
              <span className="cart-item-price">
                ${product.price.toFixed(2)}
              </span>
              <button
                className="remove-button"
                onClick={() => removeFromCart(product.id)}
              >
                Remove
              </button>
            </li>
          ))}
        </ul>
      )}
      <div className="cart-footer">
        <h3>Total Price: ${totalPrice.toFixed(2)}</h3>
      </div>
    </div>
  );
};

export default CartComponent;
