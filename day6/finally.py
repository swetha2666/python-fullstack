try:
    num1=int(input())
    num2=int(input())
    div=num1/num2
    print(f"result is:{div}")
except Exception as error:
    print(f"error occured{error}")
else:
    print("no error")
finally:
    print("ok bye")