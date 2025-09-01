N = int(input("Enter a positive integer: "))
divisors = []
for i in range(1, N + 1):
    if N % i == 0:
        divisors.append(i)
print("Number of divisors:", len(divisors))
print("Divisors are:", divisors)