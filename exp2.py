
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

print("Strong numbers between 1 and 5000 are:")

for num in range(1, 5001):
    sum_of_factorials = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10

    if sum_of_factorials == num:
        print(num)