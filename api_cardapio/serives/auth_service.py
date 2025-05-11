from api_cardapio.models.models import User, db
from api_cardapio import bcrypt
from flask_jwt_extended import create_access_token
from api_cardapio.custom_exceptions import (
    UserAlreadyExistsException,
    DatabaseException,
    Unauthorized,
)


class UserService:

    def login_user(self, user_data):

        user = User.query.filter_by(username=user_data["username"]).first()

        check_password = bcrypt.check_password_hash(
            user.password,
            user_data["password"],
        )

        if not user or not check_password:
            raise Unauthorized("Usuário ou senha incorretos")

        access_token = create_access_token(identity=user_data["username"])

        return access_token

    def create_user(self, user_data):
        try:
            if db.session.query(User).filter_by(username=user_data["username"]).first():
                raise UserAlreadyExistsException("Usuário já existe")

            user = User(
                username=user_data["username"],
                password=(
                    bcrypt.generate_password_hash(user_data["password"]).decode("utf-8")
                ),
                role_id=(user_data["role_id"]),
            )

            db.session.add(user)
            db.session.commit()

            access_token = create_access_token(identity=user_data["username"])
            return {"access_token": access_token}
        except Exception:
            raise
        except Exception as e:
            db.session.rollback()
            raise DatabaseException(str(e))
