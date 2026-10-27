from tarefas import listar_tarefas, adicionar_tarefa, concluir_tarefa

def mostrar_menu():
    print("\n1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Sair")

def main():
    tarefas = []


    while True:
        mostrar_menu()
        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Apenas numero porfavor")
            continue

        if opcao == 1:
            listar_tarefas(tarefas)

        elif opcao == 2:
            adicionar_tarefa(tarefas)

        elif opcao == 3:
            concluir_tarefa(tarefas)

        elif opcao == 4:
            print("saindo...")
            break
        else:
            print("Há apenas opções de 1 a 3!")
if __name__ == "__main__":
    main()