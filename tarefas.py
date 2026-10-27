def mostrar_menu():
    print("\n1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Sair")

def listar_tarefas(tarefas):
    print(f"\n--------tarefas---------")
    if not tarefas:
            print("nenhuma tarefa cadastrada.")
            return
    for i, t in enumerate(tarefas, start=1):
         status = "x" if t["feita"] else " "
         print(f"{i}. [{status}] {t['titulo']}")

def adicionar_tarefa(tarefas):
    titulo = input("\nDigite a tarefa a ser adicionada: ").strip()
    if not titulo:
        print("A tarefa não pode ser vazia")
        return
    tarefas.append({"titulo": titulo, "feita": False})
    print("Tarefa adicionada com sucesso")

def concluir_tarefa(tarefas):
    if not tarefas:
          print("Nenhuma tarefa cadastrada")
          return

    listar_tarefas(tarefas)

    try:
        numero = int(input("\nDigite o número da tarefa a concluir: "))
    except ValueError:
        print("Digite apenas números.")
        return

    if numero < 1 or numero > len(tarefas):
        print("Tarefa não encontrada.")
        return
    tarefas[numero - 1]["feita"] = True
    print("Tarefa Marcada como concluída")

def remover_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada")
        return

    listar_tarefas(tarefas)

    try:
        numero = int(input("\nDigite o número da tarefa a remover: "))
    except ValueError:
        print("Digite apenas números.")
        return
    if numero < 1 or numero > len(tarefas):
            print("Tarefa não encontrada.")
            return
    removida = tarefas.pop(numero - 1)
    print(f"Tarefa '{removida['titulo']}' removida com sucesso!")