
number_1 = int(input("Enter number : "))

op = input("Enter operator : ")
result = number_1

while op != "=":

    number_2 = int(input("Enter next number : "))

    if op == "+":
        result += number_2

    elif op == "-":
        result -= number_2

    elif op == "*":
        result *= number_2

    elif op == "/":
        result /= number_2

    else:
        print("Enter valid Operator to perform Calculation")

    op = input("Enter operator : ")

print("Result : " , result)

        
        