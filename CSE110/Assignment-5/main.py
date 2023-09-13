# Task 1: Read 5 numbers into a list and print them after each input
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
    print(f"Numbers in the list: {numbers}")



# Task 2: Create a new list excluding first and last two elements
input_list = input("Enter a list of numbers separated by commas: ").split(', ')
if len(input_list) < 4:
    print("Not possible")
else:
    new_list = input_list[2:-2]
    print(new_list)



# Task 3: Read 5 numbers into a list and print them in reverse order
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Printing values from the list in reverse order:")
for num in reversed(numbers):
    print(num)



# Task 4: Square every item in a list
given_list = [1, 2, 3, 4, 5, 6, 7]
squared_list = [x ** 2 for x in given_list]
print(squared_list)



# Task 5: Remove empty strings from a list
input_list = ["hey", "there", "", "what's", "", "up", "", "?"]
filtered_list = [x for x in input_list if x != ""]
print("Original List:", input_list)
print("Modified List:", filtered_list)



# Task 6: Read 7 numbers from a string, find the largest number and its index
input_str = input("Enter 7 numbers separated by commas: ")
numbers = [int(x) for x in input_str.split(',')]
max_num = numbers[0]
max_index = 0

for i in range(1, len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_index = i

print(f"My list: {numbers}")
print(f"Largest number in the list is {max_num} which was found at index {max_index}.")



# Task 7: Replace the last element of the first list with the second list
list_one = [1, 4, 7, 5]
list_two = [6, 1, 3, 9]
list_one[-1:] = list_two
print(list_one)


# Task 8: Create a list of even elements from two given lists
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
even_list = [x for x in list_one + list_two if x % 2 == 0]
print(even_list)



# Task 9: Read numbers from a string, create a list, remove even numbers
input_str = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]
print("Original list:", numbers)
numbers = [x for x in numbers if x % 2 != 0]
print("Modified list:", numbers)



# Task 10: Read numbers from a string, create a list, remove duplicates
input_str = input("Enter numbers separated by commas: ")
numbers = [int(x) for x in input_str.split(',')]
print("Input list:", numbers)
numbers = list(dict.fromkeys(numbers))
print("Modified list:", numbers)



# Task 11: Check if two lists have at least one common member
list_one = [1, 4, 3, 2, 6]
list_two = [5, 6, 9, 8, 7]
common = False

for item in list_one:
    if item in list_two:
        common = True
        break

print(common)




#Optional tasks
# Task 16: Find the second largest number and its location in a list
numbers = [int(x) for x in input("Enter 7 numbers separated by commas: ").split(', ')]
max_num = numbers[0]
second_max = None
max_index = 0

for i in range(1, len(numbers)):
    if numbers[i] > max_num:
        second_max = max_num
        max_num = numbers[i]
        max_index = i
    elif second_max is None or numbers[i] > second_max:
        second_max = numbers[i]

print(f"My list: {numbers}")
print(f"Second largest number in the list is {second_max} which was found at index {max_index}.")



# Task 17: Find the smallest and largest number and their locations in a list
numbers = [int(x) for x in input("Enter 5 numbers separated by commas: ").split(', ')]
smallest = numbers[0]
largest = numbers[0]
smallest_index = 0
largest_index = 0

for i in range(1, len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
        smallest_index = i
    if numbers[i] > largest:
        largest = numbers[i]
        largest_index = i

print(f"My list: {numbers}")
print(f"Smallest number in the list is {smallest} which was found at index {smallest_index}")
print(f"Largest number in the list is {largest} which was found at index {largest_index}")



# Task 18: Find common elements in two lists
list1 = input("Enter the first list separated by commas: ").split(', ')
list2 = input("Enter the second list separated by commas: ").split(', ')

common_elements = []

for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

print(common_elements)



# Task 19: Find unique elements in two lists
list_one = [1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

unique_elements = []

for item in list_one + list_two:
    if item not in unique_elements:
        unique_elements.append(item)

print(unique_elements)


# Task 20: Convert a string with numbers to a list of integers
input_str = input("Enter a string of numbers separated by commas: ")
input_str = input_str.strip("[]")
numbers = [int(num.strip()) for num in input_str.split(',')]
print("Original data:", input_str)
print("After removing square brackets:", input_str)
print("Numbers in string format with extra white spaces:", [str(num) for num in numbers])
print("Final data (numbers in list format):", numbers)


# Task 21: Remove duplicates from a list of numbers in a string
input_str = input("Enter a string of numbers separated by commas: ")
numbers = [int(num.strip()) for num in input_str.split(',')]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Given numbers in list:", numbers)
print("List without any duplicate values:", unique_numbers)

