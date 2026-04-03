💸 Expense Tracker API

A RESTful Expense Tracker API built with Python and FastAPI, featuring secure user authentication and full CRUD functionality.

This project allows users to manage their personal expenses efficiently, with a complete backend system that includes JWT-based authentication, database integration, and structured API endpoints.


## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

---

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente:

Linux/Mac:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 5. Configure o banco de dados

Certifique-se de ter o PostgreSQL instalado e rodando.

Crie o banco de dados:

```sql
CREATE DATABASE expense_tracker;
```

---

### 6. Crie as tabelas

Execute o script para criar automaticamente as tabelas no banco:

```bash
python create_tables.py
```

---

### 7. Inicie a aplicação

```bash
uvicorn main:app --reload
```

---

### ✅ Pronto!

A API estará disponível em:

http://127.0.0.1:8000

Documentação automática:

http://127.0.0.1:8000/docs

### https://roadmap.sh/projects/expense-tracker-api

