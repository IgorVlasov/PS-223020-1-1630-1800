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
    print ("дело добавленно")
  elif userAnswer == "remove":
    print ("дело добавленно")
  elif userAnswer == "show":
    print ("дело добавленно")
  elif userAnswer == "help":
   print (HELP)
  else:
    print ("неизвестная команда")
    print ("список команд - введите help")