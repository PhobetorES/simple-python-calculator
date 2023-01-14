# Functions for arithmatic operations here
def add(a,b):
    print(a, choice, b, "=", (a+b))
    return()
def substraction(a,b):
    print(a, choice, b, "=", (a-b))
    return()
def multiply(a,b):
    print(a, choice, b, "=", (a*b))
    return()
def divide(a,b):

    if(b==0.0):
        print("cannot devide by zero")
        print(a,'/',"0.0 = None")
        return('$')
    else:
        print(a, choice, b, "=", (a/b))
        return()
def power(a,b):
    print((a), choice, b, "=", (a**b))
    return()

def remainder(a,b):
    print(a, choice, b, "=", (a%b))
    return()

#-------------------------------------
# Select_op(choice) function
operations = ['+','-','*','/','^','%']
def select_op(choice):
    if(choice == '#'):
        return(-1)          #Checking for termination
    if(choice not in operations):
        print("Unrecognized operation")     #Checking if the operation is correct
        
    while(choice in operations):
        a = input("Enter first number:")
        if(a[-1]=='$'):
            break
        if(a=='#'):
            return(-1)
            break
        try:
            a = float(a)
        except:
            print("Not a valid number")
            break
        a = float(a)
        
        b = input("Enter second number:")
        
        if(b[-1]=='$'):
            break
        if(b=='#'):
            return(-1)
            break
        try:
            b = float(b)
        except:
            print("Not a valid number")
            break
        b = float(b)    
        
        if((choice) == '#'):
            return(-1)
        
        
        
        if((choice) == '+'):
            add(a, b)
            break      
        if((choice) == '-'):
            substraction(a, b)
            break
        if((choice) == '*'):
            multiply(a, b)
            break
        if((choice) == '/'):
            divide(a, b)
            break
        if((choice) == '^'):
            power(a, b)
            break
        if((choice) == '%'):
            remainder(a, b)
            break
#select_op(choice) function ends here
#-------------------------------------
# Main loop
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()