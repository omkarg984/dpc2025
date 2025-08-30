n = int(input("Enter first number (N): "))
m = int(input("Enter second number (M): "))

lcm = max(n, m)

while True:
    if lcm % n == 0 and lcm % m == 0:
        break
    lcm += 1

print("The LCM of", n, "and", m, "is:", lcm)