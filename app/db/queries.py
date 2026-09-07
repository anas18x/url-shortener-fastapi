CREATE_URL = """
    INSERT INTO urls (original_url, short_code)
    VALUES (%s, %s)
    RETURNING id, original_url, short_code, created_at;
"""


GET_URL_BY_CODE = """
    SELECT original_url
    FROM urls
    WHERE short_code = %s;
"""