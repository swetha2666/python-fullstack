import funcalc 
number1=int(input())
while True:
    op=input()
    if op == '=':
        print("end",number1)
        break
    number2=int(input())
    if op =='+':
        number1=funcalc.add(number1,number2)
    elif op == '-':
        number1=funcalc.sub(number1,number2)
    elif op == '*':
        number1=funcalc.mul(number1,number2)
    elif op == '/':
        number1=funcalc.div(number1,number2)
    elif op == '%':
        number1=funcalc.mod(number1,number2)
    elif op== '**':
        number1=funcalc.pow(number1,number2)
    print(number1)