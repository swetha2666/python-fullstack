x=int(input())
y=True
for i in range(2,x):
    if x%2==0:
        y=False
        break
if y!=x:
    print("prime")
else:
    print("not prime")