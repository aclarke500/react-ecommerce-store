import '../styles/HomePage.scss';
import { useNavigate } from 'react-router-dom';

export default function HomePage() {
  const categories = [
    { name: 'Food and Produce', description: 'Fresh and organic food items', tableName:'food' },
    { name: 'Electronics and Technology', description: 'Latest gadgets and devices', tableName:'electronics' },
    { name: 'Pet Supplies', description: 'Everything your pet needs' , tableName:'pet_supplies'}
  ];
    // const categories = ['Food and Produce', 'Electronics and Technology', 'Pet Supplies'];
  const navigate = useNavigate();
  const open = (category)=>{
      navigate(`/shop/${category.tableName}`)
    }
  const openAiPage = ()=>{
      navigate('/ai-assistant/');
  }

    return <div className="home-page">
      <div className="welcome-cell">
      <div className='home-title'>Welcome to Shop Cart AI</div>
      <img src="logo.png" alt="egg" />
      </div>

      <div className="category-container">
        <p className='category-title'>Check out our different categories or try out our <br/><u className='ai-link' onClick={()=>openAiPage()}><strong><span>AI Assistant</span></strong></u></p>
        <div className="category-row">
        {categories.map((category, index) => (
          <div key={index} className="category" onClick={()=>open(category)}>
            <div className="name">{category.name}</div>
            
          </div>
        ))}
    </div>
      </div>
      
    </div>
  }
  
