
def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Sair")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa}")


def main():
    tarefas = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ").strip()

            if tarefa:
                tarefas.append(tarefa)
                print("Tarefa adicionada!")
            else:
                print("A tarefa não pode ficar vazia.")

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            print("Até a próxima!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
