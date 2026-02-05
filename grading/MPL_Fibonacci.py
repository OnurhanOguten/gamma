def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci_numbers(limit):
    fibs = []
    a, b = 0, 1
    while b < limit:
        fibs.append(b)
        a, b = b, a + b
    return fibs


count = 0
fibs = fibonacci_numbers(1000)

for num in fibs:
    if num > 0 and is_prime(num):
        count += 1

print(count)