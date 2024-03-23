# from sqlalchemy.orm import Session
# from sqlalchemy.exc import IntegrityError
# from models.all_models import User, Employee, UserRole, Tenancy, Department, Unit
# from schemas.user_schema import UserCreate
# from sqlalchemy import func


# class UserRepository:
#     def __init__(self, db: Session):
#         self.db = db

#     def get_user_by_id(self, user_id: int):
#         return (
#             self.db.query(User, Employee, UserRole, Tenancy, Department, Unit)
#             .join(Employee, User.employee_id == Employee.id, isouter=True)
#             .join(UserRole, User.user_role_id == UserRole.id, isouter=True)
#             .join(Tenancy, Employee.tenancy_id == Tenancy.id, isouter=True)
#             .join(Department, Employee.dept_id == Department.id, isouter=True)
#             .join(Unit, Employee.unit_id == Unit.id, isouter=True)
#             .filter(User.id == user_id)
#             .first()
#         )

#     def get_user_by_name(self, user_name: str):
#         return (
#             self.db.query(User, Employee, UserRole, Tenancy, Department, Unit)
#             .join(Employee, User.employee_id == Employee.id, isouter=True)
#             .join(UserRole, User.user_role_id == UserRole.id, isouter=True)
#             .join(Tenancy, Employee.tenancy_id == Tenancy.id, isouter=True)
#             .join(Department, Employee.dept_id == Department.id, isouter=True)
#             .join(Unit, Employee.unit_id == Unit.id, isouter=True)
#             .filter(User.user_name == user_name)
#             .first()
#         )

#     def create_user(self, user: UserCreate):
#         existing_user = self.get_user_by_name(user.user_name)
#         if existing_user:
#             raise ValueError("User with this username already exists")
#         try:
#             db_user = User(**user.dict())
#             self.db.add(db_user)
#             self.db.commit()
#             self.db.refresh(db_user)
#             return db_user
#         except IntegrityError:
#             self.db.rollback()
#             raise ValueError("Error occurred while creating user, please try again")

#     def update_user(self, user_id: int, user_data: dict):
#         db_user = self.get_user_by_id(user_id)
#         if db_user:
#             for key, value in user_data.items():
#                 setattr(db_user, key, value)
#             self.db.commit()
#             self.db.refresh(db_user)
#         return db_user

#     def delete_user(self, user_id: int):
#         db_user = self.get_user_by_id(user_id)
#         if db_user:
#             db_user.is_active = False
#             self.db.commit()
#         return db_user


#repositories/user_re[opsitory.py
from sqlalchemy.orm import Session
from models.all_models import User, Employee, UserRole, Tenancy, Department, Unit
from schemas.user_schema import UserCreate
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from auth.security import get_password_hash,create_access_token
# from app.db.jwt_helper import  create_access_token

class UserRepository:

    def __init__(self,db:Session):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_name(db: Session, user_name: str):
        return db.query(User).filter(User.user_name == user_name).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate):
        # Check if the username already exists
        #existing_user = get_user_by_name(db, user.user_name)
        existing_user = self.db.query(User).filter(User.user_name == user.user_name).first()
        if existing_user:
            return None, "Username already exists"

        # Hash the password
        hashed_password = get_password_hash(user.password)

        # Create the user in the database
        db_user = User(user_name=user.user_name, hashed_password=hashed_password, user_role_id=user.user_role_id, employee_id=user.employee_id)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        # Generate JWT token
        access_token = create_access_token(data={"sub": db_user.user_name})
        return db_user, access_token


    def update_user_token(self, user_id: int, token: str):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.token = token
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user_data: dict):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            for key, value in user_data.items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    # def delete_user(db: Session, user_id: int):
    #     db_user = db.query(User).filter(User.id == user_id).first()
    #     if db_user:
    #         db.delete(db_user)
    #         db.commit()
    #         return db_user
    
    def delete_user(self, user_id: int):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.is_active = False
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def get_all_active_users(self):
        return (
                # self.db.query(User, Employee, UserRole, Tenancy, Department, Unit)
                self.db.query(User, Employee.employee_code,Employee.first_name,Employee.last_name,Employee.email, UserRole.role_name, Tenancy.tenant_name, Department.dept_name, Unit.unit_name)
                .join(Employee, User.employee_id == Employee.id, isouter=True)
                .join(UserRole, User.user_role_id == UserRole.id, isouter=True)
                .join(Tenancy, Employee.tenancy_id == Tenancy.id, isouter=True)
                .join(Department, Employee.dept_id == Department.id, isouter=True)
                .join(Unit, Employee.unit_id == Unit.id, isouter=True)
                .filter(User.is_active == True )
                .all()
            )

    def get_all_inactive_users(self):
        return (
                self.db.query(User, Employee.employee_code,Employee.first_name,Employee.last_name,Employee.email, UserRole.role_name, Tenancy.tenant_name, Department.dept_name, Unit.unit_name)
                .join(Employee, User.employee_id == Employee.id, isouter=True)
                .join(UserRole, User.user_role_id == UserRole.id, isouter=True)
                .join(Tenancy, Employee.tenancy_id == Tenancy.id, isouter=True)
                .join(Department, Employee.dept_id == Department.id, isouter=True)
                .join(Unit, Employee.unit_id == Unit.id, isouter=True)
                .filter(User.is_active == False)
                .all()
            )
    
    def get_user_email(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first().email

    def get_user_by_id(self, user_id: int):
        return (
                # self.db.query(User, Employee, UserRole, Tenancy, Department, Unit)
                self.db.query(User, Employee.employee_code,Employee.first_name,Employee.last_name,Employee.email, UserRole.role_name, Tenancy.tenant_name, Department.dept_name, Unit.unit_name)
                .join(Employee, User.employee_id == Employee.id, isouter=True)
                .join(UserRole, User.user_role_id == UserRole.id, isouter=True)
                .join(Tenancy, Employee.tenancy_id == Tenancy.id, isouter=True)
                .join(Department, Employee.dept_id == Department.id, isouter=True)
                .join(Unit, Employee.unit_id == Unit.id, isouter=True)
                .filter(User.id == user_id)
                .first()
            )

    def get_user_by_name(self, user_name: str):
        return (
                # self.db.query(User, Employee, UserRole, Tenancy, Department, Unit)
                self.db.query(User, Employee.employee_code,Employee.first_name,Employee.last_name,Employee.email, UserRole.role_name, Tenancy.tenant_name, Department.dept_name, Unit.unit_name)
                .join(Employee, User.employee_id == Employee.id, isouter=True)
                .join(UserRole, User.user_role_id == UserRole.id, isouter=True)
                .join(Tenancy, Employee.tenancy_id == Tenancy.id, isouter=True)
                .join(Department, Employee.dept_id == Department.id, isouter=True)
                .join(Unit, Employee.unit_id == Unit.id, isouter=True)
                .filter(User.user_name == user_name)
                .first()
            )