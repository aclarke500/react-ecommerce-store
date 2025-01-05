import React, { createContext, useState, useContext } from 'react';

export const CartContext = createContext();
export const useCart = () => useContext(CartContext);
export function CartProvider({ children }) {
    const [products, setProducts] = useState([]);

    const addToCart = (product) => {
        setProducts((prevProducts) => {
            const existingProductIndex = prevProducts.findIndex((item) => item.id === product.id);

            if (existingProductIndex !== -1) {
                const updatedProducts = [...prevProducts];
                updatedProducts[existingProductIndex].quantity += 1;
                return updatedProducts;
            } else {
                return [...prevProducts, { ...product, quantity: 1 }];
            }
        });
    };

    const removeFromCart = (productId) => {
        setProducts((prevProducts) => {
            const existingProductIndex = prevProducts.findIndex((item) => item.id === productId);

            if (existingProductIndex !== -1) {
                const updatedProducts = [...prevProducts];
                const existingProduct = updatedProducts[existingProductIndex];

                if (existingProduct.quantity > 1) {
                    updatedProducts[existingProductIndex].quantity -= 1;
                    return updatedProducts;
                } else {
                    return updatedProducts.filter((item) => item.id !== productId);
                }
            }

            return prevProducts;
        });
    };

    return (
        <CartContext.Provider value={{ products, setProducts, addToCart, removeFromCart }}>
            {children}
        </CartContext.Provider>
    );
}
