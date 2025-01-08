import '../styles/HomePage.scss';
import { useState, useEffect } from 'react';
import { queryRAG } from '../backend/rag';
import Spinner from '../components/Spinner';
import ProductCard from '../components/ProductCard';
import CartButton from '../components/CartButton';

export default function HomePage() {
  const [userSearchQuery, setUserSearchQuery] = useState("");
  const [products, setProducts] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [timeOfSubmission, setTimeOfSubmission] = useState(null);
  const [has10SecondsElapsed, setHas10SecondsElapsed] = useState(false);



  // functions for updating state
  const getItems = async () => {
    setIsLoading(true);
    setTimeOfSubmission(new Date());
    const response = await queryRAG(userSearchQuery);
    setProducts(response);
    setIsLoading(false);

  }
  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      getItems();
    }
  };


   // Periodically check if 10 seconds have passed since `timeOfSubmission`
   useEffect(() => {
    const interval = setInterval(() => {
        if (timeOfSubmission) {
            const now = new Date();
            const diffInSeconds = (now - timeOfSubmission) / 1000;
            setHas10SecondsElapsed(diffInSeconds >= 10);
        }
    }, 1000); // Check every second

    return () => clearInterval(interval); // Cleanup interval on unmount
}, [timeOfSubmission]);
  return <>
    <div className="home-page">

      <div className="ai-title">
        <div className="top-row">
          <div className="left-side"></div>
          <div className="middle">
            <h2>What can our SmartCart help you find today?</h2>
          </div>
          <div className="right-side"><CartButton /></div>
        </div>


        <input
          value={userSearchQuery}
          onChange={(e) => setUserSearchQuery(e.target.value)}
          onKeyDown={e => handleKeyDown(e)}
        ></input>
        <div className='instructions'>
          Describe what you're looking for in detail—whether it's specific, broad, or lengthy. Our AI will analyze your input and recommend the best products tailored just for you.
          <br /> We currently offer food, electronics, and pet supplies.
        </div>
        <br/>
        <button id="submit-button" onClick={getItems}>
          Send to AI
        </button>

      </div>
      <div className="bottom">
        <div className='spinner-container'>
          {isLoading && <>
            <Spinner />
            {has10SecondsElapsed && 
            <div className='slow-container'>
              <p className='slow'>Server taking a while to fetch your data? We're using free hosting and passing the savings onto you. We recommend refreshing and waiting a minute or two for the server to 'wake up'. Feel free to go grab a coffee while our server does the same. </p>
             <img src="coffee.png" alt="coffee pic" id="coffee-pic" />
              </div>

            }
          </>
          }

        </div>
        {/* this will be the relevant products */}
        {products && <div className="product-container">
          {products.map((product, index) => (
            <ProductCard key={index} product={product} className="card" />
          ))}
        </div>}
      </div>

    </div>
  </>
}
