set -e

poetry run flask --app api_cardapio db upgrade
poetry run gunicorn -b 0.0.0.0:$PORT api_cardapio:app