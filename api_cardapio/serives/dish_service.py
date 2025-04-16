from api_cardapio.models.models import Dish, db


class DishService:
    @staticmethod
    def create_dish(data):
        dish = Dish(name=data['name'], description=data['description'], price=data['price'])
        db.session.add(dish)
        db.session.commit()
        return

    @staticmethod
    def get_dishes():
        results = db.session.execute(db.select(Dish)).scalars()

        return [{ 
            "id": result.id,
            "name": result.name,
            "description": result.description,
            "price": result.price,
        } for result in results]

    @staticmethod
    def update_dish(id, data):
        dish = db.get_or_404(Dish, id)

        for key, value in data.items():
            if hasattr(dish, key):
                setattr(dish, key, value)

        db.session.commit()
        return {
            "id": dish.id,
            "name": dish.name,
            "description": dish.description,
            "price": dish.price
        },

    @staticmethod
    def delete_dish(id):
        dish = db.get_or_404(Dish, id)
        db.session.delete(dish)
        db.session.commit()
        return 