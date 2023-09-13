#Task - 1
### Take input of 2 numbers from the user
var_1 = input('Please Enter Your First Number')
var_2 = input('Please Enter Your Second Number')

#Since input() function converts everything to String,
#for performing any kind of mathematical operation you need to convert them to int.
#For this conversion, we need to use int() function


# First, let's clarify whether the inputs are actually Strings or not. 
print(type(var_1))
print(type(var_2))


# Convert Strings to integer using the int() function
var_3 = int(var_1)
var_4 = int(var_2)

#===============================================================
#input taking and conversion can be done in a single sentence
#var_1 = int(input('Please Enter Your First Number'))
#var_2 = int(input('Please Enter Your Second Number'))

#===============================================================

# Perform Addition
sum = var_3 + var_4

# Perform Multiplication 
product = var_3 * var_4

# Perform Substraction 
difference = var_3 - var_4

# Print all the calculated results
print("Sum =", sum)
print("Product =", product)
print("Difference =", difference)


#Task - 2
import math 

#taking input from the user, then converting it to float.
#Since radius can be a floating point value

radius  = float(input("please enter the radius value:")) 


# squares can be made using this 3 ways, as written in hints. 
# all 3 ways, generates the same result of area

area = math.pi * radius **2 
print("Area result is:", area)

area = math.pi * math.pow(radius, 2)
print("Area result is:", area)

area = math.pi * radius * radius
print("Area result is:", area)


#Task - 3
#Todo
number_one = float(input(" Please enter your first value: "))
print("Your first number is: ", + number_one)
number_two = float(input("Please enter your second value: "))
print("Your second number is: ", + number_two)

if number_one>number_two:
    print("First Number is Greater")
elif number_one<number_two:
    print("Second Number is Greater")
else:
    print("The Numbers are Equal")
    
    
#Task - 4
number_one= float(input("Enter your first number: "))
number_two= float(input("Enter your second number: "))
print("Your First Number is: ",+number_one)
print("Your Second Number is: ",+number_two)
if number_one>number_two:
    r= (number_one-number_two)
    print("The result is: ",+r)
elif number_two>number_one:
    r= (number_two-number_one)
    print("The result is: ",+r)
else:
    print("The result is: 0")
    
    
#Task - 5
number= float(input("Enter a Number: "))
print("The Number is: ",+ number)
if number%2==0:
    print("it's an Even Number")
else:
    print("It's an odd number")
    

#Task - 6
number= int(input("Please Enter an Integer: "))
print("The Integer is: ",+number)
if number%2==0 or number%5==0:
    print("It's a multiple either 2 or 5")
else:
    print("Not a multiple")
    
    
#Task - 7
number= int(input("Please Enter an Integer: "))
print("The Integer is: ",+number)
if number%2==0 and number%5==0:
    print("Multiple of 2 and 5 both")
else:
    print("it is a multiple of either 2 or 5 but not both")
    


# Task 8: Check if an integer is a multiple of both 2 and 5
num = int(input("Enter an integer: "))

if num % 2 == 0 and num % 5 == 0:
    print(num)
else:
    print("Not multiple of 2 and 5 both")

# Task 9: Convert seconds to hours, minutes, and seconds
seconds = int(input("Enter the number of seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"Hours: {hours} Minutes: {minutes} Seconds: {remaining_seconds}")

# Task 10: Calculate weekly salary based on hours worked
hours_worked = int(input("Enter the number of hours worked: "))

if hours_worked < 0 or hours_worked > 168:
    print("Impossible to work more than 168 hours weekly")
elif hours_worked <= 40:
    salary = hours_worked * 200
    print(salary)
else:
    salary = 8000 + (hours_worked - 40) * 300
    print(salary)

# Task 11: Calculate L based on S
S = int(input("Enter a value for S: "))

if S >= 100:
    L = 12000 / (4 + (S * S) / 14900)
else:
    L = 3000 - 125 * S * S

print(L)

# Task 12: Determine mealtime based on the input hour
hour = int(input("Enter the hour (in 24-hour format): "))

if 4 <= hour <= 6:
    print("Breakfast")
elif 12 <= hour <= 13:
    print("Lunch")
elif 16 <= hour <= 17:
    print("Snacks")
elif 19 <= hour <= 20:
    print("Dinner")
elif 0 <= hour <= 23:
    print("Patience is a virtue")
else:
    print("Wrong Time")

# Task 13: Calculate grade based on the student's mark
mark = int(input("Enter the student's mark: "))

if 0 <= mark <= 100:
    if mark >= 90:
        print("A")
    elif mark >= 80:
        print("B")
    elif mark >= 70:
        print("C")
    elif mark >= 60:
        print("D")
    elif mark >= 50:
        print("E")
    else:
        print("F")
else:
    print("Invalid mark")

# Task 14: Calculate velocity and check if the car is working properly
distance = float(input("Enter distance in meters: "))
time = float(input("Enter time in seconds: "))

velocity_kph = (distance / 1000) / (time / 3600)

if velocity_kph < 60:
    print(f"{velocity_kph:.1f} km/h Too slow. Needs more changes.")
elif 60 <= velocity_kph <= 90:
    print(f"{velocity_kph:.1f} km/h Velocity is okay. The car is ready!")
else:
    print(f"{velocity_kph:.1f} km/h Too fast. Only a few changes should suffice.")


# Task 15: Check eligibility for a waiver based on CGPA and credits
cgpa = float(input("Enter CGPA: "))
credits_completed = int(input("Enter credits completed: "))

if cgpa >= 3.8 and credits_completed >= 30:
    if 3.8 <= cgpa <= 3.89:
        print("The student is eligible for a waiver of 25 percent.")
    elif 3.9 <= cgpa <= 3.94:
        print("The student is eligible for a waiver of 50 percent.")
    elif 3.95 <= cgpa <= 3.99:
        print("The student is eligible for a waiver of 75 percent.")
    elif cgpa == 4.0:
        print("The student is eligible for a waiver of 100 percent.")
else:
    print("The student is not eligible for a waiver.")
    

#Ungraded

# Task 20: Check if an integer is not a multiple of 2 or 5
num = int(input("Enter an integer: "))

if num % 2 != 0 and num % 5 != 0:
    print(num)
else:
    print("No")

# Task 21: Check if an integer is not a multiple of 2 or 5
num = int(input("Enter an integer: "))

if num % 2 != 0 or num % 5 != 0:
    print(num)
else:
    print("No")

# Task 22: Calculate total amount with discounts for canvases and paint tubes
canvas_price = 120
paint_price = 75

canvases = int(input("Enter the number of canvases: "))
paint_tubes = int(input("Enter the number of paint tubes: "))

total_price = canvases * canvas_price + paint_tubes * paint_price

discount = 0
if 0 <= total_price < 300:
    discount = 0
elif 300 <= total_price < 500:
    discount = 10
elif 500 <= total_price < 750:
    discount = 20
elif 750 <= total_price < 1000:
    discount = 50
else:
    discount = 150

new_total_price = total_price - discount

print(f"Previous total: {total_price} New total after discount: {new_total_price}")

# Task 23: Convert Fahrenheit to Celsius and determine season
fahrenheit = float(input("Enter temperature in degrees Fahrenheit: "))

celsius = (fahrenheit - 32) * 0.56

if celsius < 20:
    print(f"{celsius:.2f} degrees C Winter")
elif 20 <= celsius <= 25:
    print(f"{celsius:.2f} degrees C Autumn")
elif celsius > 25 and celsius < 30:
    print(f"{celsius:.2f} degrees C Spring")
else:
    print(f"{celsius:.2f} degrees C Summer")
