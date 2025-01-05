import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import { ProductProvider } from './store/ProductContext';
import { CartProvider } from "./store/CartContext";
import HomePage from './pages/HomePage';
import ShopPage from './pages/ShopPage';
import ProductDetailsPage from './pages/ProductDetailsPage';
import CartPage from './pages/CartPage';
import AiAssistantPage from './pages/AiAssistantPage';

function App() {
  return (
    <CartProvider>
    <ProductProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/shop/:table_name?" element={<ShopPage />} />
          <Route path="/product/:id" element={<ProductDetailsPage />} />
          <Route path="/cart" element={<CartPage />} />
          <Route path="/ai-assistant" element={<AiAssistantPage />} />
        </Routes>
      </Router>
    </ProductProvider>
    </CartProvider>


  );
}

export default App;
