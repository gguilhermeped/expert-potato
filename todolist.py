class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa para mostrar.")
        else:
            print("Tarefas:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Concluída" if task.completed else "Pendente"
                print(f"{index}. [{status}] {task.description}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            print(f"A tarefa '{task.description}' foi marcada como concluída.")
        else:
            print("Índice de tarefa inválido.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nO que você deseja fazer?")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")

        choice = input("Escolha uma opção (1/2/3/4): ")

        if choice == "1":
            description = input("Digite a descrição da tarefa: ")
            task_manager.add_task(description)
            print("Tarefa adicionada com sucesso.")

        elif choice == "2":
            task_manager.list_tasks()

        elif choice == "3":
            task_manager.list_tasks()
            task_index = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            task_manager.mark_task_completed(task_index)

        elif choice == "4":
            print("Saindo da aplicação.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
