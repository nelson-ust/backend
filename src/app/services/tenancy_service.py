from sqlalchemy.orm import Session
from repositories.tenancy_repository import TenancyRepository
from schemas.tenancy_schema import TenancyCreate, TenancyUpdate


class TenancyService:

    def __init__(self, db: Session):
        self.db = db
        self.tenancy_repository = TenancyRepository(db)

    def create_tenancy(self, tenancy: TenancyCreate):
        return self.tenancy_repository.create_tenancy(tenancy)


    def get_tenancy(self, tenancy_id: int):
        return self.tenancy_repository.get_tenancy(tenancy_id)


    def get_tenancies(self, skip: int = 0, limit: int = 10):
        return self.tenancy_repository.get_tenancies( skip, limit)


    def update_tenancy(self, tenancy_id: int, tenancy: TenancyUpdate):
        return self.tenancy_repository.update_tenancy( tenancy_id, tenancy)


    def delete_tenancy(self, tenancy_id: int):
        return self.tenancy_repository.delete_tenancy(tenancy_id)
