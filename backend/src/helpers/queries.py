class Queries:
    GET_USER_ID_BY_EMAIL = "SELECT id FROM users WHERE email = $1"
    GET_USER_CREDENTIALS_BY_EMAIL = (
        "SELECT id, hashed_password FROM users WHERE email = $1"
    )
    INSERT_USER = "INSERT INTO users (email, hashed_password) VALUES ($1, $2)"
