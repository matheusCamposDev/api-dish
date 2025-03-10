from flask_migrate import Migrate
from flask import Flask
from api_cardapio.models.models import db
from  flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config= {
        'app_name': "Cardápio"
    }
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardapio.db'

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
