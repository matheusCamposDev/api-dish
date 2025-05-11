#!/bin/sh
# Espera o banco ficar disponível
echo "Aguardando o banco estar pronto..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Banco disponível, rodando migrações..."
poetry run flask --app api_cardapio db upgrade

echo "Iniciando a API..."
poetry run flask --app api_cardapio run --host=0.0.0.0 --port=5000 --debug