HELP = """
help - список команд
add - добавить дело
remove - удалить объект
show - показать список дел
exit - выход из приложения
"""
userAnswer = 0
todo = {}

print("Введите команду")
print("список команд - введите help")

while True:
  userAnswer = input().lower()

  if userAnswer == "exit":
    print("Программа закрываеться")
  elif userAnswer == "add":
    print ("Введите дату в форме ДД.ММ.ГГГГ")
    todoValue = input()

    todo[todoKey] = todoValue
    print ("Дело добвленно")
  elif userAnswer == "remove":
    print ("что нужно сделать")
  elif userAnswer == "show":
    print ("\nсписок дел")

    for i in sorted (todo.keys() ):
      print (i + "\t + todo[todoKey]")
  elif userAnswer == "help":
   print (HELP)
  else:
    print ("неизвестная команда")
    print ("список команд - введите help")