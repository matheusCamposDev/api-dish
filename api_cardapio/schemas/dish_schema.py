from api_cardapio import ma
from marshmallow import validates, ValidationError, fields
from api_cardapio.models.models import Dish


class DishSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dish
        load_instance = True

    @validates("price")
    def validate_price(self, value, **kwargs):
        if value < 0:
            raise ValidationError("Price must be greater than or equal to 0.")

    @validates("name")
    def validate_name(self, value, **kwargs):
        if not value.strip():
            raise ValidationError("The name of the dish cannot be empty.")

    @validates("description")
    def validate_description(self, value, **kwargs):
        if not value.strip():
            raise ValidationError("The description of the dish cannot be empty.")


class DishUpdateSchema(DishSchema):
    class Meta(DishSchema.Meta):
        load_instance = False
