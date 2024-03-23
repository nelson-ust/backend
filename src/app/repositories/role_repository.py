from sqlalchemy.orm import Session
from models.all_models import UserRole
from schemas.role_schema import UserRoleBase, UserRoleCreate, UserRole as UserRoleResponse
from typing import List, Optional

class RoleRepository:
    def __init__(self, db: Session):
        self.session = db

    def get_role_by_id(self, role_id: int) -> Optional[UserRoleResponse]:
        role = self.session.query(UserRole).filter(UserRole.id == role_id,UserRole.is_active==True).first()
        return role

    def get_role_by_name(self, role_name: str) -> Optional[UserRoleResponse]:
        role = self.session.query(UserRole).filter(UserRole.role_name == role_name,UserRole.is_active==True).first()
        return role

    def get_all_roles(self) -> List[UserRoleResponse]:
        roles = self.session.query(UserRole).filter(UserRole.is_active == True).all()
        return roles

    def create_role(self, role_create: UserRoleCreate) -> UserRoleResponse:
        role_data = role_create.dict()
        role = UserRole(**role_data)
        self.session.add(role)
        self.session.commit()
        self.session.refresh(role)
        return role

    def update_role(self, role_id: int, role_update: UserRoleBase) -> Optional[UserRoleResponse]:
        role = self.get_role_by_id(role_id)
        if role:
            role_data = role_update.dict(exclude_unset=True)
            for key, value in role_data.items():
                setattr(role, key, value)
            self.session.commit()
            self.session.refresh(role)
        return role

    def delete_role(self, role_id: int) -> bool:
        role = self.get_role_by_id(role_id)
        if role:
            role.is_active = False
            self.session.commit()
            return True
        return False
