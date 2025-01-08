import React from 'react';
import { useNavigate } from 'react-router-dom';

import { useCart } from '../store/CartContext';
import '../styles/CartPage.scss'; // Link the styles here

const CartComponent = () => {
  const { products, addToCart, removeFromCart } = useCart();

  const totalPrice = products.reduce((sum, product) => sum + product.price, 0);
  const navigate = useNavigate();
  const search = () => {
    navigate('/'); 
};

  return (
    <div className="cart-container">
      <div className="top-row">
        <div className="side"></div>
        <h1>Your Cart</h1>
        <div className="side">
          <div className="cart-button-container" id='search' onClick={search}>
            <i className="fa-solid fa-magnifying-glass item" ></i>
          </div>
        </div>
      </div>
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
