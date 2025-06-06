from funcalc import add
number1=int(input())
while True:
    op=input()
    if op == '=':
        print("end",number1)
        break
    number2=int(input())
    if op =='+':
        number1=add(number1,number2)
    elif op == '-':
        number1=sub(number1,number2)
    elif op == '*':
        number1=mul(number1,number2)
    elif op == '/':
        number1=div(number1,number2)
    elif op == '%':
        number1=mod(number1,number2)
    elif op== '**':
        number1=pow(number1,number2)
    print(number1)