# Task 1: Reverse a string
input_str = input("Enter a string: ")
output_str = input_str[::-1]
print(output_str)


# Task 2: Reverse part of a string
input_str = input("Enter a string: ")
index = int(input("Enter the index to start reversing from: "))
output_str = input_str[:index] + input_str[index:][::-1]
print(output_str)


# Task 3: Check if a string is a binary number
input_str = input("Enter a string: ")

if all(char == '0' or char == '1' for char in input_str):
    print("Binary Number")
else:
    print("Not a Binary Number")



# Task 4: Modify a string based on conditions
input_str = input("Enter a word: ")

if len(input_str) < 4:
    print(input_str)
elif input_str.endswith("est"):
    print(input_str)
elif input_str.endswith("er"):
    print(input_str.replace("er", "est"))
else:
    print(input_str + "er")



# Task 5: Print subsequent substrings of a word
input_str = input("Enter a word: ")

for i in range(1, len(input_str) + 1):
    print(input_str[:i])



# Task 6: Print ASCII values of characters in a string
input_str = input("Enter a string: ")

for char in input_str:
    print(char, ":", ord(char))



# Task 7: Print next alphabet for each character in a string
input_str = input("Enter a string of lowercase letters: ")

for char in input_str:
    next_char = chr(ord(char) + 1)
    if next_char > 'z':
        next_char = 'a'
    print(next_char, end="")
print()


# Task 8: Remove characters at even index and print in uppercase
input_str = input("Enter a string: ")
result_str = ""
for i in range(len(input_str)):
    if i % 2 == 1:
        result_str += input_str[i].upper()
print(result_str)



# Task 9: Remove consecutive duplicates from a string
input_str = input("Enter a string: ")
result_str = input_str[0]
for char in input_str[1:]:
    if char != result_str[-1]:
        result_str += char
print(result_str)



# Task 10: Mix two strings alternately
input_str = input("Enter two strings separated by a comma and space: ")
str1, str2 = input_str.split(", ")
len1, len2 = len(str1), len(str2)
result_str = ""

for i in range(max(len1, len2)):
    if i < len1:
        result_str += str1[i]
    if i < len2:
        result_str += str2[i]

print(result_str)



#Optional tasks
# Task 16: Remove letter from string or trim first and last letters
input_str = input("Enter a string: ")
letter = input("Enter a letter: ")

if letter in input_str:
    output_str = input_str.replace(letter, "")
else:
    if len(input_str) > 3:
        output_str = input_str[1:-1]
    else:
        output_str = input_str

print(output_str)



# Task 17: Split a string on a given character
input_str = input("Enter a string: ")
split_char = input("Enter a split character: ")

output_list = []
temp_str = ""

for char in input_str:
    if char == split_char:
        output_list.append(temp_str)
        temp_str = ""
    else:
        temp_str += char

output_list.append(temp_str)

for item in output_list:
    print(item)



# Task 18: Concatenate a string multiple times based on even or odd number
input_str = input("Enter a string: ")
num = int(input("Enter a number: "))

if num % 2 == 0:
    result = input_str * (2 * num)
else:
    result = input_str * (3 * num)

print(result)



# Task 19: Modify a string based on alternating uppercase-lowercase
input_str = input("Enter a string: ")
modified_str = ""
is_upper = True

for char in input_str:
    if char.isalpha():
        if is_upper:
            modified_str += char.upper()
        else:
            modified_str += char.lower()
        is_upper = not is_upper
    else:
        modified_str += char

print(modified_str)
