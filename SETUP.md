
### Criar Ambiente Virtual (Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Opção 2: pyenv (se disponível)
pyenv virtualenv 3.10.6 mcpserver
pyenv activate mcpserver
```

### 3. Instalar o Projeto
```bash
pip install -e .

pip install -e ".[dev]"
```

### 4. Configurar Variáveis de Ambiente
```bash

incluir OPENAI_API_KEY na variavel .env.dev e renomear para .env

```

##  Executar Testes

```bash
pytest -v              # Todos os testes
pytest tests/server/   # Apenas servidor
pytest tests/client/   # Apenas cliente
```
