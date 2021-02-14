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
  print("введите дату в формате дд")
  todo Key = input
   print("что нужно сделать?")
   todoValue = input()

   todo {todoKey} = todoValue
    print("дело добавлено")
  elif userAnswer == "remove"
    print("дело удалено")
  elif userAnswer == "show"
    print ("\nсписок дел:")
    for i in sorted(todo.Keys() );
    print( ; + "\t" + {todo.Keys} )
  elif userAnswer == "help"
    print(HELP)
  else;
    print("неизвестная команда")
    print("список команд-введите help")
