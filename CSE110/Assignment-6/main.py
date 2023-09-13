# Task 1: Access and print the value 400
a_tuple = ("The Institute", ("Best Mystery & Thriller", "The Silent Patient", 68821), 75717, [1, 2, 3, 400, 5, 6, 7], ("Best Fiction", "The Testaments", 98291))
print(a_tuple[3][3])



# Task 2: Create a new tuple excluding the first and last two elements
sample_input = (10, 20, 24, 25, 26, 35, 70)
new_tuple = sample_input[2:-2]
print(new_tuple)


# Task 3: Print the size of the tuple and all its elements
book_info = (
    ("Best Mystery & Thriller", "The Silent Patient", 68, 821),
    ("Best Horror", "The Institute", 75, 717),
    ("Best History & Biography", "The five", 31, 783),
    ("Best Fiction", "The Testaments", 98, 291)
)

print("Size of the tuple is:", len(book_info))
for item in book_info:
    print(item)



# Task 4: Print award category, book name, and total votes
book_info = (
    ("Best Mystery & Thriller", "The Silent Patient", 68821),
    ("Best Horror", "The Institute", 75717),
    ("Best History & Biography", "The five", 31783),
    ("Best Fiction", "The Testaments", 98291)
)

for category, book, votes in book_info:
    print(f"{book} won the '{category}' category with {votes} votes")



# Task 5: Count the number of times an input appears in the tuple
given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
user_input = int(input("Enter a number: "))
count = given_tuple.count(user_input)
print(f"{user_input} appears {count} times in the tuple")



# Task 6: Reverse a given tuple
given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
reversed_tuple = tuple(reversed(given_tuple))
print(reversed_tuple)



# Task 7: Merge two dictionaries
dict1 = {'Harry': 15, 'Draco': 8, 'Nevil': 19}
dict2 = {'Ginie': 18, 'Luna': 14}
marks = {**dict1, **dict2}
print(marks)



# Task 8: Calculate and print the average of dictionary values
input_dict = eval(input("Enter a dictionary: "))  # Input should be like {'Jon': 100, 'Dan': 200, 'Rob': 300}
values = input_dict.values()
average = sum(values) / len(values)
print(f"Average is {average}.")



# Task 9: Create a new dictionary with values higher than user input
exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
user_input = int(input("Enter a value: "))
new_dict = {key: value for key, value in exam_marks.items() if value >= user_input}
print(new_dict)


# Task 10: Find the largest value and its key in a dictionary
book_sales = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure': 14}
max_genre = max(book_sales, key=book_sales.get)
max_sales = book_sales[max_genre]
print(f"The highest selling book genre is '{max_genre}' and the number of books sold are {max_sales}.")



# Task 11: Count character frequencies in a string using a dictionary
input_string = input("Enter a string: ")
char_freq = {}
for char in input_string:
    char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
print(char_freq)



# Task 12: Count total items in dictionary values
dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
total_items = sum(len(value) for value in dict_1.values())
print(total_items)



# Task 13: Convert a list of tuples into a dictionary with grouped values
list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
result_dict = {}
for key, value in list_1:
    if key in result_dict:
        result_dict[key].append(value)
    else:
        result_dict[key] = [value]
print(result_dict)





#Optional tasks
# Task 15: Multiply elements of tuples and return a list of results
tuples_list = [(2, 3), (4, 5), (6, 7), (2, 8)]
result_list = [x * y for x, y in tuples_list]
print(result_list)


# Task 16: Replace the last element of each inner list with user input
a_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
user_input = input("Enter a value: ")
a_tuple = [sublist[:-1] + [user_input] for sublist in a_tuple]
print(tuple(a_tuple))



# Task 17: Remove empty items (None values) from a dictionary
my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue', 'a5': None}
my_dictionary = {k: v for k, v in my_dictionary.items() if v is not None}
print(my_dictionary)



# Task 18: Extract dictionary items with values in a given range
dict_1 = {'a': 6, 'b': 7, 'c': 9, 'd': 8, 'e': 11, 'f': 12, 'g': 13}
lower, upper = map(int, input("Enter lower and upper values separated by a space: ").split())
result_dict = {k: v for k, v in dict_1.items() if lower <= v < upper}
print(result_dict)



# Task 19: Group tuples based on the second element
tuples_list = [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]
result_dict = {}
for item in tuples_list:
    key = item[1]
    if key in result_dict:
        result_dict[key].append(item)
    else:
        result_dict[key] = [item]
print(result_dict)

# Task 20: Create a dictionary using special characters as keys and words as values
input_sentence = input("Enter a sentence: ")
special_characters = input("Enter special characters separated by spaces: ").split()
words = input_sentence.split()
result_dict = {}

for word in words:
    # Calculate the index using the provided formula
    index = sum(ord(char) for char in word) % len(special_characters)
    key = special_characters[index]
    
    # Check for duplicates
    if key not in result_dict:
        result_dict[key] = [word]
    elif word not in result_dict[key]:
        result_dict[key].append(word)

print("Words in the given String:", words)
print("Answer:", result_dict)
