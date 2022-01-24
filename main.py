i = 1
def IDE():
  ide = input("Type command:")

  if ide == "/test":
    print("test complete")
  elif ide == "/help":
    print("/test: test command \n/help: get a list of commands \n/say: type in a set of words and the machine will repeat them")
  elif ide == "/say":
  
    prnt=input("")
    print(prnt)
  else :
    print("Error type help for a list of commands")

    
while i == 1:
  IDE()
