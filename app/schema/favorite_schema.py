from pydantic import BaseModel


class FavoriteResponse(BaseModel):
    success: bool
    message: str