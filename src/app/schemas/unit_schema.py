from pydantic import BaseModel
from typing import Optional


class UnitBase(BaseModel):
    unit_name: str
    dept_id: Optional[int]


class UnitCreate(UnitBase):
    pass


class Unit(UnitBase):
    id: int

    class Config:
        from_attributes=True
