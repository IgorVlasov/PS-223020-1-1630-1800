HELP = """
help    - список команд
add     - добавить дело
remove  - удалить объект
show    - показать список дел
exit    - выход из приложения
"""
userAnswer = 0
todo = {}

print("Введите команду")
print("список команд - введите help")

while True:
  userAnswer = input().lower()

  if userAnswer == "exit":
    print("Программа закрыта")
  elif userAnswer == "add":
    print("Введите дату в формате ДД.ММ.ГГГГ")
    todoKey = input()

    print("Что нужно сделать?")
    todoValue = input()

    todo[todoKey] = todoValue

    print("дело добавлено")
  elif userAnswer == "remove":
    print("дело удалено")
  elif userAnswer == "show":
    print("\nСписок дел:")

    for i in sorted( todo.keys() ):
      print( i + "\t" + todo[todoKey] )


    
  elif userAnswer == "help":
    print(HELP)
  else:
    print("Не известная команда")
    print("список команд - введите help")
