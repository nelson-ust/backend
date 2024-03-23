from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.role_schema import UserRoleBase, UserRoleCreate, UserRole as UserRoleResponse
from services.role_service import RoleService

#router = APIRouter(prefix="/roles", tags=["roles"])
router = APIRouter()

@router.get("/roles/", response_model=List[UserRoleResponse])
def get_all_roles(db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.get_all_roles()

@router.get("/roles/{role_id}", response_model=UserRoleResponse)
def get_role_by_id(role_id: int, db : Session = Depends(get_db)):
    role_service = RoleService(db)
    role = role_service.get_role_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.post("/roles/", response_model=UserRoleResponse, status_code=201)
def create_role(role_create: UserRoleCreate, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.create_role(role_create)

@router.put("/roles/{role_id}", response_model=UserRoleResponse)
def update_role(role_id: int, role_update: UserRoleBase, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    role = role_service.update_role(role_id, role_update)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    if not role_service.delete_role(role_id):
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted successfully"}
