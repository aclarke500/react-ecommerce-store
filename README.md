
# E-Commerce Product Page with React

This is a full stack project meant to showcase/practice frontend and backend development, as well as some AI experience by employing a RAG. The main technologies used in this project are:
- **React**: I've always been a VueJS guy, so the primary motivation of this was to upskill my React capabilities.
- **Flask**: A Flask server is used to dish out the api and integrates with the React front end. It handles the RAG as well as serving products and images to the front end.
- **OpenAI**: The LLM used for the RAG and all sentence embeddings are done using OpenAI's respective tooling.
- **Render**: Continuous deploymnet is done using render for hosting the Flask API.
- **Numpy/sklearn**: Numpy is used to process the embeddings and sklearn is used to rank the embeddings.

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
   npm run dev
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
   python app.py
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
