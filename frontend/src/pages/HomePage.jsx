import '../styles/HomePage.scss';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { queryRAG } from '../backend/rag';
import Spinner from '../components/Spinner';
import ProductCard from '../components/ProductCard';
import CartButton from '../components/CartButton';

export default function HomePage() {
  const [userSearchQuery, setUserSearchQuery] = useState("");
  const [products, setProducts] = useState(null);
  const [isLoading, setIsLoading] = useState(false);


  // functions for updating state
  const getItems = async () => {
    setIsLoading(true);
    const response = await queryRAG(userSearchQuery);
    setProducts(response);
    setIsLoading(false);

  }
  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      getItems();
    }
  };

  return <>
    <div className="home-page">
      {/* this will be nothing */}

      {/* this will be the ai text box */}

      {/* organized as a column */}
    <CartButton/>
      <div className="ai-title">

        <h2>What can our SmartCart help you find today?</h2>
        <textarea
          name=""
          id=""
          // placeholder='Enter to start searching!'
          value={userSearchQuery}
          onChange={(e) => setUserSearchQuery(e.target.value)}
          onKeyDown={e => handleKeyDown(e)}
        ></textarea>
        <div className='instructions'>
          Describe what you're looking for in detail—whether it's specific, broad, or lengthy. Our AI will analyze your input and recommend the best products tailored just for you.
        </div>

      </div>
  <div className="bottom"></div>
  {isLoading && <Spinner/>}
      {/* this will be the relevant products */}
      {products && <div className="product-container">
        {products.map((product, index) => (
          <ProductCard key={index} product={product} className="card" />
        ))}
      </div>}

    </div>
  </>
}
