# from sqlalchemy.orm import Session
# from repositories.user_repository import UserRepository
# from schemas.user_schema import UserCreate


# class UserService:
#     def __init__(self, db: Session):
#         self.db = db
#         self.user_repository = UserRepository(db)

#     def get_user_by_id(self, user_id: int):
#         return self.user_repository.get_user_by_id(user_id)

#     def get_user_by_name(self, user_name: str):
#         return self.user_repository.get_user_by_name(user_name)

#     def create_user(self, user: UserCreate):
#         return self.user_repository.create_user(user)

#     def update_user(self, user_id: int, user_data: dict):
#         return self.user_repository.update_user(user_id, user_data)

#     def delete_user(self, user_id: int):
#         return self.user_repository.delete_user(user_id)

#     def get_all_active_users(self):
#         return self.user_repository.get_all_active_users()

#     def get_all_inactive_users(self):
#         return self.user_repository.get_all_inactive_users()


# #Services.user_service.py
# from sqlalchemy.orm import Session
# from repositories.user_repository import UserRepository
# from schemas.user_schema import UserCreate, User

# class UserService:
#     def __init__(self,db_session:Session):
#         self.db_session = db_session
#         self.user_repo = UserRepository(db_session)

#     def get_user(self, user_id: int):
#         return self.user_repo.get_user( user_id=user_id)

#     def get_user_by_name(self, user_name: str):
#         return self.user_repo.get_user_by_name( user_name=user_name)

#     def get_user_email(self,user_email:str):
#         return self.user_repo.get_user_email(user_email)
    
#     def get_users(self, skip: int = 0, limit: int = 100):
#             return self.user_repo.get_users( skip=skip, limit=limit)

#     def create_user(self, user: UserCreate):
#         db_user, access_token = self.user_repo.create_user( user=user)
#         return db_user, access_token

#     def update_user_token(self, user_id: int, token: str):
#         return self.user_repo.update_user_token(user_id=user_id, token=token)

#     def update_user(self, user_id: int, user_data: dict):
#         return self.user_repo.update_user( user_id=user_id, user_data=user_data)

#     def delete_user(self, user_id: int):
#         return self.user_repo.delete_user( user_id=user_id)

#     def get_all_active_users(self):
#         return self.user_repo.get_all_active_users()

#     def get_all_inactive_users(self):
#         return self.user_repo.get_all_inactive_users()

#     def get_user_by_id(self, user_id: int):
#         return self.user_repo.get_user_by_id( user_id)

#     def get_user_by_name(self, user_name: str):
#         return self.user_repo.get_user_by_name( user_name)


from sqlalchemy.orm import Session
from models.all_models import User
from schemas.user_schema import UserCreate, UserUpdate, UserLogin
from repositories.user_repository import UserRepository

class UserService:             
    def __init__(self, db: Session):
        # self.db = db
        self.user_repo = UserRepository(db)

    def authenticate_user(self, user_login: UserLogin):
        return self.user_repo.authenticate_user(user_login)

    def create_user(self, user: UserCreate, current_user: User):
        return self.user_repo.create_user(user, current_user)

    def update_user(self, user_id: int, user_data: UserUpdate, current_user: User):
        return self.user_repo.update_user(user_id, user_data, current_user)

    def delete_user(self, user_id: int, current_user: User):
        return self.user_repo.delete_user(user_id, current_user)

    def get_all_users(self, current_user: User):
        return self.user_repo.get_all_users(current_user)

    def get_active_users(self, current_user: User):
        return self.user_repo.get_active_users(current_user)

    def get_inactive_users(self, current_user: User):
        return self.user_repo.get_inactive_users(current_user)

    def update_user_token(self, user_id: int, token: str):
        return self.user_repo.update_user_token(user_id, token)
