
# E-Commerce Product Page with React

This is a feature-rich e-commerce web application built with React, providing users with a seamless product browsing and shopping cart experience. The project demonstrates modern React development practices, including Context API for state management, responsive design, and reusable components.

---

## Features

- **AI-Powered Product Search**: Integrated RAG (Retrieval-Augmented Generation) to provide intelligent product search functionality.
- **Dynamic Product Listing**: View a variety of products with details such as name, price, and description.
- **Cart Page**: Displays selected products, total cost, and allows users to remove items.
- **Dark Theme**: Modern styling with a user-friendly layout optimized for dark mode.
- **Responsive Design**: Optimized for all screen sizes, from desktops to mobile devices.

---

## Technologies Used

- **Frontend**:
  - [React](https://reactjs.org/) - Component-based JavaScript library for building user interfaces.
  - [React Router](https://reactrouter.com/) - For handling client-side routing.
  - CSS for styling, including responsive design.

- **Backend**:
  - [Flask](https://flask.palletsprojects.com/) - Lightweight Python web framework.
  - LanceDB - Vector database for intelligent product queries.

- **State Management**:
  - React Context API for managing product and cart state.

---

## Getting Started

### Installation

#### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

#### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Start the Flask server:
   ```bash
   flask run --port=5001
   ```

---

## File Structure

```
ecommerce-react-app/
├── frontend/
│   ├── src/
│   │   ├── components/       # Reusable components (e.g., ProductCard, Spinner)
│   │   ├── pages/            # Page components (AiAssistantPage, ShopPage, CartPage)
│   │   ├── store/            # Contexts for state management
│   │   ├── App.js            # Main app entry point
│   │   └── index.js          # App initialization
├── backend/
│   ├── api.py                # Main Flask server
│   ├── utils/                # Helper utilities for database and queries
│   └── requirements.txt      # Backend dependencies
├── .gitignore                # Files and directories to ignore in Git
├── README.md                 # Project documentation
```

---

## Future Improvements

- **Enhanced AI Search**: Further optimize product search with advanced vector database queries.
- **User Authentication**: Enable user login for personalized shopping experiences.
- **Payment Integration**: Add a payment gateway for checkout functionality.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [LanceDB Documentation](https://lancedb.github.io/)

Happy coding!
