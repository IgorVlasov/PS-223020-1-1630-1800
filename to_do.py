HELP = """
  help   - список команд
  add    - добавить событие
  remove - удалить объект
  show   - показать список дел
  exit   - выйти из приложения

"""
userAnswer = 0
todo = {}


print("Введите команду")
print("Список команд - введите help")

while True:
  userAnswer = input().lower()

if userAnswer == "exit":
  print("Программа закрыта")
elif userAnswer == "add":
  print("Введите дату в формате ДД.ММ.ГГГГ")
  todoKey = input()
  print("Введите что нужно сделать")
  todoValue = input()
  todo[todoKey] = todoValue
  print("Дело добавлено")
elif userAnswer == "remove":
  print("Дело удалено")
elif userAnswer == "show":
  print("\nДело показано: ")
  for i in sorted( todo.keys()):
    print(i + "\t" + todo[todoKey])
elif userAnswer == "help":
  print(HELP)
else:
  print("Неизвестная команда")
  print("список команд-введите help")



