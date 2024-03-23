from pydantic import BaseModel

class RequestTypeBase(BaseModel):
    request_type_name: str

class RequestTypeCreate(RequestTypeBase):
    pass

class RequestType(RequestTypeBase):
    id: int

    class Config:
        orm_mode = True
