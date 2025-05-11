from api_cardapio.models.models import Dish, db
from sqlalchemy.exc import NoResultFound


class DishService:
    @staticmethod
    def create_dish(dish: Dish):
        try:
            db.session.add(dish)
            db.session.commit()
            return dish
        except:
            db.session.rollback()
            raise

    @staticmethod
    def get_by_id(id):
        return db.session.execute(db.select(Dish).filter_by(id=id)).scalar_one()

    @staticmethod
    def get_dishes():
        try:
            dish = Dish.query.all()
            return dish
        except Exception as e:
            raise RuntimeError from e

    @staticmethod
    def update_dish(id, data):
        dish = db.session.execute(db.select(Dish).filter_by(id=id)).scalar_one()

        for key, value in data.items():
            if hasattr(dish, key):
                setattr(dish, key, value)

        db.session.commit()
        return dish

    @staticmethod
    def delete_dish(id):
        try:
            dish = db.session.execute(db.select(Dish).filter_by(id=id)).scalar_one()
            db.session.delete(dish)
            db.session.commit()
            return
        except Exception:
            db.session.rollback()
            raise
