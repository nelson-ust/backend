
#repositories/tenancy_repository.py
from typing import List
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session
from models.all_models import Tenancy
from schemas.tenancy_schema import TenancyCreate, TenancyUpdate

class TenancyRepository:
    def __init__(self, db: Session) ->None:
        self.db = db

    def create_tenancy(self,tenancy_data:TenancyCreate)->Tenancy:
        existing_tenancy = self.db.query(Tenancy).filter(
            Tenancy.tenant_name== tenancy_data.tenant_name
        ).first()
        if existing_tenancy:
            return None
        db_tenancy=Tenancy(**tenancy_data.dict())
        self.db.add(db_tenancy)

        try:
            self.db.commit()
            self.db.refresh(db_tenancy)
            return db_tenancy
        except IntegrityError:
            self.db.rollback()
            return None

    def get_tenancy(self, tenancy_id: int):
        return self.db.query(Tenancy).filter(Tenancy.id == tenancy_id, Tenancy.is_active == True).first()

    def get_tenancies(self, skip: int = 0, limit: int = 10) ->List:
        return self.db.query(Tenancy).filter(Tenancy.is_active == True).offset(skip).limit(limit).all()
   
    def get_tenancy_by_name(self, tenant_name: str):
        return self.db.query(Tenancy).filter(
            Tenancy.tenant_name == tenant_name
        ).first()

    def update_tenancy(self,tenancy_id:int,tenancy:TenancyUpdate):
        db_tenancy=self.db.query(Tenancy).filter(Tenancy.id==tenancy_id).first()
        if db_tenancy:
           # Check if the combination of srt_name and tenancy_id already exists 
           existing_tenancy=self.get_tenancy_by_name(tenancy.tenant_name)
           if existing_tenancy and existing_tenancy.id !=tenancy_id:
               return None  #Tenancy cannot be updated
           #Update the Tenancy
           for var,value in vars(tenancy).items():
               setattr(db_tenancy,var,value) if value else None
           self.db.commit()
           self.db.refresh(db_tenancy)
           return db_tenancy
        return None
    

    #Soft Delete
    def delete_tenancy(self, tenancy_id: int):
        db_tenancy = self.db.query(Tenancy).filter(Tenancy.id == tenancy_id, Tenancy.is_active == True).first()
        if db_tenancy:
            db_tenancy.is_active = False
            self.db.commit()
        return db_tenancy


