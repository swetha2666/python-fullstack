while True:
    n = int(input())
    if n == 0:
        break
    total_sum = 0
    for i in range(n + 1):
        num = i
        reversed_num = 0
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10
        if i == reversed_num:
            total_sum += i
    print(total_sum)