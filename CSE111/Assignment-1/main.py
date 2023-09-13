#String
#task 1
user = input()
lower = 0
upper = 0
for i in user:
    if 'A' <= i <= 'Z':
        upper += 1
    elif 'a' <= i <= 'z':
        lower += 1
if upper > lower:
    print(user.upper())
else:
    print(user.lower())
    

#task 2
user = input()
number = 0
word = 0
for i in range(len(user)):
    if 65 <= ord(user[i]) <= 90 or 97 <= ord(user[i]) <= 122:
        word += 1
    elif 48 <= ord(user[i]) <= 57:
        number += 1
if number > 0 and word > 0:
    print("Mixed")
elif word > 0:
    print("Word")
else:
    print("Number")
    

#task 3
user = input()
temp = ''
for i in user:
    if 'A' <= i <= 'Z':
       temp += i
b = user.index(temp[0])
c = user.index(temp[len(temp)-1])
if c == b+1:
    print("BLANK")
else:
    print(user[b+1:c])
    
    
#task 4
user = input()
a = user[:user.find(',')]
b = user[user.find(',')+1:]

temp = ""
for i in a:
    if i in b:
        temp += i
for i in b:
    if i in a:
        temp += i
print(temp)


#task 5
user = input()
upper = 0
lower = 0
digit = 0
special = 0
for i in user:
    if 65 <= ord(i) <= 90:
        upper += 1
    elif 97 <= ord(i) <= 122:
        lower += 1
    elif 48 <= ord(i) <= 57:
        digit += 1
    elif i in ['_', '#', '@', '$']:
        special = special + 1
if upper > 0 and lower > 0 and digit > 0 and special > 0:
    print('OK')
else:
    if upper == 0:
        if lower != 0 and digit != 0 and special != 0:
            print('Uppercase Character missing')
        else:
            print('Uppercase Character missing', end=',')
    if lower == 0:
        if upper != 0 and digit != 0 and special != 0:
            print('Lowercase Character missing')
        else:
            print('Lowercase Character missing', end=',')
    if digit == 0:
        if lower != 0 and upper != 0 and special != 0:
            print('Digit missing')
        else:
            print('Digit missing', end=',')
    if special == 0:
        print('Special character missing')
        
#List
#Task 1
list1 = []
list2 = []

while True:
    user = input()
    if user.lower() == 'stop':
        break
    else:
        list1.append(user)
for i in list1:
    if i not in list2:
        print(str(i) + "-" + str(list1.count(i)), 'times')
        list2.append(i)

#task 2
user = int(input())
max_sum = 0
max_lst = []
for i in range(user):
    list1 = [int(num) for num in input().split()]
    initial_max_sum = 0
    for j in list1:
       initial_max_sum += j
    if initial_max_sum > max_sum:
        max_sum = initial_max_sum
        max_lst = list1.copy()
print(max_sum)
print(max_lst)

#task 3
list1 = [int(num) for num in input().split()]
list2 = [int(num) for num in input().split()]
list_final = []
for i in list1:
    for j in list2:
        list_final.append(i*j)
print(list_final)

#task 4
ans = []
count = 0
while True:
  user_input = input()
  if user_input == 'STOP':
    break
  else:
    ans.append(0)
    x = [int(i) for i in user_input.split()]
    abs_ref = []
    for i in range(len(x)-1):
      elem = x[i]- x[i+1]
      elemf = abs(elem)
      abs_ref.append(elemf)
    for i in abs_ref:
      if i >= len(x):
        ans[count] = 'Not UB Jumper'
        break
      else:
        ans[count] = "UB Jumper"
    count += 1
for i in ans:
  print(i)

#task 5
user = input()
n = int(user[0])
k = int(user[-1])
user = input().split(" ")
count = 0
for i in user:
    if int(i)+k <= 5:
        count = count+1
print(count//3)

#Dictionary & Tuple
#task 1
dict1 = input().split(", ")
dict2 = input().split(", ")
final_dict ={}
print(dict1,dict2)
for i in dict1:
  i = i.split(": ")
  print(i)
  final_dict[i[0]] = int(i[1])
print(final_dict)
for i in dict2:
  i = i.split(": ")
  print(i)
  if i[0] not in final_dict.keys():
    final_dict[i[0]] = int(i[1])
  else:
    final_dict[i[0]] += int(i[1])
print(final_dict)

temp_dict_values = []
for i in final_dict.values():
  if i not in temp_dict_values:
    temp_dict_values.append(i)

dict_values = tuple(sorted(temp_dict_values))
print(final_dict)
print(dict_values)


#task 2
dict1 = {}
while True:
    user = input()
    if user.lower() == "stop":
        break
    else:
        dict1[user] = dict1.get(user,0)+1
        print(dict1)
for key, val in dict1.items():
    print(str(key)+"-"+str(val), "times")
#another by using with list
list1 = []
dict1 = {}
while True:
    user = input()
    if user.lower() == "stop":
        break
    else:
        user1 = user.split()
        for i in user1:
            list1.append(i)
    for i in list1:
        dict1[i] = list1.count(i)

for key, val in dict1.items():
    print(str(key)+"-"+str(val), "times")

#task 3
dict1 = {}
user = input().split(", ")
for i in user:
    i = i.split(" : ")
    dict1[i[1]] = dict1.get(i[1],[])
    dict1[i[1]].append(i[0])
print(dict1)

#task 4
values = {'.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
           'A': '2', 'B': '22', 'C': '222',
           'D': '3', 'E': '33', 'F': '333',
           'G': '4', 'H': '44', 'I': '444',
           'J': '5', 'K': '55', 'L': '555',
           'M': '6', 'N': '66', 'O': '666',
           'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
           'T': '8', 'U': '88', 'V': '888',
           'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
           ' ': '0'}

user = input().upper()
result = ""
for i in user:
    result += values[i]
print(result)