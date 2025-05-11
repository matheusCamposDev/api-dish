from api_cardapio.models.models import Dish, db
from flask import Blueprint, request, jsonify
from http import HTTPStatus
from api_cardapio.serives.dish_service import DishService
from flask_jwt_extended import jwt_required
from api_cardapio.schemas.dish_schema import DishSchema, DishUpdateSchema
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound

dish_bp = Blueprint("dish", __name__, url_prefix="/dish")
service = DishService()
dish_schema = DishSchema()
dishes_schema = DishSchema(many=True)
dish_update_schema = DishUpdateSchema()


# CREATE
@dish_bp.route("/", methods=["POST"])
@jwt_required()
def create_dish():
    try:
        data_request = dish_schema.load(request.get_json())
        created_dish = service.create_dish(data_request)
        return jsonify(dish_schema.dump(created_dish)), HTTPStatus.CREATED
    except ValidationError as err:
        return jsonify(
            {"code": HTTPStatus.UNPROCESSABLE_ENTITY, "message": err.messages}
        )
    except Exception as e:
        return jsonify(
            {"code": HTTPStatus.BAD_REQUEST, "message": str(e)},
        )


# READ_BY_ID
@dish_bp.route("/<int:id>", methods=["GET"])
def get_dish(id):
    try:
        dish_by_id = service.get_by_id(id)
        return jsonify(dish_schema.dump(dish_by_id)), HTTPStatus.OK
    except NoResultFound:
        return (
            jsonify(
                {
                    "code": HTTPStatus.NOT_FOUND,
                    "message": f"Dish not found with ID {id}",
                }
            ),
            HTTPStatus.NOT_FOUND,
        )


# READ ALL
@dish_bp.route("/", methods=["GET"])
def get_dishes():
    try:
        all_dishes = service.get_dishes()
        return jsonify(dishes_schema.dump(all_dishes)), HTTPStatus.OK
    except Exception as e:
        return (
            jsonify({"code": HTTPStatus.INTERNAL_SERVER_ERROR, "message": str(e)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


# UPDATE
@dish_bp.route("/<int:id>", methods=["PATCH"])
def update_dish(id):
    try:
        json_data = request.get_json()
        data_request = dish_update_schema.load(json_data, partial=True)
        update_dish = service.update_dish(id, data_request)
        return jsonify(dish_schema.dump(update_dish)), HTTPStatus.OK
    except ValidationError as err:
        return (
            jsonify({"code": HTTPStatus.UNPROCESSABLE_ENTITY, "message": err.messages}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    except NoResultFound:
        return (
            jsonify(
                {
                    "code": HTTPStatus.NOT_FOUND,
                    "message": f"Dish not found with ID {id}",
                }
            ),
            HTTPStatus.NOT_FOUND,
        )
    except Exception as e:
        return (
            jsonify({"code": HTTPStatus.BAD_REQUEST, "message": str(e)}),
            HTTPStatus.BAD_REQUEST,
        )


# DELETE
@dish_bp.route("/<int:id>", methods=["DELETE"])
def delete_dish(id):
    try:
        service.delete_dish(id)
        return jsonify({"message": "Dish deleted successfully"}), HTTPStatus.NO_CONTENT
    except NoResultFound:
        return (
            jsonify(
                {
                    "code": HTTPStatus.NOT_FOUND,
                    "message": f"Dish not found with ID {id}",
                }
            ),
            HTTPStatus.NOT_FOUND,
        )
