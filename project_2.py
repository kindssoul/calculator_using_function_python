

#Decision whether you wanna continue playing or not

def decision():
    re = input("Do you wanna do more calculation? Type Y for yes, Q for Quit: ")
    if re=="y" or re=="Y":
        game_begin()
    elif re=="Q" or re=="q":
        print(f"THANKS FOR USING THIS CALCULATOR. GOODBYE")
        quit()
    else:
        print("Invalid Key. Try Again With Y for Yes and Q for Quit")
        decision()
#Addition of 2 numbers
def addition_2(x, y):
    sum = x+y
    print(f"Sum of {x} and {y} is", sum)
#Addition of 3 numbers
def addition_3(x, y, z):
    sum = x+y+z
    print(f"Sum of {x}, {y} and {z} is", sum)
#subtraction
def subtraction(x, y):
    if x>=y:
        print(f"{x} - {y} is", x-y)
    elif y>=x:
        print(f"{y} - {x} is", y-x)
    else:
        print("You have entered invalid number. Try again")
#product
def multiplication(x, y):
    print(f"{x} * {y} is", x*y)
#Division
def divide(x, y):
    print(f"{x} / {y} is", x/y)
    print(f"{y} / {x} is", y/x)
#greeting    
def greeting(x):
    c = "Hello "  +  x
    return c
#main_code_formula
def game_begin():   
    ques = input("What sort of calculation you wanna do?  ")
    if ques=="+":
        sum_1 = float(input("Enter first number: "))
        sum_2 = float(input("Enter second number: "))
        addition_2(sum_1, sum_2)
        decision()
    elif ques=="+++":
        sum_3 = float(input("Enter first number: "))
        sum_4 = float(input("Enter second number: "))
        sum_5 = float(input("Enter third number:  "))
        addition_3(sum_3, sum_4, sum_5)
        decision()
    elif ques=="-":
        sub_1 = float(input("Enter first number: "))
        sub_2 = float(input("Enter second number: "))
        subtraction(sub_1, sub_2)
        decision()
    elif ques=="*":
        mul_1 = float(input("Enter first number: "))
        mul_2 = float(input("Enter second number: "))
        multiplication(mul_1, mul_2)
        decision()
    elif ques=="/":
        div_1 = float(input("Enter first number: "))
        div_2 = float(input("Enter second number: "))
        divide(div_1, div_2)
        decision()
    else:
        print("Invalid input. Kindly check info again and type the correct keyword.")
        decision()
#Instructions
def begin():
    print("Welcome to the Calculator World...")
    print("Instructions below:-")
    print("Use + for addition") 
    print("Use - for subtraction")
    print("Use * for multiplication")
    print("Use / for divide")
    print("Use +++ for adding three numbers")
    user_name = input("What is your name? ")
    print("Hello", user_name)
    print("Lets play")
#Calling function
begin()
game_begin()



    
