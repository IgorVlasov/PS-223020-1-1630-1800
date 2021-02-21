import time

HELP = """
help    - список команд
add     - добавить дело
remove  - удалить объект
showall - показать список весь дел
show    - список дел по дате
exit    - выход из приложения
"""
userAnswer = 0
todo = {}


def checkDate(Date):
  try:
    time.strptime(Date, '%d.%m.%Y')
    return True
  except ValueError:
    print('Неверный формат даты')
    return False

def addTask(Date, Task):
  if uDate in todo:
    todo[uDate].append(uTask)
  else:
    todo[uDate] = [uTask]
  print(  f"На {uDate} назначено '{uTask}'" )

  

print("Введите команду")
print("список команд - введите help")

while True:
  userAnswer = input().lower()

  if userAnswer == "exit":
    print("Программа закрыта")
    break
  elif userAnswer == "add":
    uDate = input("Введите дату в формате ДД.ММ.ГГГГ\n")
    if checkDate(uDate) == False:
      continue
    uTask = input("Что нужно сделать?\n")
    addTask(uDate, uTask)

  elif userAnswer == "remove":
    print("дело удалено")
  elif userAnswer == "showall":
    print("\nСписок дел:")

    for printDate in sorted( todo.keys() ):
      for printTask in todo[printDate]:
        print( f"[ {printDate} ]\t{printTask} ")
  elif userAnswer == "show":
    uDate = input("Введите дату:\n")
    
    if checkDate(uDate) == False:
      continue
    
    if uDate in todo:
      print(f"\nСписок дел на {uDate}:")
      for printTask in todo[uDate]:
        print( f"[ ] {printTask}.")
    else:
      print(f"На {uDate} дел нет!")
      
  elif userAnswer == "help":
    print(HELP)
  else:
    print("Не известная команда")
    print("список команд - введите help")