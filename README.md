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


## References

- Token Handling:
  https://github.com/Shreyansh-Agrawal/QuizApplication/blob/api/fastapi/src/utils/token_handler.py
- Password Hashing:
  https://pypi.org/project/bcrypt/
- LangChain - Gemini Integration:
  https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai


## Industry best practices used

1. Layered architecture to maintain clear separation of concerns
2. Logging and error handling
3. PII masking (e.g., email addresses) while logging
4. Pre-commit hooks to enforce code quality and consistency
5. Strong input validation at API boundaries
6. REST API principles for predictable and scalable endpoints
7. FastAPI background tasks for asynchronous processing (LLM tagging)
