from flask_migrate import Migrate
from flask import Flask
from api_cardapio.models.models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardapio.db'

db.init_app(app)

migrate = Migrate()

migrate.init_app(app, db)

with app.app_context():
    db.create_all()

from api_cardapio.routes.dish import dish_bp

app.register_blueprint(dish_bp)

if __name__ == "__main__":

    app.run(debug=True)
