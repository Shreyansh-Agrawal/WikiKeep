class Queries:
    GET_USER_ID_BY_EMAIL = "SELECT id FROM users WHERE email = $1"
    GET_USER_PASSWORD_BY_EMAIL = "SELECT hashed_password FROM users WHERE email = $1"
    GET_ARTICLE_BY_EMAIL = """
        SELECT page_id, title, summary, url, tags
        FROM articles
        WHERE user_email = $1
        ORDER BY created_at DESC
    """
    INSERT_USER = "INSERT INTO users (email, hashed_password) VALUES ($1, $2)"
    INSERT_ARTICLE_INFO = """
        INSERT INTO articles (user_email, page_id, title, summary, url)
        VALUES ($1, $2, $3, $4, $5)
    """
    UPDATE_ARTICLE_TAGS = """
        UPDATE articles
        SET tags = $1
        WHERE user_email = $2 AND page_id = $3
    """
