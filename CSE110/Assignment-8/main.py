#Task - 1
# Function to perform bubble sort
def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

# Input list
my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

# Perform bubble sort
bubble_sort(my_list)

# Print sorted list
print(my_list)


#Task - 2
# Function to perform selection sort
def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

# Input list
my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

# Perform selection sort
selection_sort(my_list)

# Print sorted list
print(my_list)


#Task - 3
# Function to perform bubble sort in descending order
def bubble_sort_descending(my_list):
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

# Input list
my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

# Perform bubble sort in descending order
bubble_sort_descending(my_list)

# Print sorted list
print(my_list)


#Task - 4
# Function to organize student sitting arrangement
def organize_sitting_arrangement(sitting_list):
    even_indices = sorted(sitting_list[::2])
    odd_indices = sorted(sitting_list[1::2], reverse=True)
    organized_list = [even_indices[i//2] if i % 2 == 0 else odd_indices[i//2] for i in range(len(sitting_list))]
    return organized_list

# Input list
sitting_list = [10, 30, 20, 70, 11, 15, 22, 16, 58, 100, 12, 56, 70, 80]

# Organize sitting arrangement
organized_list = organize_sitting_arrangement(sitting_list)

# Print organized list
print(organized_list)


#Task - 5
# Function to sort students by course marks
def sort_students_by_course(course_name, student_data):
    course_index = -1
    sorted_student_data = sorted(student_data, key=lambda x: x[course_index])
    sorted_names = [student[0] for student in sorted_student_data]
    return sorted_names

# Input student data
student_data = [["Alan", 95, 87, 91],
                ["Turing", 92, 90, 83],
                ["Elon", 87, 92, 80],
                ["Musk", 85, 94, 90]]

# Input course name
course_name = "MAT110"

# Sort students by course marks
sorted_names = sort_students_by_course(course_name, student_data)

# Print sorted names
for name in sorted_names:
    print(name)


#Task - 6
# Function to count elements that changed position during sorting
def count_changed_elements(my_list):
    original_list = my_list.copy()
    bubble_sort(my_list)
    count = sum(1 for i, j in zip(original_list, my_list) if i != j)
    return count

# Input list
my_list = [4, 2, 3, 1, 6, 5]

# Count changed elements
changed_count = count_changed_elements(my_list)

# Print count
print(changed_count)


#Task - 7: Function to merge and find median
def merge_and_find_median(list_one, list_two):
    # Merge the two lists
    merged_list = list_one + list_two
    
    # Sort the merged list
    merged_list.sort()
    
    # Calculate the median
    n = len(merged_list)
    if n % 2 == 0:
        median = (merged_list[n//2 - 1] + merged_list[n//2]) / 2
    else:
        median = merged_list[n//2]
    
    return merged_list, median

# Input lists
list_one = [1, 2, 1, 4]
list_two = [5, 4, 1]

# Merge and find median
sorted_list, median = merge_and_find_median(list_one, list_two)

# Print results
print("Sorted list =", sorted_list)
print("Median =", median)


#Task - 8: Function to find two pairs with smallest sum closest to zero
def find_pairs_with_smallest_sum(list_one):
    n = len(list_one)
    if n < 4:
        return "List should contain at least 4 elements"
    
    list_one.sort()
    pairs = []
    min_sum = float('inf')
    
    for i in range(n - 1):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = list_one[i] + list_one[left] + list_one[right]
            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                pairs = [list_one[i], list_one[left], list_one[right]]
            if current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return pairs

# Input list
list_one = [-10, 15, 2, 4, -4, 7, -8]

# Find pairs
pairs = find_pairs_with_smallest_sum(list_one)

# Print result
print("Two pairs which have the smallest sum =", pairs)


#Task - 9: Function to calculate distance between two points
import math
def distance(point):
    x, y = point
    return math.sqrt(x**2 + y**2)

# Function to find point closest to origin
def closest_to_origin(points):
    closest_point = points[0]
    min_distance = distance(points[0])
    
    for point in points[1:]:
        dist = distance(point)
        if dist < min_distance:
            min_distance = dist
            closest_point = point
    
    return min_distance, closest_point

# Input points
points = [(5, 3), (2, 9), (-2, 7), (-3, -4), (0, 6), (7, -2)]

# Find closest point to origin
min_dist, closest = closest_to_origin(points)

# Print result
print("Minimum distance =", min_dist)
print("Closest point to origin =", closest)
