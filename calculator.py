def addition():
    x,y=map(int,input("Enter numbers:").split())
    print(x+y)
def subtraction():
    x,y=map(int,input("Enter numbers:").split())
    print(x-y)
def multiplication():
    x,y=map(int,input("Enter numbers:").split())
    print(x*y)
def division():
    x,y=map(int,input("Enter numbers:").split())
    print(float(x/y))
print("What do you want to do?")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
#choice=int(input("Enter your choice(1-5):"))
while True:
    choice=int(input("Enter your choice(1-5):"))
    if(choice==1):
        addition()
    elif(choice==2):
        subtraction()
    elif (choice==3):
        multiplication()
    elif (choice==4):
        division()
    else:
        break