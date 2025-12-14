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
    DELETE_ARTICLE_BY_EMAIL_AND_PAGE_ID = """
        DELETE FROM articles
        WHERE user_email = $1 AND page_id = $2
    """


"""
Below queries are used to create the db tables -


CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email STRING NOT NULL UNIQUE,
    hashed_password STRING NOT NULL,
    created_at TIMESTAMP DEFAULT now()
);


CREATE TABLE IF NOT EXISTS articles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_email STRING NOT NULL,
    page_id INT NOT NULL,
    title STRING NOT NULL,
    summary STRING,
    url STRING,
    tags STRING[],
    created_at TIMESTAMP DEFAULT now(),

    UNIQUE (user_email, page_id)
);

"""
