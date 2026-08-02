
import os
import json

def back_main():
    print()
    input("Нажмите Enter, чтобы вернуться в главное меню...")
    
def show_tasks(tasks):

    print("Список дел:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} / {'Выполнено' if task['done'] else 'Не выполнено'} / Приоритет: {task['priority']}")
            
def proprsk():
    
    for i in range(30):
        print()

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main_menu():
    
    proprsk()
    
    print("============================")
    print("       Список дел!")
    print("============================")
    print()
    print("1. Добавить дело")
    print("2. Изменить статус дела")
    print("3. Изменить приоритет дела")
    print("4. Удалить дело")
    print("5. Вывести список дел")
    print("6. Выход")
    print()

def add_task(tasks):
    title = input("Введите название дела: ")
    print("Выберите приоритет дела:")
    print("1. Высокий")
    print("2. Средний")
    print("3. Низкий")
    priority_choice = input("Введите номер приоритета (1-3): ")
    if priority_choice == "1":
        priority = "Высокий"
    elif priority_choice == "2":
        priority = "Средний"
    elif priority_choice == "3":
        priority = "Низкий"
    else:
        print("Некорректный выбор приоритета. Дело не добавлено.")
        return
    
    task = {
        "title": title,
        "done": False,
        "priority": priority
    }
    
    print (f"Дело '{title}' добавлено в список с приоритетом: {priority}.")
    
    tasks.append(task)
    save_tasks(tasks)
    
    back_main()

def priority_change(tasks):
    if not tasks:
        print("Список дел пуст.")
        back_main()
        return
    
    else:
        print("Список дел:")
        show_tasks(tasks)
        
        print()
        try:
            task_index = int(input("Введите номер: "))
        except ValueError:
            print("Введите число!")
            return
        
        if task_index < 1 or task_index > len(tasks):
            print("Некорректный номер дела.")
            return
        else:
            print()
            print(f"Вы выбрали дело: {tasks[task_index - 1]['title']}")
            print()
            print("Выберите новый приоритет дела:")
            print("1. Высокий")
            print("2. Средний")
            print("3. Низкий")
            print()
            priority_choice = input("Введите номер приоритета (1-3): ")
            
            if priority_choice == "1":
                tasks[task_index - 1]["priority"] = "Высокий"
            elif priority_choice == "2":
                tasks[task_index - 1]["priority"] = "Средний"
            elif priority_choice == "3":
                tasks[task_index - 1]["priority"] = "Низкий"
            else:
                print("Некорректный выбор приоритета.")
                return
            print(f"Приоритет дела '{tasks[task_index - 1]['title']}' изменен на: {tasks[task_index - 1]['priority']}")
            
            save_tasks(tasks)
            back_main()
            
def done_change(tasks):
    if not tasks:
        print("Список дел пуст.")
        back_main()
        return
    
    else:
        print("Список дел:")
        show_tasks(tasks)
        
        print()
        try:
            task_index = int(input("Введите номер дела, статус которого хотите изменить: "))
        except ValueError:
            print("Введите число!")
            return
        else:
            tasks[task_index - 1]["done"] = not tasks[task_index - 1]["done"]
            status = "Выполнено" if tasks[task_index - 1]["done"] else "Не выполнено"
            print(f"Статус дела '{tasks[task_index - 1]['title']}' изменен на: {status}")
           
            back_main()
            save_tasks(tasks)
            
def delete_task(tasks):
    if not tasks:
        print("Список дел пуст.")
        back_main()
        return
    
    else:
        print("Список дел:")
        show_tasks(tasks)
        
        print()
        task_index = int(input("Введите номер дела, которое хотите удалить: "))
        
        if task_index < 1 or task_index > len(tasks):
            print("Некорректный номер дела.")
            return
        else:
            deleted_task = tasks.pop(task_index - 1)
            print(f"Дело '{deleted_task['title']}' удалено из списка.")
            save_tasks(tasks)
            back_main()

def print_tasks(tasks):
    if not tasks:
        print("Список дел пуст.")
        back_main()
    else:
        print("Список дел:")
        show_tasks(tasks)
            
def main():
    tasks = load_tasks()
    
    while True:
        main_menu()
        choice = input("Введите номер действия (1-6): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            done_change(tasks)
        elif choice == "3":
            priority_change(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print_tasks(tasks)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()