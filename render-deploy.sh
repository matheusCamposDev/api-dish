set -e

poetry run flask --app api_cardapio db upgrade
poetry run gunicorn api_cardapio:app -bind 0.0.0.0:$PORT