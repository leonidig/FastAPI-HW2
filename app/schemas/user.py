from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserData(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Optional[int] = None
    name: str