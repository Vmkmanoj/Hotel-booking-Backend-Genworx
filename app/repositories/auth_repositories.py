
from sqlalchemy.orm import Session
from app.models.users import User
from app.models.roles import Role

class AuthRepository:
    def __init__(self, db : Session):
        self.db = db

    def get_user_by_email(self, email):

        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )
    
    def get_user_role(self,role_id):

        return (
            self.db.query(Role).filter(Role.id == role_id).first())
    

    def get_role_by_name(self, role_name):
        return self.db.query(Role).filter(Role.name == role_name).first()

