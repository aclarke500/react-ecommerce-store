import { Link } from 'react-router-dom'
import '../App.css'
export default function ProductCard(props) {
    return <Link  to={`/product/${props.product.id}`} className="product-card">
    <div >
        <h2>{props.product.name}</h2>
        <h3>Price: ${props.product.price}</h3>
    </div>
    </Link>

}