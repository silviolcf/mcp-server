# Dockerfile para MCP Vehicle Search System
FROM python:3.10-slim

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    git \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos de dependências
COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia código fonte
COPY . .

# Cria usuário não-root para segurança
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Expõe porta do servidor MCP
EXPOSE 8000

# Comando padrão para executar o servidor MCP
CMD ["fastmcp", "run", "server/interface/mcp_server.py:mcp", "--transport", "http", "--port", "8000", "--host", "0.0.0.0"]