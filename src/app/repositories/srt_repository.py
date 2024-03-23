# repositories/srt_repository.py

from psycopg2 import IntegrityError
from sqlalchemy.orm import Session
from models.all_models import SRT, Tenancy
from schemas.srt_schema import SRTCreate, SRTUpdate
#Modify the get_srts function to add tenant_name from the tenant tab
class SRTRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_srt(self, srt_id: int) -> None:
        return self.db.query(SRT).filter(SRT.id == srt_id,SRT.is_active==True).first()


    def get_srts(self) -> list:
        return self.db.query(SRT).filter(SRT.is_active==True).all()  

    def create_srt(self, srt_data: SRTCreate, tenancy_id: int) -> SRT:
        existing_srt = self.db.query(SRT).filter(
            SRT.srt_name == srt_data.srt_name,
            SRT.tenancy_id == tenancy_id
        ).first()

        if existing_srt:
            return None

        db_srt = SRT(**srt_data.dict(), tenancy_id=tenancy_id)
        self.db.add(db_srt)
        
        try:
            self.db.commit()
            self.db.refresh(db_srt)
            return db_srt
        except IntegrityError:
            self.db.rollback()
            return None
    
    def get_srt_by_name_and_tenancy_id(self, srt_name: str, tenancy_id: int):
        return self.db.query(SRT).filter(
            SRT.srt_name == srt_name,
            SRT.tenancy_id == tenancy_id
        ).first()


    def update_srt(self, srt_id: int, srt: SRTUpdate):
        db_srt = self.db.query(SRT).filter(SRT.id == srt_id).first()
        if db_srt:
            # Check if the combination of srt_name and tenancy_id already exists
            existing_srt = self.get_srt_by_name_and_tenancy_id(srt.srt_name, db_srt.tenancy_id)
            if existing_srt and existing_srt.id != srt_id:
                return None  # Combination already exists, cannot update
            # Update the SRT
            for var, value in vars(srt).items():
                setattr(db_srt, var, value) if value else None
            self.db.commit()
            self.db.refresh(db_srt)
            return db_srt
        return None