# Store API

Este projeto é uma API para gerenciamento de produtos baseada em TDD (Test-Driven Development) usando FastAPI, Pydantic, Motor (MongoDB) e pytest.

A API permite:
- Cadastrar
- Buscar
- Atualizar
- Deletar

## Requisitos
- Python 3.9+
- Poetry
- Docker
- Docker Compose

## Configuração do Ambiente
1. Clone o repositório:
    ```
    git clone https://github.com/seu-usuario/store-api.git
    cd store-api
    ```

2. Instale as dependências:
    ```
    poetry install
    ```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto e adicione as variáveis necessárias.

4. Inicie o banco de dados MongoDB usando Docker Compose:
    ```
    docker-compose up -d
    ```

## Executando a API
1. Inicie a aplicação:
    ```
    poetry run uvicorn store.main:app --reload
    ```

2. Acesse a documentação interativa da API em [http://localhost:8000/docs](http://localhost:8000/docs).

## Testes
1. Para executar os testes, use o comando:
    ```
    poetry run pytest
    ```
2. Para executar um teste individualmente, use o comando:
    ```
    poetry run pytest -s -rx -k (função)  --pdb store ./tests/  
    ```

## Estrutura de Pastas
- **store/controllers**: Controladores da API.
- **store/core**: Configurações e exceções da aplicação.
- **store/db**: Configuração do banco de dados.
- **store/models**: Modelos de dados.
- **store/schemas**: Schemas Pydantic para validação e serialização.
- **store/usecases**: Casos de uso da aplicação.
- **store/main.py**: Ponto de entrada da aplicação.
- **store/routers.py**: Definição das rotas da API.
- **tests/**: Testes automatizados para a aplicação.
- **.env**: Variáveis de ambiente.
- **.gitignore**: Arquivos e diretórios a serem ignorados pelo Git.
- **.pre-commit-config.yaml**: Configuração do pre-commit.
- **docker-compose.yml**: Configuração do Docker Compose.
- **Makefile**: Comandos úteis para facilitar o desenvolvimento.
- **poetry.lock**: Arquivo de bloqueio de dependências do Poetry.
- **pyproject.toml**: Configurações do projeto e dependências.

## Contribuição
- Faça um fork do projeto.
- Crie uma branch para sua feature (git checkout -b minha-feature).
- Commite suas mudanças (git commit -am 'Adiciona minha feature').
- Faça um push para a branch (git push origin minha-feature).
- Crie um novo Pull Request.
