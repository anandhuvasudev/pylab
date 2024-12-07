N = int(input("Enter the value of N: "))
count = 0
print("Alternate prime numbers up to", N, "are:")

for num in range(2, N + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        if count % 2 == 0:
            print(num, end=" ")
        count += 1
