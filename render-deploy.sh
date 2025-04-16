set -e

poetry run flask --app api_cardapio db upgrade
gunicorn -b 0.0.0.0:10000 api_cardapio:app