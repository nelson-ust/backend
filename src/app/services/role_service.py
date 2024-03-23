from sqlalchemy.orm import Session
from repositories.role_repository import RoleRepository
from schemas.role_schema import UserRoleBase, UserRoleCreate, UserRole as UserRoleResponse
from typing import List, Optional

class RoleService:
    def __init__(self, session: Session):
        self.repository = RoleRepository(session)

    def get_role_by_id(self, role_id: int) -> Optional[UserRoleResponse]:
        return self.repository.get_role_by_id(role_id)

    def get_role_by_name(self, role_name: str) -> Optional[UserRoleResponse]:
        return self.repository.get_role_by_name(role_name)

    def get_all_roles(self) -> List[UserRoleResponse]:
        return self.repository.get_all_roles()

    def create_role(self, role_create: UserRoleCreate) -> UserRoleResponse:
        return self.repository.create_role(role_create)

    def update_role(self, role_id: int, role_update: UserRoleBase) -> Optional[UserRoleResponse]:
        return self.repository.update_role(role_id, role_update)

    def delete_role(self, role_id: int) -> bool:
        return self.repository.delete_role(role_id)
