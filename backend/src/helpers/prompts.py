class Prompts:
    GENERATE_CATEGORY_TAG_PROMPT = """
        You are an assistant that generates concise category tags.

        Given the article title and summary, return 2-3 relevant tags.
        Rules:
        - Tags must be short (1-2 words)
        - Use Title Case
        - Return ONLY a JSON array of strings
        - No explanation

        Title:
        {title}

        Summary:
        {summary}
    """
