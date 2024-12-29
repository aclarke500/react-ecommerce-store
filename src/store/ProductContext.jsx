import { createContext, useContext, useState } from 'react';

const ProductContext = createContext();

export const ProductProvider = ({ children }) => {
    const [products] = useState([
        {
            id: 1,
            name: 'Whimsical Widget',
            price: 29.99,
            description: 'A magical widget that adds whimsy to your daily tasks.',
            stock: 15,
            category: 'Tools',
            rating: 4.5,
            image: '/images/whimsical-widget.webp'
        },
        {
            id: 2,
            name: 'Giggly Gadget',
            price: 49.99,
            description: 'A gadget guaranteed to bring a smile to your face.',
            stock: 8,
            category: 'Electronics',
            rating: 4.7,
            image: '/images/giggly-gadget.webp'
        },
        {
            id: 3,
            name: 'Silly Sprocket',
            price: 19.99,
            description: 'A silly sprocket perfect for light-hearted tinkering.',
            stock: 25,
            category: 'Mechanical Parts',
            rating: 4.2,
            image: '/images/silly-sprocket.webp'
        },
        {
            id: 4,
            name: 'Quirky Contraption',
            price: 99.99,
            description: 'An advanced contraption for the curious and creative.',
            stock: 5,
            category: 'Innovations',
            rating: 4.8,
            image: '/images/quirky-contraption.webp'
        },
        {
            id: 5,
            name: 'Funky Gizmo',
            price: 39.99,
            description: 'A funky gizmo that combines fun and functionality.',
            stock: 20,
            category: 'Fun Stuff',
            rating: 4.6,
            image: '/images/funky-gizmo.webp'
        }
    ]);
    

    return (
        <ProductContext.Provider value={products}>
            {children}
        </ProductContext.Provider>
    );
};

export const useProducts = () => useContext(ProductContext);
