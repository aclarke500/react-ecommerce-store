import React from 'react';
import { useContext } from 'react';
import '../styles/CartButton.scss';

export default function CartButton() {
    const numberOfItems = 0;

    // const cart = useContext(CartContext);
    return (
        <div className="cart-button-container">
            {numberOfItems && <div className="item-count">{numberOfItems}</div>}
            <img src="cart.png" alt="Cart Icon" />
        </div>
    );
}
