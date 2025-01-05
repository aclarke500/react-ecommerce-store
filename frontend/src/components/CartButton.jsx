import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/CartButton.scss';

export default function CartButton() {
    const numberOfItems = 5;
    const navigate = useNavigate();

    const handleNavigate = () => {
        navigate('/cart'); // Replace '/cart' with your actual cart route
    };

    return (
        <div className="cart-button-container" onClick={handleNavigate}>
            {numberOfItems > 0 && <div className="item-count">{numberOfItems}</div>}
            <img src="cart.png" alt="Cart Icon" />
        </div>
    );
}
