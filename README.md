# RAG General Store

A full-stack application for the RAG General Store that leverages a React-based frontend and a Flask-powered backend with LanceDB for vector database integration. This app serves as a modern, AI-powered e-commerce store.

---

## Directory Structure

- **frontend/**  
  Contains the React application for the store's user interface. Features include:
  - A product listing page.
  - AI-powered assistant using RAG (Retrieval-Augmented Generation) for intelligent search.
  - Routing and dynamic components for smooth navigation.

- **backend/**  
  Hosts the Flask server handling the API logic, database queries, and integration with LanceDB. Features include:
  - RESTful API endpoints for product management and retrieval.
  - Vector database queries for enhanced search functionality.

- **.gitignore**  
  Defines files and directories to exclude from version control, including:
  - \`node_modules/\` (frontend dependencies).
  - \`venv/\` (backend virtual environment).
  - Temporary build files and logs.

---

## Setup Instructions

### 1. Backend Setup
1. Navigate to the \`backend\` directory:
   \`\`\`bash
   cd backend
   \`\`\`
2. Create a virtual environment and install dependencies:
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   pip install -r requirements.txt
   \`\`\`
3. Start the Flask server:
   \`\`\`bash
   flask run --port=5001
   \`\`\`

### 2. Frontend Setup
1. Navigate to the \`frontend\` directory:
   \`\`\`bash
   cd frontend
   \`\`\`
2. Install dependencies:
   \`\`\`bash
   npm install
   \`\`\`
3. Start the React development server:
   \`\`\`bash
   npm start
   \`\`\`

---

## Usage
1. Visit the frontend at \`http://localhost:3000\` (default React port).
2. The Flask backend runs at \`http://127.0.0.1:5001\`.
3. Use the AI-powered assistant to search for products or browse the store.

---

## Tech Stack
- **Frontend**: React (Vite, React Router)
- **Backend**: Flask
- **Database**: LanceDB (vector database for RAG)
- **AI Integration**: Retrieval-Augmented Generation for intelligent product queries
