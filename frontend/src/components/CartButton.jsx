import React, { useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { useCart } from '../store/CartContext'
import '../styles/CartButton.scss';

export default function CartButton() {

    const { products, addToCart, removeFromCart } = useCart();
    const numberOfItems = useMemo(() => products.length, [products]);
    const navigate = useNavigate();

    const handleNavigate = () => {
        navigate('/cart'); // Replace '/cart' with your actual cart route
    };

    return (
        <div className="cart-button-container" onClick={handleNavigate}>
            {numberOfItems > 0 && <div className="item-count">{numberOfItems}</div>}
            <img src="/cart.png" alt="Cart Icon" />
        </div>
    );
}
