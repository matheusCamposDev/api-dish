from api_cardapio.models.models import Dish, db
from flask import Blueprint, request, jsonify
from http import HTTPStatus
from dataclasses import asdict
from api_cardapio.serives.dish_service import DishService

dish_bp = Blueprint('dish', __name__, url_prefix='/dish')

@dish_bp.route('/', methods=['POST'])
def create_dish():
    data_request = request.get_json()
    DishService.create_dish(data_request)

    return jsonify({"Created" : data_request}), HTTPStatus.CREATED

# READ
@dish_bp.route('/<int:id>', methods=['GET'])
def get_dish(id):
    dish = db.get_or_404(Dish, id)

    return jsonify(asdict(dish)), HTTPStatus.OK

# READ ALL
@dish_bp.route('/', methods=['GET'])
def get_dishes():
    all_dishes = DishService.get_dishes()

    return jsonify({"dishes" : all_dishes}), HTTPStatus.OK

# UPDATE
@dish_bp.route('/<int:id>', methods=['PATCH'])
def update_dish(id):
    data_request = request.get_json()
    update_dish = DishService.update_dish(id, data_request)

    return jsonify(update_dish), HTTPStatus.OK

# DELETE
@dish_bp.route('/<int:id>', methods=['DELETE'])
def delete_dish(id):
    DishService.delete_dish(id)

    return jsonify({"message": "Dish deleted successfully"}), HTTPStatus.NO_CONTENT
