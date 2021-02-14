HELP = """
help - список команд 
add - добавить дел  
remove - удалить объект
show - показать  сипсок дел 
exit - выйти 
"""
userAnswer = 0 
todo = {}

print("Введите команду")
print("Список команд - ведите help")

while True: 
  userAnswer = input().lower()

  if userAnswer == "exit":
    print("Программа закрыта")
  elif userAnswer == "add":
    print('Введите дату в формате ДД.ММ.ГГГГ')
    todoKey = input()

    print("Введите что нужно сделать?")
    todoValue = input()
    
    todo[todoKey] = todoValue

    print("Дело добавлено")
  elif userAnswer == "remove":
    print("дело удалено")
  elif userAnswer == "show":
    print("\nСписок дел")

    for i in sorted (todo.keys() ):
      print( i + "\t" + todo[todoKey] ) 


  elif userAnswer == "help":
    print(HELP)
  else:
    print("Не изветсная программа")
    print("Список команд - введите help")