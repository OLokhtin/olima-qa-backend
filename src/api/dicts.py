from fastapi import APIRouter, HTTPException, status

from src.api.dependencies import SessionDep, AuthDep
from src.repository.dicts import DictsRepository

router = APIRouter()

@router.get("/api/dicts/{dict_key}",
            tags=["dict-controller"],
            summary="get_dict",
            dependencies=[AuthDep]
            )
async def get_dict(
        dict_key:str,
        session: SessionDep
):
    dict = await DictsRepository.get_dict(dict_key, session)
    if not dict:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Dict not found"
                            )
    return dict