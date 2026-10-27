import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"), 
            password=os.getenv("DB_PASSWORD"), 
            database=os.getenv("DB_NAME")
        )

def inserir_tarefa(titulo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo) VALUES (%s)", (titulo,))
    conn.commit()
    conn.close()

def buscar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, feita FROM tarefas")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultado

def marcar_como_feita(id_tarefa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET feita = TRUE WHERE id = %s", (id_tarefa,))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_tarefa(id_tarefa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = %s", (id_tarefa, ))
    conn.commit()
    cursor.close()
    conn.close()
