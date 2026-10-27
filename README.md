# Gerenciador de Tarefas

É um pequeno gerenciador que lista as tarefas adicionadas pelo usuário, as salva no banco MySQL e  permite marcar tarefas como concluídas.

## Funcionalidades

- Listar: Lista todas as tarefas adicionadas pelo usuário.
- Adicionar: Permite adicionar uma tarefa.
- Concluir: Marca a tarefa escolhida como concluída.
- Remover: Remove a tarefa digitando seu ID.

## Requisitos

- Python
- MySQL (servidor em execução)
- bibliotecas: 
```pip install mysql-connector-python python-dotenv```

## Banco de dados

Crie o banco e a tabela no MySQL:

```sql
CREATE DATABASE gerenciador_tarefas;

USE gerenciador_tarefas;

CREATE TABLE tarefas (
    id INT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    feita TINYINT(1) DEFAULT 0,
    PRIMARY KEY (id)
);
```

## Configuração

1. Copie o arquivo `.env.example` e renomeie a cópia para `.env`.
2. Preencha com os dados do seu MySQL.

## Como executar

Para utilizar basta ter o Python instalado e rodar:
```
python main.py
```

## Próximos passos

- prioridade e data limite nas tarefas
- editar tarefa
- filtrar pendentes e concluídas.
