# DishAPI ![versão](https://img.shields.io/badge/version-1.0.0-blue)

- API de menu de cardápios com autenticação e autorização de usuários para cadastrar um novo prato.

# Descrição

Esta API permite o gerenciamento de um cardápio, onde é possível criar, listar, atualizar e deletar pratos. A criação de novos pratos está protegida por autenticação via JWT e só é permitida para usuários autenticados.
A autenticação é realizada por meio dos endpoints `/auth/signup` ou `/auth/sigin` que retorna um token, garantindo que apenas usuários autorizados possam realizar criações no cardápio.

# Technologies Used | Tecnologias usadas

- **[Python 3.11](https://www.python.org/)**
- **[Flask](https://flask.palletsprojects.com/)** – Microframework web
- **[SQLAlchemy](https://www.sqlalchemy.org/)** – ORM para banco de dados relacional
- **[Flask-Migrate](https://flask-migrate.readthedocs.io/)** – Controle de migrações
- **[Marshmallow](https://marshmallow.readthedocs.io/)** – Serialização e validação de dados
- **[Swagger (Flask swagger ui)](https://pypi.org/project/flask-swagger-ui/)** – Documentação dos endpoints
- **[PostgreSQL](https://www.postgresql.org/)** – Banco de dados relacional
- **[Docker](https://docs.docker.com/)** – Elaboração de containers
- **[PyJWT](https://pyjwt.readthedocs.io/en/stable/)** – Autenticação e Autorização
- **[Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/)** – Encriptação de senhas
- **[Psycopg2-binary ]()** – Conexão da aplicaçãos com PostgreSQL

# Instalação e Configuração

###  Rodando com Docker
#### Pré-requisitos

- Docker instalado
- Docker Compose instalado

#### Passos

1. Clone o repositório:
    ```bash
        git clone https://github.com/matheusCamposDev/api-dish.git
    ```
2. Configure as variáveis de ambiente no arquivo .env:
    ```ini
        POSTGRES_USER= your_user
        POSTGRES_PASSWORD= your_password
        POSTGRES_DB= your_database
        DATABASE_URL=postgresql://your_user:your_passord@db:5432/your_database
    ```

3. Suba os containers com Docker Compose:

        docker-compose up --build

4. Acesse a aplicação:

- API: Running on http://127.0.0.1:5000
- Swagger: Running on http://127.0.0.1:5000/swagger


# Como usar

### Autenticação

O endpoint de CREATE exige autenticação com JWT.

- Primeiro, faça login para obter o token:

`POST /auth/login`

```json
    {
        "username": "username",
        "password": "Password@123",
        "role_id": 1
    }
```

**Resposta(200)**:
```json
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsIn..."
    }
```
Depois, envie o token no header de cada requisição:
                
        Authorization: Bearer SEU_TOKEN_AQUI

###  Dish

### Criar um filme


`POST /dish`

```json
    {
        "name": "name",
        "description": "description",
        "price": 0
    }
```

**Resposta (201):**

```json
    {
        "id": 0,
        "name": "name",
        "price": 0,
        "description": "description"
    }
```

### Listar todos os pratos

`GET /dish`

**Resposta(200):**

```json
[
    {
        "description": "description",
        "id": 1,
        "name": "name",
        "price": 1
    },
    {
        "description": "description",
        "id": 2,
        "name": "name",
        "price": 1
    }
]
```

### Busca prato por ID

`GET /dish/{id}`

**Resposta(200):**

```json
    {
        "description": "description",
        "id": 1,
        "name": "name",
        "price": 1
    },
```

### Atualiza prato por ID

`Path /dish/{id}`

**Resposta(200):**

```json
    {
        "description": "description",
        "id": 1,
        "name": "name",
        "price": 1
    },
```

### Deletar um prato por ID

`DELETE /dish/{id}}`

Resposta (204 No Content)

**Consulte a documentação Swagger para mais detalhes de resposta dos endpoints da API.**


## Estrutura do Projeto


```
API-DISH/
├── api_caradapio/      # Pasta principal da aplicação Flask
│ ├── init.py           # Inicializa o app Flask
│ ├── controllers/      # Camada de controle (rotas e lógica de requisição)
│ │ ├── auth.py         # Controlador de autenticação
│ │ └── dish.py         # Controlador de pratos (dishes)
│ ├── models/           # Modelos do banco de dados (ORM)
│ │ └── models.py       # Definições das entidades (User, Dish, etc)
│ ├── schema/           # Esquemas de validação e serialização com Marshmallow
│ │ └── dish_schema.py  # Esquema para serializar/validar dados dos pratos
│ ├── services/         # Regras de negócio e lógica de serviço
│ │ ├── auth_service.py     # Serviço de autenticação
│ │ └── dish_service.py     # Serviço para manipulação de pratos
│ ├── static/               # Arquivos estáticos
│ │ └── swagger.yaml        # Documentação da API no formato Swagger/OpenAPI
│ ├── config.py             # Configurações da aplicação (ambiente, banco etc)
│ └── custom_exception.py   # Definição de exceções personalizadas
│
├── migrations/         # Controle de versões do banco de dados (via Flask-Migrate)
│ └── versions/
│   └── seed_admin_user.py  # Seed de tipos de usuário
│
├── tests/              # Testes automatizados (unitários e integração)
│
├── .env                # Variáveis de ambiente (NÃO versionar dados sensíveis)
├── README.md           # Documentação do projeto
├── Dockerfile          # Imagem Docker da aplicação
├── docker-compose.yaml # Orquestração de containers (app, banco etc)
├── entrypoint.sh       # Script de inicialização do container
├── poetry.lock         # Lockfile do Poetry (congela versões de dependências)
├── pyproject.toml      # Arquivo de configuração do Poetry e dependências do projeto
└── render-deploys.sh   # Script para deploy no Render
```

## Testes 

- Em densenvolvimento

## Autor

Desenvolvido por **Matheus Campos**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white
)](https://www.linkedin.com/in/matheuscamposdev/)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/matheusCamposDev)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:theuscampos45@gmail.com)


