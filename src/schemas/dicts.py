from pydantic import BaseModel

class DictScheme(BaseModel):
    status: int
    dict_key: str
    self_id: int
    value: str
    description: str