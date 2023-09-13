#Task 2: Generate Fibonacci series up to a limit
def even_checker(number):
    if number % 2 == 0:
        print("Even!!")
    else:
        print("Odd!!")

# Example 1
even_checker(5)  # Output: Odd!!

# Example 2
even_checker(2)  # Output: Even!!



#Task 2: Generate Fibonacci series up to a limit
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=' ')
        a, b = b, a + b

# Example 1
fibonacci(10)  # Output: 0 1 1 2 3 5 8

# Example 2
fibonacci(5)   # Output: 0 1 1 2 3 5


#Task 3: Generate statements based on number divisibility
def foo_moo(number):
    if number % 2 == 0 and number % 3 == 0:
        return "FooMoo"
    elif number % 2 == 0:
        return "Foo"
    elif number % 3 == 0:
        return "Moo"
    else:
        return "Boo"

# Example 1
result1 = foo_moo(5)
print(result1)  # Output: Boo

# Example 2
result2 = foo_moo(4)
print(result2)  # Output: Foo

# Example 3
result3 = foo_moo(6)
print(result3)  # Output: FooMoo


#Task 4: Count uppercase and lowercase letters in a string
def count_letters(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    print(f"No. of Uppercase characters: {uppercase_count}")
    print(f"No. of Lowercase Characters: {lowercase_count}")

# Example 1
count_letters('The quick Sand Man')
# Output:
# No. of Uppercase characters : 3
# No. of Lowercase Characters: 12

# Example 2
count_letters('HaRRy PotteR')
# Output:
# No. of Uppercase characters : 5
# No. of Lowercase Characters: 6


#Task 5: Calculate tax based on age, salary, and job designation
def calculate_tax(age, salary, job_designation):
    if age < 18 or job_designation.lower() == "president" or salary < 10000:
        return 0
    elif 10000 <= salary <= 20000:
        return salary * 0.05
    else:
        return salary * 0.10

# Example 1
tax1 = calculate_tax(16, 20000, 'Student')
print(tax1)  # Output: 0

# Example 2
tax2 = calculate_tax(20, 18000, 'assistant manager')
print(tax2)  # Output: 900.0

# Example 3
tax3 = calculate_tax(20, 22000, 'Assistant manager')
print(tax3)  # Output: 2200.0

# Example 4
tax4 = calculate_tax(20, 122000, 'president')
print(tax4)  # Output: 0


#Task 6: Convert days into years, months, and days
def convert_days(days):
    years = days // 365
    months = (days % 365) // 30
    remaining_days = (days % 365) % 30
    print(f"{years} years, {months} months, and {remaining_days} days")

# Example 1
convert_days(4330)
# Output: 11 years, 10 months, and 15 days

# Example 2
convert_days(2250)
# Output: 6 years, 2 months, and 0 days


#Task 7: Generate a palindrome string
def show_palindrome(number):
    palindrome = ''.join([str(i) for i in range(1, number + 1)])
    palindrome += ''.join([str(i) for i in range(number - 1, 0, -1)])
    print(palindrome)

# Example 1
show_palindrome(5)
# Output: 123454321

# Example 2
show_palindrome(3)
# Output: 12321


#Task 8: Generate a palindromic triangle
def show_palindromic_triangle(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        for j in range(i - 1, 0, -1):
            print(j, end=' ')
        print()

# Example 1
show_palindromic_triangle(5)
# Output:
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

# Example 2
show_palindromic_triangle(3)
# Output:
#     1
#   1 2 1
# 1 2 3 2 1


#Task 9: Calculate area and circumference of a circle
import math

def area_circumference_generator(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

radius1 = 1
result1 = area_circumference_generator(radius1)
print(result1)
# Output: (3.141592653589793, 6.283185307179586)
# Area of the circle is 3.141592653589793 and circumference is 6.283185307179586

radius2 = 1.5
result2 = area_circumference_generator(radius2)
print(result2)
# Output: (7.0685834705770345, 9.42477796076938)
# Area of the circle is 7.0685834705770345 and circumference is 9.42477796076938

radius3 = 2.5
result3 = area_circumference_generator(radius3)
print(result3)
# Output: (19.634954084936208, 15.707963267948966)
# Area of the circle is 19.634954084936208 and circumference is 15.707963267948966


#Task 10: Create a dictionary of squares from a tuple range
def make_square(ranges):
    start, end = ranges
    square_dict = {num: num ** 2 for num in range(start, end + 1)}
    return square_dict

# Example 1
result1 = make_square((1, 3))
print(result1)
# Output: {1: 1, 2: 4, 3: 9}

# Example 2
result2 = make_square((5, 9))
print(result2)
# Output: {5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


#Task 11: Remove duplicate values from a tuple
def rem_duplicate(data_tuple):
    unique_items = []
    for item in data_tuple:
        if item not in unique_items:
            unique_items.append(item)
    return tuple(unique_items)

# Example 1
result1 = rem_duplicate((1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 4, 0, 0, 0))
print(result1)
# Output: (1, 2, 3, 4, 5, 6, 0)

# Example 2
result2 = rem_duplicate(("Hi", 1, 2, 3, 3, "Hi", 'a', 'a', [1, 2]))
print(result2)
# Output: ('Hi', 1, 2, 3, 'a', [1, 2])


#Task 12: Remove elements from a list based on maximum occurrence
def remove_max_occurrence(data_list):
    removed_count = 0
    for item in data_list:
        if data_list.count(item) > 2:
            data_list.remove(item)
            removed_count += 1
    return removed_count, data_list

# Example 1
result1, updated_list1 = remove_max_occurrence([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])
print(f"Removed: {result1}")
print(updated_list1)
# Output: Removed: 2
# [1, 2, 3, 3, 4, 5, 8, 8]

# Example 2
result2, updated_list2 = remove_max_occurrence([10, 10, 15, 15, 20])
print(f"Removed: {result2}")
print(updated_list2)
# Output: Removed: 0
# [10, 10, 15, 15, 20]


#Task 13: Perform basic calculations based on operator
def perform_operation(operator, operand1, operand2):
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            result = "Division by zero is not allowed."
        else:
            result = operand1 / operand2
    return result

# Example 1
result1 = perform_operation("+", 10, 20)
print(result1)
# Output: 30.0

# Example 2
result2 = perform_operation("*", 5.5, 2.5)
print(result2)
# Output: 13.75


#Task 14: Remove characters from a sentence based on position
def remove_characters(sentence, position):
    new_sentence = ""
    for i, char in enumerate(sentence):
        if i == 0 or (i + 1) % position != 0:
            new_sentence += char
    return new_sentence

# Example 1
result1 = remove_characters("I love programming.", 3)
print(result1)
# Output: I lveprgrmmngo oai.

# Example 2
result2 = remove_characters("Python is easy to learn. I love python.", 6)
print(result2)
# Output: Pythonis eay to earn.I lov pythn. sl eo


#Task 15: Calculate total cost of groceries with delivery fee
def calculate_total_cost(order_items, location="Dhanmondi"):
    item_prices = {
        "Rice": 105,
        "Potato": 20,
        "Chicken": 250,
        "Beef": 510,
        "Oil": 85
    }
    
    total_cost = 0
    for item in order_items:
        if item in item_prices:
            total_cost += item_prices[item]
    
    delivery_fee = 30 if location.lower() == "dhanmondi" else 70
    total_cost += delivery_fee
    
    return total_cost

# Example 1
total_cost1 = calculate_total_cost(["Rice", "Beef", "Rice"], "Mohakhali")
print(total_cost1)
# Output: 790

# Example 2
total_cost2 = calculate_total_cost(["Rice", "Beef", "Rice"])
print(total_cost2)
# Output: 750



#Task 16: Split an amount of money into various notes
def splitting_money(amount):
    notes = [500, 100, 50, 20, 10, 5, 2, 1]
    result = []
    
    for note in notes:
        count = amount // note
        if count > 0:
            result.append(f"{note} Taka: {count} note(s)")
            amount %= note
    
    return '\n'.join(result)

# Example
result = splitting_money(1234)
print(result)
# Output:
# 500 Taka: 2 note(s)
# 100 Taka: 2 note(s)
# 20 Taka: 1 note(s)
# 10 Taka: 1 note(s)
# 2 Taka: 2 note(s)


#Task 17: Remove odd numbers from a list
def remove_odd(numbers_list):
    even_numbers = [num for num in numbers_list if num % 2 == 0]
    return even_numbers

# Example 1
result1 = remove_odd([21, 33, 44, 66, 11, 1, 88, 45, 10, 9])
print(result1)
# Output: [44, 66, 88, 10]

# Example 2
result2 = remove_odd([11, 2, 3, 4, 5, 2, 0, 5, 3])
print(result2)
# Output: [2, 4, 2, 0]


#Task 18: Find numbers divisible by one divisor or the other but not both
def find_divisible_numbers(start, end, divisor1, divisor2):
    divisible_sum = 0
    
    for num in range(start, end):
        if (num % divisor1 == 0) ^ (num % divisor2 == 0):
            divisible_sum += num
    
    return divisible_sum

# Example 1
result1 = find_divisible_numbers(10, 40, 4, 7)
print(result1)
# Output: 210

# Example 2
result2 = find_divisible_numbers(5, 100, 3, 4)
print(result2)
# Output: 2012


#Task 19: Check if all alphabets from 'a' to 'j' are in a string
def check_alphabets_in_string(input_string):
    alphabets_to_check = set('abcdefghij')
    
    for char in input_string.lower():
        if char in alphabets_to_check:
            alphabets_to_check.remove(char)
    
    return 5 if not alphabets_to_check else 6

# Example 1
result1 = check_alphabets_in_string("Hello abcdefghij World")
print("PSG will win the Champions League this season" * result1)
# Output: PSG will win the Champions League this seasonPSG will win the Champions League this season

# Example 2
result2 = check_alphabets_in_string("This is a Test")
print("PSG will win the Champions League this season" * result2)
# Output: PSG will win the Champions League this seasonPSG will win the Champions League this seasonPSG will win the Champions League this seasonPSG will win the Champions League this seasonPSG will win the Champions League this seasonPSG will win the Champions League this season


#Task 20: Implement a Function to Calculate Exponential Power
def calculate_exponential(base, exponent):
    result = base ** exponent
    return result

# Example 1
result1 = calculate_exponential(2, 3)
print(result1)
# Output: 8

# Example 2
result2 = calculate_exponential(5, 2)
print(result2)
# Output: 25



#Task 21: Implement a Function to Calculate Factorial
def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Example 1
result1 = calculate_factorial(5)
print(result1)
# Output: 120

# Example 2
result2 = calculate_factorial(0)
print(result2)
# Output: 1
