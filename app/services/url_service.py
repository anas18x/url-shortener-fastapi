from app.core.config import settings
from app.db.connection import pool
from app.db.queries import CREATE_URL, GET_URL_BY_CODE
from app.schemas.url import CreateURLRequest, URLResponse
from app.utils.short_code import generate_short_code
from psycopg.errors import UniqueViolation


def create_short_url(data: CreateURLRequest) -> URLResponse:
    while True:
        short_code = generate_short_code()

        try:
            with pool.connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        CREATE_URL,
                        (str(data.original_url), short_code),
                    )

                    row = cursor.fetchone()

        except UniqueViolation:
            continue

        break

    return URLResponse(
        id=row[0],
        original_url=row[1],
        short_code=row[2],
        short_url=f"{settings.base_url}/urls/{row[2]}",
        created_at=row[3],
    )



def get_original_url(short_code: str) -> str | None:
    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                GET_URL_BY_CODE,
                (short_code,),
            )

            row = cursor.fetchone()

    if not row:
        return None

    return row[0]