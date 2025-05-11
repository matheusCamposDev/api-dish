set -e

# Rodar db upgrade
echo "Applying database migrations..."
poetry run flask --app api_cardapio db upgrade

# Verificar se a variável $PORT está definida
if [ -z "$PORT" ]; then
  echo "Error: The PORT environment variable is not set!"
  exit 1
fi

# Iniciar o Gunicorn
echo "Starting Gunicorn..."
poetry run gunicorn api_cardapio:app --bind 0.0.0.0:$PORT
