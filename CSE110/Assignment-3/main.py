# Task 1(a): Print the sequence 24, 18, 12, 6, 0, -6
counter = 24
while counter >= -6:
    if counter == -6:
        print(counter, end="")
    else:
        print(counter, end=", ")
    counter -= 6
# Task 1(b): Print the sequence -10, -5, 0, 5, 10, 15, 20
counter = -10
while counter <= 20:
    if counter == 20:
        print(counter, end="")
    else:
        print(counter, end=", ")
    counter += 5
# Task 1(c): Print the sequence 18, 27, 36, 45, 54, 63
counter = 18
while counter <= 63:
    if counter == 63:
        print(counter, end="")
    else:
        print(counter, end=", ")
    counter += 9
# Task 1(d): Print the sequence 18, -27, 36, -45, 54, -63
counter = 18
negate = False
while counter <= 63:
    if negate:
        counter *= -1
        negate = False
    else:
        negate = True

    if counter == -63:
        print(counter, end="")
    else:
        print(counter, end=", ")
    counter += 9

# Task 2: Repeat the favorite car name
favorite_car = input("Enter the name of your favorite car: ")
n = int(input("Enter a number: "))

for _ in range(n):
    print(favorite_car)

    
# Task 3: Sum of multiples of 7 and 9 up to 600
total = 0
for i in range(63, 601, 63):
    total += i

print(total)



# Task 4: Sum of multiples of 7 or 9 but not both up to 600
total = 0
for i in range(1, 601):
    if (i % 7 == 0 or i % 9 == 0) and not (i % 7 == 0 and i % 9 == 0):
        total += i

print(total)



# Task 5: Display odd numbers between 10 and 50
for num in range(11, 51, 2):
    print(num, end=" ")



# Task 6: Calculate the value of y
n = int(input("Enter a number (n): "))
y = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        y += i ** 2
    else:
        y -= i ** 2

print(y)


# Task 7: Total and average of odd numbers among ten numbers
total_odd = 0
count_odd = 0

for _ in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        total_odd += num
        count_odd += 1

if count_odd == 0:
    print("No odd numbers entered.")
else:
    average_odd = total_odd / count_odd
    print(f"The total of the odd numbers is {total_odd} and their average is {average_odd:.1f}")



# Task 8: Sum of multiples of 7 up to a given number
n = int(input("Enter a number (N): "))
total = 0

for i in range(1, n + 1):
    if i % 7 == 0:
        total += i

print(total)



# Task 9: Print the sum of numbers from 1 to N
n = int(input("Enter a number (N): "))
total = 0

for i in range(1, n + 1):
    total += i
    print(total)



# Task 10: Print the digits of a number from right to left
num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num //= 10



# Task 11: Count the digits in a number
num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print(count)



# Task 12: Print the digits of a number from left to right
num = int(input("Enter a number: "))
temp = num
count = 0

while temp > 0:
    count += 1
    temp //= 10

for _ in range(count):
    divisor = 10 ** (count - 1)
    digit = num // divisor
    print(digit, end=" ")
    num %= divisor
    count -= 1

# Task 13: Print divisors of a number and count them
num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        count += 1

print(f"Total {count} divisors.")



# Task 14: Check if a number is a perfect number
num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")



# Task 15: Check if a number is prime
num = int(input("Enter a number: "))
is_prime = True

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



# Task 16: Find maximum, minimum, and average of numbers
n = int(input("Enter the quantity of numbers: "))
total = 0
max_num = float('-inf')
min_num = float('inf')

for i in range(n):
    num = float(input("Enter a number: "))
    total += num
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

average = total / n

print(f"Maximum {max_num}")
print(f"Minimum {min_num}")
print(f"Average is {average}")


# Task 17: Print a square of size N
n = int(input("Enter the size of the square: "))

for i in range(n):
    print("+" * n)



# Task 18: Print a rectangle of size MxN
m = int(input("Enter the height (M): "))
n = int(input("Enter the length (N): "))

for i in range(m):
    print("".join(str(j) for j in range(1, n + 1)))

# Task 19: Print a right-angled triangle of height N
n = int(input("Enter the height of the triangle: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()



#Optional task
# Task 25: Print Fibonacci numbers up to N
n = int(input("Enter a number (N): "))
a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b



# Task 26: Convert decimal to binary
decimal = int(input("Enter a decimal number: "))
binary = ""

while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal //= 2

print(binary)



# Task 27: Convert binary to decimal
binary = input("Enter a binary number: ")
decimal = 0
power = 0

for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print(decimal)



# Task 28: Count prime and perfect numbers in a range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

prime_numbers = []
perfect_numbers = []

for num in range(start, end + 1):
    # Check for prime
    is_prime = True
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    else:
        is_prime = False

    # Check for perfect number
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        perfect_numbers.append(num)
    elif is_prime:
        prime_numbers.append(num)

print(f"Between {start} and {end},")
print(f"Found {len(prime_numbers)} prime numbers")
print(f"Found {len(perfect_numbers)} perfect number(s)")
print(f"Prime numbers: {', '.join(map(str, prime_numbers))}")
print(f"Perfect number(s): {', '.join(map(str, perfect_numbers))}")



# Task 29: Find numbers whose digit product is divisible by a given number
start = int(input("Enter the starting number (inclusive): "))
end = int(input("Enter the ending number (inclusive): "))
divisor = int(input("Enter the divisor: "))

for num in range(start, end + 1):
    product = 1
    temp_num = num

    while temp_num > 0:
        digit = temp_num % 10
        product *= digit
        temp_num //= 10

    if product % divisor == 0:
        print(num, end=" ")


