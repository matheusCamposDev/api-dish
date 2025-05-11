from flask import Blueprint, request
from http import HTTPStatus

from api_cardapio.serives.auth_service import UserService
from api_cardapio.custom_exceptions import (
    UserAlreadyExistsException,
    DatabaseException,
    Unauthorized,
)

service = UserService()

dish_bp = Blueprint("auth", __name__, url_prefix="/auth")


@dish_bp.route("/signin", methods=["POST"])
def sigin():
    data = request.get_json()
    try:
        token = service.login_user(data)
        return {"message": "Usuário autorizado!", "Token": token}, HTTPStatus.OK
    except Unauthorized:
        return {"message": "Usuário ou senha incorretos"}, HTTPStatus.UNAUTHORIZED


@dish_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    try:
        token = service.create_user(data)
        return {"message": "Usuário created!", "Token": token}, HTTPStatus.CREATED
    except UserAlreadyExistsException:
        return {"error": "Nome de usuário já existe."}, HTTPStatus.BAD_REQUEST
    except DatabaseException as e:
        return {"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        return {
            "error": "Unexpected error",
            "details": str(e),
        }, HTTPStatus.INTERNAL_SERVER_ERROR
