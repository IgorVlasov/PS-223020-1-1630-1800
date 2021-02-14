HELP = """
help   - список команд
add    - добавить дело
remove - удалить объект
show   - показать список дел
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
  elif userAnswer == "add":
    print("Дело добавлено")
  elif userAnswer == "remove":
    print("Дело удалено")
  elif userAnswer == "show":
    print("Дело показано")
  elif userAnswer == "help":
    print(HELP)
  else:
    print("Неизвестная команда!")
    print("Список команд - введите help")