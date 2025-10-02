def even(num):
    res = []
    for n in num:
        if (n % 2 == 0) and (n <= 237):
            res.append(n)
    return res



number = list(range(1, 500))

print(even(number))

