![Preview](image.png)

# Objetivo
Desenvolvimento de um agente de IA especializado em responder perguntas utilizando a engine de buscas do DuckDuckGo.com

## Rodar projeto localmente
```bash
    docker-compose up -d --build --force-recreate
```

## Configurar modelo no container ollama
```bash
    docker exec -it ollama ollama run <nome_do_modelo>
```

## Para formatar o backend

```bash
    black backend --exclude "__init__.py"; isort backend
```

## Modelos
Os modelos usados no projeto foram:
* llama3.2 para o chat
* nomic-embed-text para o embedding

São modelos especialmente úteis para GPUs mais antigas ou com pouca VRAM.

## Instalar os modelos
```bash
    docker exec -it ollama ollama pull llama3.2
    docker exec -it ollama ollama pull nomic-embed-text
```