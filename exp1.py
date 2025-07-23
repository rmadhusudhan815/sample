import math

print("Prime numbers between 1 and 100:")

for num in range(2, 110):  # 110 because the upper bound is exclusive
    is_prime = True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
