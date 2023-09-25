
def myPrint(color, text): 
  if color.upper() == "RED":
    print("\033[0;31m",text,sep="", end="")
  elif color.upper() == "GREEN": 
    print("\033[0;32m",text,sep="", end="")
  elif color.upper() == "PURPLE":
    print("\033[0;35m",text,sep="", end="")
  elif color.upper() == "CYAN":
    print("\033[0;36m",text,sep="", end="")
  elif color.upper() == "BROWN":
    print("\033[0;33m",text,sep="", end="")
  elif color.upper() == "BLUE":
    print("\033[0;34m",text,sep="", end="")
  elif color.upper() == "LIGHT_GRAY":
    print("\033[0;37m",text,sep="", end="")
  elif color.upper() == "YELLOW":
    print("\033[1;33m",text,sep="", end="")
  elif color.upper() == "LIGHT_GREEN":
    print("\033[1;32m",text,sep="", end="")
  elif color.upper() == "LIGHT_BLUE":
    print("\033[1;34m",text,sep="", end="")
  else:
    print("\033[0m",text,sep="", end="")
  print("\033[0m",sep="", end="")
    
print("Super Subroutine\n")
print("With my ", end = "")
myPrint("purple", "new program ") 
print("I can just call red('and') ", end = "")
myPrint("red", "and ")
print("that word will appear in the color I set it to.\n", end="")
print("With no ", end = "")
myPrint("cyan","weird gaps")
print(".")
print("\nEpic.")



