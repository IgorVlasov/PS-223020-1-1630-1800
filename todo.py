HELF = ""
help   "список команд"
add    "добавить дело"
remove "удалить обьект"
show   "показать список дел"
exit   "выход из преложения"

userAnswer =0
todo ={}

print("введите команду")
print("список команд-введите help")

white True;
 userAnswer = imput().lower()

  if userAnsler == "exit"
    print("програма закрыта")
  elif userAnswer == "add"
    print("дело добавлено")
  elif userAnswer == "remove"
    print("дело удалено")
  elif userAnswer == "show"
    print userAnswer("дело показано") 
  elif userAnswer == "help"
    print(HELP)
  else;
    print("неизвестная команда")
    print("список команд-введите help")
