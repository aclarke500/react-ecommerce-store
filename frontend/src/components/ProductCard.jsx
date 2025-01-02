import { useState, useEffect } from 'react'
import '../styles/ProductCard.scss';
import { getProductImageFromId } from '../backend/product';


export default function ProductCard(props) {
    const [imageSrc, setImageSrc] = useState(null);

    useEffect(() => {
            async function fetchImage() {
                try {
                    const imageUrl = await getProductImageFromId(props.product.id);
                    setImageSrc(imageUrl);
                } catch (error) {
                    console.error("Error fetching product image:", error);
                }
            }
    
            fetchImage();
        }, [props.product.id]);


    const handleClick = () => {
        window.location.href = `/product/${props.product.id}`;
    };

    return (
        <div onClick={handleClick} className="product-card">
            <img src={imageSrc}/>
            <div className="product-tag">
                <p className='name'>{props.product.name}</p>
                {/* <p className='description'>{props.product.description}</p> */}
                <p className='price'>${props.product.price}</p>
            </div>
        </div>
    );

}