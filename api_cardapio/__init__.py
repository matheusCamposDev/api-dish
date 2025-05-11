from flask_migrate import Migrate
from flask import Flask
from api_cardapio.models.models import db

import os
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)


SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.yaml"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Menu Dish",
        "persistAuthorization": True,
    },
)


# Setup the Flask-JWT-Extended extension
jwt = JWTManager()
bcrypt = Bcrypt()
ma = Marshmallow()

app.config.from_object(f"api_cardapio.config.{os.getenv('FLASK_ENV').title()}Config")

migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
bcrypt.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()

from api_cardapio.controllers import dish
from api_cardapio.controllers import auth

app.register_blueprint(dish.dish_bp)
app.register_blueprint(auth.dish_bp)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":

    app.run(debug=False)
