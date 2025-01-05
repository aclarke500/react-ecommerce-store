import React, { createContext, useState, useContext } from 'react';

export const CartContext = createContext();

export const useCart = () => useContext(CartContext);

export function CartProvider({ children }) {
  const [products, setProducts] = useState([]);

  const addToCart = (product) => {
    setProducts((prevProducts) => {
      const newProducts = [...prevProducts];
      product.vector = null
      newProducts.push(product);
      console.log(products)
      return newProducts;

    });
  };

  const removeFromCart = (productId) => {
    setProducts((prevProducts) => {
      const newProducts = [];
      let foundProduct = false;

      prevProducts.forEach((product) => {
        if (product.id === productId && !foundProduct) {
          foundProduct = true; // Skip this product only once
        } else {
          newProducts.push(product); // Keep other products
        }
      });

      return newProducts;
    });
  };

  return (
    <CartContext.Provider value={{ products, setProducts, addToCart, removeFromCart }}>
      {children}
    </CartContext.Provider>
  );
}
