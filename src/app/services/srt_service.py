# services/srt_service.py

# from typing import List
# from sqlalchemy.orm import Session
# from repositories.srt_repository import SRTRepository
# from schemas.srt_schema import SRTCreate, SRTInDB

# class SRTService:
#     def __init__(self, db: Session):
#         self.db = db
#         self.srt_repository = SRTRepository(db)

#     def get_srt(self, srt_id: int):
#         return self.srt_repository.get_srt(srt_id)
    
#     def get_srts(self, tenancy_id: int, skip: int = 0, limit: int = 10) -> List[SRTInDB]:
#         srts_with_tenancy_name = self.srt_repository.get_srts(tenancy_id, skip, limit)
#         srts = [{"srt": srt[0], "tenant_name": srt[1]} for srt in srts_with_tenancy_name]
#         return srts

#     def create_srt(self, srt_data: SRTCreate, tenancy_id: int):
#         return self.srt_repository.create_srt(srt_data, tenancy_id)


# services/srt_service.py

from typing import List
from sqlalchemy.orm import Session
from repositories.srt_repository import SRTRepository
from schemas.srt_schema import SRTCreate, SRTInDB, SRTUpdate

class SRTService:
    def __init__(self, db: Session):
        self.db = db
        self.srt_repository = SRTRepository(db)

    def get_srt(self, srt_id: int):
        return self.srt_repository.get_srt(srt_id)
    
    def get_srts(self) -> List[SRTInDB]:
        return self.srt_repository.get_srts()

    def create_srt(self, srt_data: SRTCreate, tenancy_id: int):
        return self.srt_repository.create_srt(srt_data, tenancy_id)
    
    # def update_srt(self, srt_id: int, srt_update: SRTUpdate) -> SRTInDB:
    #     return self.srt_repository.update_srt(srt_id, srt_update)
    def update_srt(self, srt_id: int, srt:SRTUpdate):
        db_srt = self.srt_repository.update_srt(srt_id, srt)
        return db_srt
    
    def update_srt(self, srt_id: int, srt: SRTUpdate):
        db_srt = self.srt_repository.update_srt(srt_id, srt)
        return db_srt