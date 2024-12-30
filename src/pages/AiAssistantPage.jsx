import '../styles/AiAssistantPage.scss'
import '../components/Spinner'
import Spinner from '../components/Spinner'
import ProductList from '../components/ProductList';
import { useState, useMemo } from 'react';
import { queryRAG } from '../backend/rag';

export default function AiAssistantPage() {
    //  declare variables
    const [isLoading, setIsLoading] = useState(false);
    const [userQuery, setUserQuery] = useState("");
    const [products, setProducts] = useState(null);
    const showProducts = useMemo(() => {
        return !!(!isLoading && products && products.length);
    })

    // functions for updating state
    const getItems = async () => {
        setIsLoading(true);
        const response = await queryRAG(userQuery);
        setProducts(response);
        setIsLoading(false);

    }


    // html
    return <>
        {/* <p>{showProducts}</p> */}
        {!showProducts && <div>
            {!isLoading && <div className="content-box">
                <div className="ai-container">
                    <div className="centered-flex-cell heading">
                        <h2>Welcome to the Future</h2>
                    </div>
                    <div className="centered-flex-cell description">
                        <p>Need help finding what you want? Use our <b>AI Powered Assistant</b> to find what you're looking for!</p>
                    </div>
                    <div className="centered-flex-cell">
                        <input
                            placeholder="What would you like to search for?"
                            value={userQuery}
                            onChange={(e) => setUserQuery(e.target.value)}
                        >
                        </input>
                    </div>
                    <div className="centered-flex-cell">
                        <button onClick={() => { getItems() }}>Enter</button>
                    </div>
                </div>
            </div>
            }
            {isLoading &&
                <div className="content-box">
                    <div className="ai-container">
                        <Spinner ></Spinner>
                        <p>Our AI is hard at working fetching your items!</p>
                        <p>You searched for: {userQuery}</p>
                    </div>
                </div>
            }
        </div>}
        {showProducts && 
        <div className="product-list">
        <ProductList products={products} />
        </div>}
    </>
}