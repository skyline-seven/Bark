import os
from datetime import datetime
i = 1
now = datetime.now()
def cls():
  os.system("clear")
def IDE():
  ide = input("Type command:")

  if ide == "/test":
    print("test complete")

  elif ide == "/help":
    print("/test: test command \n/help: get a list of commands \n/say: type in a set of words and the machine will repeat them")
    print("/math enter a calculation and you will get answer in return")
    print("/clear to clear screen * only for linux *\n/exit to exit program")

  elif ide == "/say":
    prnt=input("")
    print(prnt)

  elif ide =="/math":
    math=input("Enter Math Problem here:")
    if math == "0/0":
      print("Bro stop")
    else:
      print(eval(math))

  elif ide == "/time":
    print(now.strftime("%H:%M:%S"))
  elif ide == "/date":
    print(now.strftime("%Y-%m-%d"))
  elif ide == "/clear":
    cls()
  elif ide == "/exit":
    exit()
  else:
    print("Error type help for a list of commands")

    
while i == 1:
  IDE()
