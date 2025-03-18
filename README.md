# Projeto

Este projeto utiliza Node.js e Python para desenvolvimento backend com Flask e gerenciamento de dependências com npm.

## Configuração do Ambiente

### 1. Inicializar um projeto Node.js
Execute o seguinte comando para criar um `package.json` padrão:

```sh
npm init -y
```

### 2. Instalar dependências do Node.js
Se houver um `package.json`, execute:

```sh
npm install
```

### 3. Instalar Flask (Python)
Para configurar o backend com Flask, instale o Flask via pip:

```sh
pip install flask
```

### 4. Instalar Flask-SQLAlchemy
Se o projeto precisar de um banco de dados, instale Flask-SQLAlchemy:

```sh
pip install flask-sqlalchemy
```

## Observação
Certifique-se de ter o **Python** e o **Node.js** instalados corretamente antes de executar os comandos. Caso precise de um ambiente virtual para Python, utilize:

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

