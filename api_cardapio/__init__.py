from flask_migrate import Migrate
from flask import Flask
from api_cardapio.models.models import db
from  flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL = 'https://api-dish.onrender.com/static/swagger.json',
    config= {
        'app_name': "Cardápio"
    }
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]

db.init_app(app)

migrate = Migrate()

migrate.init_app(app, db)

with app.app_context():
    db.create_all()

from api_cardapio.routes.dish import dish_bp

app.register_blueprint(dish_bp)
app.register_blueprint(swaggerui_blueprint)

if __name__ == "__main__":

    app.run(debug=True)
