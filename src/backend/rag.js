
export async function queryRAG(query){
    if (query == 'hi' || query =='est') return test;



    const url = "http://127.0.0.1:5001/query";
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query:query })
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    // console.log(data);
    return data;
}


const test = [
    {
      "availability": true,
      "description": "Fresh, crisp romaine lettuce.",
      "id": 16,
      "name": "Lettuce",
      "price": 1.29,
      "quantity": 90
    },
    {
      "availability": true,
      "description": "High-quality canned tuna in water.",
      "id": 48,
      "name": "Canned Tuna",
      "price": 2.79,
      "quantity": 120
    },
    {
      "availability": true,
      "description": "Convenient frozen mixed vegetables.",
      "id": 72,
      "name": "Frozen Mixed Vegetables",
      "price": 3.49,
      "quantity": 80
    },
    {
      "availability": true,
      "description": "Instant ramen noodles in a variety of flavors.",
      "id": 68,
      "name": "Pack of Ramen",
      "price": 3.99,
      "quantity": 100
    },
    {
      "availability": true,
      "description": "Fresh and crunchy green cabbage.",
      "id": 35,
      "name": "Cabbage",
      "price": 1.29,
      "quantity": 40
    },
    {
      "availability": true,
      "description": "Fresh, antioxidant-rich blueberries.",
      "id": 33,
      "name": "Blueberries",
      "price": 3.99,
      "quantity": 70
    },
    {
      "availability": true,
      "description": "Organic spinach leaves, ready to cook or eat raw.",
      "id": 12,
      "name": "Spinach",
      "price": 2.5,
      "quantity": 85
    },
    {
      "availability": true,
      "description": "Crunchy, organic carrots.",
      "id": 8,
      "name": "Carrots",
      "price": 1.99,
      "quantity": 100
    },
    {
      "availability": true,
      "description": "Crispy and tender frozen chicken nuggets.",
      "id": 76,
      "name": "Chicken Nuggets",
      "price": 6.49,
      "quantity": 70
    },
    {
      "availability": true,
      "description": "Lean ground beef for versatile cooking.",
      "id": 7,
      "name": "Ground Beef",
      "price": 7.99,
      "quantity": 70
    }
  ]