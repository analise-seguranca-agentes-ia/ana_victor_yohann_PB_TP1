# TP1 - Projeto de Bloco: Análise e Segurança de Agentes de IA

## Objetivo
TP1 do Projeto de Bloco de Análise e Segurança de Agentes de IA — EDA do 
Customer Support Ticket Dataset, estrutura base de uma API FastAPI com 
autenticação JWT, e DFD básico com trust boundaries e análise CIA.

O objetivo é definir o domínio do sistema de atendimento ao cliente: entender os 
dados com rigor estatístico e deixar a API autenticada rodando de forma segura, 
servindo de base para o modelo de ML e o agente que serão implementados nos 
próximos TPs.

## Equipe
- Ana Beatriz Rangel Mattos
- Victor Henrique Watanabe
- Yohann Matheus Gusso Guedes

## Dataset
**Customer Support Ticket Dataset**, disponível no Kaggle:
https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset/data

O arquivo já está versionado neste repositório em `data/customer_support_tickets.csv`.
A fonte, as principais características e o motivo da escolha do dataset estão 
documentados na seção 1 do notebook [eda/eda.ipynb](eda/eda.ipynb).

## Estrutura de pastas
```
TP1/
├── data/                    # dataset original
│   └── customer_support_tickets.csv
├── eda/
│   ├── eda.ipynb            # documentação do dataset, EDA e hipóteses
│   └── requirements.txt
├── fastapi/
│   ├── main.py              # ponto de entrada da aplicação
│   ├── requirements.txt
│   ├── models/              # modelos Pydantic (auth, prediction, user)
│   ├── routes/              # endpoints (auth, health, prediction)
│   └── security/            # JWT + OAuth2PasswordBearer
├── others/
│   ├── dfd.png              # DFD com trust boundaries
│   └── dfd-cia.md           # análise da tríade CIA
└── README.md
```

## Pré-requisitos
- Python 3.10 ou superior (o código utiliza unions do tipo `str | None`)
- `pip`

Opcionalmente, crie um ambiente virtual antes de instalar as dependências:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/macOS
```

## EDA - Instruções

### Dependências

Para instalar as dependências do notebook, execute:

```bash
cd eda
pip install -r requirements.txt
```

### Pacotes Utilizados

- pandas: Leitura e manipulação do dataset;
- numpy: Operações numéricas;
- matplotlib: Geração dos gráficos;
- seaborn: Visualizações estatísticas;
- jupyter: Execução do notebook.

### Execução

Inicie o Jupyter com:

```bash
cd eda
jupyter notebook eda.ipynb
```

Ou, se preferir, abra o arquivo `eda/eda.ipynb` diretamente no VS Code (com as 
extensões *Python* e *Jupyter* instaladas) e execute as células por lá.

Em ambos os casos o notebook roda a partir do diretório `eda/`, o que é 
necessário porque ele lê o dataset pelo caminho relativo 
`../data/customer_support_tickets.csv`.

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

A partir do diretório `fastapi/` (os imports da aplicação dependem disso), 
inicie o servidor com um dos dois comandos:
```bash
python main.py
```

ou

```bash
uvicorn main:app --reload
```

No Linux/macOS, use `python3 main.py` caso `python` não esteja disponível.

- **API URL:** `http://127.0.0.1:8000`
- **Documentação Swagger:** `http://127.0.0.1:8000/docs`

### Rotas

| Método | Rota | Protegida | Descrição |
|---|---|---|---|
| `GET` | `/health/` | Não | Verifica se a API está ativa |
| `POST` | `/auth/token` | Não | Autentica o usuário (form-urlencoded) e retorna o token JWT |
| `POST` | `/predict/` | Sim (Bearer) | Recebe `{"text": "..."}` e retorna `201` com `{"text", "intention"}` simulada |

#### Autenticação

Para testar a rota protegida `/predict`, autentique-se via `/auth/token` ou use o botão `Authorize` no Swagger com um dos seguintes usuários:

##### Usuário admin:

Username: `johndoe`
Password: `johndoe123`

##### Usuário normal

Username: `janedoe`
Password: `janedoe123`

## DFD e Tríade CIA

O DFD da API, com entradas, saídas e trust boundaries identificados, está em 
[others/dfd.png](others/dfd.png).

A descrição dos componentes, das trust boundaries e a classificação de cada 
componente na tríade CIA (confidencialidade, integridade e disponibilidade) 
está em [others/dfd-cia.md](others/dfd-cia.md).
