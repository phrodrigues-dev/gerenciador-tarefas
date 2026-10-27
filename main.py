from tarefas import listar_tarefas, adicionar_tarefa, concluir_tarefa, remover_tarefa

def mostrar_menu():
    print("\n1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

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
            listar_tarefas()

        elif opcao == 2:
            adicionar_tarefa()

        elif opcao == 3:
            concluir_tarefa()

        elif opcao == 4:
            remover_tarefa()

        elif opcao == 5:
            print("saindo...")
            break
        else:
            print("Opção inválida")
            
if __name__ == "_1_main__":
    main()