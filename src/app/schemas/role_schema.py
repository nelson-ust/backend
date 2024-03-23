from pydantic import BaseModel

class UserRoleBase(BaseModel):
    role_name: str

class UserRoleCreate(UserRoleBase):
    pass

class UserRole(UserRoleBase):
    id: int

    class Config:
        from_attributes=True



# from pydantic import BaseModel
# from typing import Optional

# class Tenancy(BaseModel):
#     tenant_name: str

# class SRTBase(BaseModel):
#     srt_name: str

# class SRTCreate(SRTBase):
#     pass

# class SRTUpdate(SRTBase):
#     srt_name: Optional[str]


# class SRT(BaseModel):
#     id: int
#     srt_name: str
#     tenancy_id: int

#     class Config:
#         from_attributes=True

# class SRTWithTenancy(BaseModel):
#     id: int
#     srt_name: str
#     tenancy: Optional[Tenancy]

#     class Config:
#         from_attributes = True

# class SRTInDB(BaseModel):
#     id: int
#     srt_name: str
#     tenancy_id: int

#     class Config:
#         from_attributes = True

# class SRTsResponse(BaseModel):
#     srt_list: list[SRTWithTenancy]  # Updated to use SRTWithTenancy

#     class Config:
#         from_attributes = True

# class SRTReturn(BaseModel):
#     message: str
#     srt: Optional[dict]

#     class Config:
#         from_attributes = True
