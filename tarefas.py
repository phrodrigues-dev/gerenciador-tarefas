from banco import inserir_tarefa, buscar_tarefas, marcar_como_feita, deletar_tarefa

def mostrar_menu():
    print("\n1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Sair")

def listar_tarefas():
    print(f"\n--------tarefas---------")
    tarefas = buscar_tarefas()

    if not tarefas:
        print("Nenhuma tarefa cadastrada")
        return
    
    for id_tarefa, titulo, feita in tarefas:
        status = "x" if feita else " "
        print(f"{id_tarefa}. [{status}] {titulo} ")

def adicionar_tarefa():
    titulo = input("\nDigite a tarefa a ser adicionada: ").strip()

    if not titulo:
        print("A tarefa não pode ser vazia")
        return
    
    inserir_tarefa(titulo)
    print("Tarefa adicionada com sucesso")

def concluir_tarefa():
    tarefas = buscar_tarefas()
    if not tarefas:
          print("Nenhuma tarefa cadastrada")
          return

    listar_tarefas()

    try:
        id_tarefa = int(input("\nDigite o ID da tarefa a concluir: "))
    except ValueError:
        print("Digite apenas números.")
        return

    encontrou = False

    for id_banco, titulo, feita in tarefas:
        if id_banco == id_tarefa:
            encontrou = True

    if not encontrou:
        print("Tarefa não encontrada.")
        return
    
    marcar_como_feita(id_tarefa)
    print("Tarefa marcada como concluída")

def remover_tarefa():
    tarefas = buscar_tarefas()
    if not tarefas:
          print("Nenhuma tarefa cadastrada")
          return

    listar_tarefas()

    try:
        id_tarefa = int(input("\nDigite o ID da tarefa a remover: "))
    except ValueError:
        print("Digite apenas números.")
        return

    encontrou = False
    
    for id_banco, titulo, feita in tarefas:
        if id_banco == id_tarefa:
            encontrou = True
    
    if not encontrou:
        print("Tarefa não encontrada.")
        return
        
    deletar_tarefa(id_tarefa)
    print("Tarefa excluída com sucesso!")