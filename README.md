# WikiKeep

WikiKeep is a Python (FastAPI) web application that allows users to search Wikipedia articles using a keyword, save their favorite articles, and organize them with AI-generated category tags.

The application integrates with the Wikipedia API to fetch article data and uses Google Gemini Pro (via LangChain) to automatically generate relevant tags for each saved article. Users can view all their saved articles on a dedicated page and modify the generated category tags as needed.

The system includes authentication, follows REST API best practices, and is deployed using Render and CockroachDB.

## API Documentation

https://wikikeep.onrender.com/docs

## Getting started

Consider using `pipenv` to manage your project dependencies.

### Installation

1. Clone this repository:

```bash
https://github.com/Shreyansh-Agrawal/WikiKeep.git
```

2. Navigate to the below directory:

```bash
cd WikiKeep/backend/src
```

3. Install the requirements

```bash
python -m pip install -r requirements.txt
```

### Run the Application

Make sure to include a .env file in the `/backend` directory. Please check out the .env.example file for the environment variables required.

```bash
uvicorn app:app
```

## Database Schema
<img width="599" height="351" alt="Screenshot 2025-12-14 150210" src="https://github.com/user-attachments/assets/ca67256a-65b0-42b8-b82d-c9942bd22066" />
