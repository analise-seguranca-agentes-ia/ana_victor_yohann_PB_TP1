# TP1 - Projeto de Bloco: Análise e Segurança de Agentes de IA

## Descrição
TP1 do Projeto de Bloco de Análise e Segurança de Agentes de IA — EDA do 
Customer Support Ticket Dataset, estrutura base de uma API FastAPI com 
autenticação JWT, e DFD básico com trust boundaries e análise CIA.

## Equipe
- Ana Beatriz Rangel Mattos
- Victor Henrique Watanabe
- Yohann Matheus Gusso Guedes

## Estrutura do repositório
- `data/` — dataset original (`customer_support_tickets.csv`)
- `eda/` — notebook (`.ipynb`) com a análise exploratória completa (EDA)
- `fastapi/` — código-fonte da API FastAPI (rotas, models, security)
- `others/` — DFD (Data Flow Diagram) em formato `.png` e documentação

## FastAPI - Instruções

### Dependências

Para instalar as Dependências necessárias, execute:

```bash
cd fastapi
pip install -r requirements.txt
```

### Pacotes Utilizados

- fastapi[standard]: Framework web;
- uvicorn: Servidor para execução da API;
- pydantic: Validação e tipagem de dados;
- pyjwt: Geração e verificação de tokens;
- pwdlib[argon2]: Hashing de senhas.

### Execução

Inicie o servidor com um dos dois comandos:
```bash
python3 main.py
```

ou

```bash
uvicorn main:app --reload
```

- **API URL:** `http://127.0.0.1:8000`
- **Documentação Swagger:** `http://127.0.0.1:8000/docs`

#### Autenticação

Para testar a rota protegida `/predict`, autentique-se via `/auth/token` ou use o botão `Authorize` no Swagger com o seguinte usuário admin:

Username: `admin-v01`
Password: `dumbpassword`
