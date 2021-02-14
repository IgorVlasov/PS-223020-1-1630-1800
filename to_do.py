HELP = """
help   - список команд
add    - добавить дело
remove - удалить объект
show   - показать объект 
exit   - выход из приложения
"""



userAnswer = 0 
todo = {}

print("Введите команду")
print("Список команд - введите help")


while True:
  userAnswer = input().lower()

  if userAnswer == "exit":
    print("Программа закрыта")
    todoKey = input()

    print("Что нужно сделать?")
    todoValue = input()

todo[todoKey] = todoValue
    elif userAnswer == "add":
      print("дело добавлено")
    elif userAnswer == "remove":
      print("дело удалено")
    elif userAnswer == "show":
      print("\nСписок дел: ")


for i in sorted( todo.keys() ):
  print( i + "\t" + todo[todoKey] )


    elif userAnswer == "help":
      print(HELP)
    else:
      print("Не известная программа")
      print("Чписок команд - введите help")