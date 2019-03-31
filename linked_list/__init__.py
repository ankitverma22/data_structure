import re

print("enter equation")
print("type 'quit' for exit\n")



previous = 0
run = True

def answer():
    global run
    global previous
    if previous ==0:
        equation = input("enter Equation")
    else:
        equation = input(str(previous))


    if equation == "quit":
        print("GoodBye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.;]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)



while run:
    answer()