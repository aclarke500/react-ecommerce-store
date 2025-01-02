import '../styles/ProductList.scss'
import { useNavigate } from 'react-router-dom';

export default function ProductList(props){
    const navigate = useNavigate();

    const openProduct = (p)=>{navigate(`/product/${p.id}`)}

    return <>
    {/* <h1>Hello</h1> */}

    <div className="product-list-container">
        <h1 className="product-list-title">Browse our most relevant items</h1>
        <div className="product-header">
            <h2 className='name'>Name</h2>
            <h2 className='price'>Price</h2>
            <h2 className='description'>Description</h2>
        </div>
        {props.products.map((product, index) => (

            <div key={index} className="product"
                onClick={()=>{openProduct(product)}}
            >
                <h3 className='name cell'>{product.name}</h3>
                <p className='price cell'>${product.price}</p>
                <p className='description cell'>{product.description}</p>
            </div>

        ))}
    </div>

    </>
}