import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import { ProductProvider } from './store/ProductContext';
import { CartProvider } from "./store/CartContext";
import HomePage from './pages/HomePage';
import ShopPage from './pages/ShopPage';
import ProductDetailsPage from './pages/ProductDetailsPage';
import CartPage from './pages/CartPage';

function App() {
  return (
    <CartProvider>
    <ProductProvider>
      <Router>
        <div className="navbar">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/ai-assistant" className="nav-link">AI Assistant</Link>
          <Link to="/shop" className="nav-link">Shop</Link>
          <Link to="/cart" className="nav-link">Cart</Link>
        </div>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/shop" element={<ShopPage />} />
          <Route path="/product/:id" element={<ProductDetailsPage />} />
          <Route path="/cart" element={<CartPage />} />
        </Routes>
      </Router>
    </ProductProvider>
    </CartProvider>


  );
}

export default App;
