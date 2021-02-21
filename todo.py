import time

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
    break
  elif userAnswer == "add":
    uDate = input("Введите дату в формате ДД.ММ.ГГГГ\n")
    try:
      valid_date = time.strptime(uDate, '%m.%d.%Y')
    except ValueError:
      print('Invalid date!')



    uTask = input("Что нужно сделать?\n")

    todo[uDate] = uTask

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
