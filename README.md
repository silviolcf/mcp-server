# MCP Vehicle Search System

##  Visão Geral

O **MCP Vehicle Search System** é um sistema inteligente de busca de veículos que combina **Model Context Protocol (MCP)**, **LangChain** e **OpenAI** para criar uma experiência de busca conversacional avançada. O sistema permite que usuários façam consultas em linguagem natural sobre veículos e recebam resultados relevantes com sugestões inteligentes.

##  Características Principais

###  **Assistente Inteligente**
- **Processamento de linguagem natural** em português
- **Extração automática de filtros** relevantes
- **Sugestões contextuais** quando não encontra resultados
- **Busca iterativa** com refinamento de consultas

###  **Arquitetura Limpa**
- **Clean Architecture** + **Hexagonal Architecture**
- **Separação clara** entre servidor e cliente
- **Inversão de dependências** para testabilidade
- **Padrões de design** bem implementados

###  **Tecnologias Modernas**
- **FastMCP**: Servidor MCP de alta performance
- **LangChain**: Framework para aplicações LLM
- **OpenAI GPT-3.5-turbo**: Modelo de linguagem
- **SQLAlchemy**: ORM para banco de dados
- **Rich**: Interface de terminal rica e colorida

###  **Deploy Simplificado**
- **Docker** e **Docker Compose** para execução fácil
- **Script de execução** automatizado
- **Configuração mínima** necessária
- **Ambiente isolado** e reproduzível
 Arquitetura do Sistema

### Servidor MCP (Backend)
```
server/
├── domain/           #  Entidades de negócio
├── application/      #  Casos de uso
├── infrastructure/   #  Banco de dados e ORM
└── interface/        #  API MCP
```

### Cliente Inteligente (Frontend)
```
client/
├── domain/           #  Modelos e schemas
├── application/      #  Serviço do agente
├── infrastructure/   #  Cliente MCP e OpenAI
└── interface/        #  Interface de linha de comando
```

## 🚀 Início Rápido

### Pré-requisitos
- **Python 3.10+**
- **Docker** e **Docker Compose**
- **OpenAI API Key**

### Execução com Docker (Recomendada)
```
- Realize a construção das imagens docker com: docker compose up --build
- Finalize a execução
- Inicie o servidor em background com docker compose up -d mcp-server
- inicie o cliente em modo interativo com docker compose run --rm mcp-client
- para sair client digite (sair ou quit ou exit)
- finalize o servidor com docker compose down
```
##  Exemplos de Uso

### Consultas Básicas
```
Digite sua busca: Quero um Toyota
Digite sua busca: Carro vermelho até 50000 reais
Digite sua busca: Honda automático com ar condicionado
```

### Consultas Avançadas
```
Digite sua busca: Quero um carro 2020 ou mais novo, até 80000 reais, com menos de 50000 km
Digite sua busca: Toyota Corolla branco, automático, com ar condicionado
Digite sua busca: Carro econômico, até 40000 reais, 4 portas
```


### Cobertura de Testes
- **Servidor**: ~85% de cobertura
- **Cliente**: ~80% de cobertura
- **Integração**: ~70% de cobertura

## Tecnologias Utilizadas

### Backend
- **FastMCP**: Framework para servidores MCP
- **SQLAlchemy**: ORM para Python
- **SQLite**: Banco de dados embarcado
- **Pydantic**: Validação de dados

### Frontend
- **LangChain**: Framework para aplicações LLM
- **OpenAI GPT-3.5-turbo**: Modelo de linguagem
- **Rich**: Biblioteca para terminal rico
- **Asyncio**: Programação assíncrona

### DevOps
- **Docker**: Containerização
- **Docker Compose**: Orquestração de containers
- **pytest**: Framework de testes
- **Git**: Controle de versão


