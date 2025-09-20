from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.models.dicts import DictModel

class DictsRepository:
    @classmethod
    async def get_dict(cls,
                       dict_key:str,
                       session: SessionDep
                       ):
        query = (select(DictModel)
                 .filter(DictModel.dict_key == dict_key)
                 )
        result = await session.execute(query)
        dict = result.scalars().all()
        return dict