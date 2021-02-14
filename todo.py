HELP = """
help   - список команд
add    - добавить дело 
remove - удалить обьект
show   - показать список дел
exit   - выход из пртложения
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
    print("Дело добавлено")
  elif userAnswer == "remove":
    print("Дело удалено")
  elif userAnswer == "show":
    print("Дело показано")
  elif userAnswer == "help":
    print(HELP)
  else:
    print("Не известная команда")
    print("список команд - введите help")