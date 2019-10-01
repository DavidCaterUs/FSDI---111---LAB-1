def say_hello():
    print("Hello from a method")

def menu ():
    print(" Menu   ")
    print ("[1] - Add")
    print ("[2] - Substract")
    print ("[3] - Multiply")
    print ("[4] - Divide")
    print ("[x] - EXIT!")

def sum(op1, op2):
    return op1 + op2
def sub(op1, op2):
    return op1 - op2
def mul(op1, op2):
    return op1 * op2
def div(op1, op2):
    return op1 / op2


print("-" * 30)
print("Welcome to PyCalculator")


opc = ""
while (opc != "x"):
    print("-" * 30)
    menu()
    print("-" * 30)

    opc = input("Selct an option: ")
    print("-" * 30)
    if(opc == 'x'):
         break # break the loop



    num1 = float(input ("First Number: "))
    num2 = float( input  ("Second Number: "))

    if (opc == '1'):
        sum_res = sum(num1, num2)
        print ("Sum = " + str(sum_res))
    elif (opc == '2'):
        sub_res = sub(num1, num2)
        print ("Sub = " + str(sub_res))
    elif (opc == '3'):
        mul_res = mul(num1, num2)
        print ("Mul = " + str(mul_res))
    elif (opc == '4'):
        div_res = div(num1, num2)
        print ("Div = " + str(div_res))

    input("Press Enter to go back")

print ("Thank you for using PyCalc, good Byte!")
print("-" * 30)
