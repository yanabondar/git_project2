def summ():
    numbers = [1, 2]

    total = 0

    for num in numbers:
       total += num
    print(total)

summ()

def subb():
    numbers = [8, 2]

    total = 0

    for num in numbers:
       if total == 0:
         total += num
       else:
         total -= num
    print(total)

subb()


