FibArray = [0, 1]


def fibonacci(m):
    if m < len(FibArray):
        return FibArray[m]
    else:
        temp_fib = fibonacci(m - 1) + fibonacci(m - 2)
        FibArray.append(temp_fib)
        return temp_fib


n = int(input("Write the nth fibonacci number "))
while n < 0:
    print("Incorrect input. Try again")
    n = int(input())
p = fibonacci(n)
print("The", n, "th fibonacci number is", p)
count = 0
if p == 0 or p == 1:
    print("The number 0 or 1 are not considered to be prime numbers")
else:
    for i in range(20):
        import random
        a = random.randint(1, p)
        if a ** p % p == a % p:
            count += 1
        else:
            print("The number", p, "is not prime.")
            break
if count == 20:
    print("The number", p, "is prime.")
