from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.schemas.url import CreateURLRequest, URLResponse
from app.services.url_service import (
    create_short_url,
    get_original_url,
)


router = APIRouter(
    prefix="/urls",
    tags=["URLs"],
)


@router.post(
    "",
    response_model=URLResponse,
    status_code=201,
)
def create_url(data: CreateURLRequest):
    return create_short_url(data)


@router.get("/{short_code}")
def resolve_url(short_code: str):
    original_url = get_original_url(short_code)

    if not original_url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found",
        )

    return RedirectResponse(
        url=original_url,
        status_code=307,
    )