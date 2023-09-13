#ClassWork
#task 1
class BankAccount:
  def __init__(self,user_name,account_type):
    self.user_name = user_name
    self.account_type = account_type
    self.balance = 1.0

account1 = BankAccount("Bilbo", "Savings")
print("=====================================")
print(f"User Name: {account1.user_name}")
print(f"Balance: {account1.balance}")
print(f"Account Type:", account1.account_type)
print("=====================================")
account2 = BankAccount("Frodo", "Business")
print(f"User Name: {account2.user_name}")
print(f"Balance: {account2.balance}")
print(f"Account Type: {account2.account_type}")
print("=====================================")


#task 2
class BankAccount:
    def __init__(self,user_name,account_type):
        self.user_name = user_name
        self.account_type = account_type
        self.balance = 1.0

account1 = BankAccount("Bilbo", "Savings")
account1.balance = 15.75
print("=====================================")
print(f"User Name: {account1.user_name}")
print(f"Balance: {account1.balance}")
print(f"Account Type:", account1.account_type)
print("=====================================")
account2 = BankAccount("Frodo", "Business")
account2.balance = 700.50
print(f"User Name: {account2.user_name}")
print(f"Balance: {account2.balance}")
print(f"Account Type: {account2.account_type}")
print("=====================================")

#task 3
class MangoTree:
    def __init__(self,variety):
        self.variety = variety
        self.height = 1
        self.number_of_mangoes = 0



mangoTree1= MangoTree("Gopalbhog")
# Display the details of the mango tree
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
# Display the details of the mango tree
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

'Subtask ii'
class MangoTree:
  def __init__(self,variety):
    self.variety = variety
    self.height = 1
    self.number_of_mangoes = 0



mangoTree1= MangoTree("Gopalbhog")
# Display the details of the mango tree
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
# Display the details of the mango tree
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

print(f'Updated details after 5 years: \n=====================================')
mangoTree1.height = mangoTree1.height + 5*3
mangoTree1.number_of_mangoes = 10* mangoTree1.height
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")


mangoTree2.height = mangoTree2.height + 5*3
mangoTree2.number_of_mangoes = 15* mangoTree2.height
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")


#task 4
class Contacts:
    def __init__(self,list1,list2):
        self.list1 = list1
        self.list2 = list2
        self.contactDict = {}
        if len(self.list1) != len(self.list2):
            print('Contacts cannot be saved. Length Mismatch!')
        else:
            for i in range(len(self.list1)):
                self.contactDict[self.list1[i]] = self.list2[i]


names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]

m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")

names.append("Mother")
numbers.pop()

m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)

#task 5
class Student:
  def __init__(self,name,cgpa,courses_taken):
    self.name = name
    self.cgpa = cgpa
    self.courses_taken = courses_taken
    if self.cgpa < 2:
      self.student_status = 'Probation'
      if self.courses_taken > 2:
        print(f'Hello {self.name}, you are on probation and cannot take more than 2 courses.')
        self.advising_status = 'Denied'
        self.courses_taken = 0
      else:
        print(f'Study hard this time, {self.name}')
        self.advising_status = 'approved'
    else:
      self.student_status = 'Regular'
      if self.cgpa >= 2 and self.courses_taken <= 2:
        print(f'Hello {self.name}, You are a regular student and have to take between 3 to 5 courses.')
        self.advising_status = 'Denied'
        self.courses_taken = 0
      else:
        print(f'All the best, {self.name}, for the upcoming semester.')
        self.advising_status = 'approved'

s1 = Student("Clark", 3.45, 4)
print(f"Name: {s1.name}\nCGPA: {s1.cgpa}\nCourses Taken: {s1.courses_taken}")
print(f"Student Status: {s1.student_status}\nAdvising Status: {s1.advising_status}")
print("--------------------------------------------------------------------------------")
s2 = Student("Barry", 1.93, 2)
print(f"Name: {s2.name}")
print(f"Student Status: {s2.student_status}\nAdvising Status: {s2.advising_status}")
print("--------------------------------------------------------------------------------")
s3 = Student("Diana", 2.91, 2)
print(f"Advising Status: {s3.advising_status}\nCourses Taken: {s3.courses_taken}")
print("--------------------------------------------------------------------------------")
s4 = Student("Bruce", 1.52, 5)
print(f"Advising Status: {s4.advising_status}\nCourses Taken: {s4.courses_taken}")

#HomeWork
#task 1
# Subtask 1: Write the CellPackage Class           
class CellPackage:
    def __init__(self, price, data, talktime, sms, cashback, validity):
        self.price = price
        self.data = int(data[:-3])*1024
        self.talktime = talktime
        self.sms = sms
        self.cashback = int(cashback[:-1])
        self.validity = validity
        self.cashback = self.price * self.cashback // 100



pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')

#Subtask 2   #Same for all
if pkg.data != 0:
    print(f"Data = {pkg.data} MB")
if pkg.talktime != 0:
    print(f"Talktime = {pkg.talktime} Minutes")
if pkg.sms != 0:
    print(f"SMS/MMS = {pkg.sms}")
print(f"Validity = {pkg.validity} Days")
print(f"--> Price = {pkg.price} tk")
if pkg.cashback != 0:
    print(f"Buy now to get {pkg.cashback} tk cashback.")



pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')

#subtask 3     #Same for all
if pkg2.data != 0:
    print(f"Data = {pkg2.data} MB")
if pkg.talktime != 0:
    print(f"Talktime = {pkg2.talktime} Minutes")
if pkg2.sms != 0:
    print(f"SMS/MMS = {pkg2.sms}")
print(f"Validity = {pkg2.validity} Days")
print(f"--> Price = {pkg2.price} tk")
if pkg2.cashback != 0:
    print(f"Buy now to get {pkg2.cashback} tk cashback.")


pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')

#subtask 4      #Same for all
if pkg4.data != 0:
    print(f"Data = {pkg4.data} MB")
if pkg4.talktime != 0:
    print(f"Talktime = {pkg4.talktime} Minutes")
if pkg4.sms != 0:
    print(f"SMS/MMS = {pkg4.sms}")
print(f"Validity = {pkg4.validity} Days")
print(f"--> Price = {pkg4.price} tk")
if pkg4.cashback != 0:
    print(f"Buy now to get {pkg4.cashback} tk cashback.")
    
    
#task 2
class Pokemon:
    def __init__(self,pokemon1_name,pokemon2_name,pokemon1_power,pokemon2_power,damage_rate):
        self.pokemon1_name = pokemon1_name
        self.pokemon2_name = pokemon2_name
        self.pokemon1_power = pokemon1_power
        self.pokemon2_power = pokemon2_power
        self.damage_rate = damage_rate


team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name, team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)


# Write your code for subtask 2 and 3 here           #Same for all
team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
print('=======Team 2=======')
print('Pokemon 1:',team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name, team_bulb.pokemon2_power)
pika_combined_power = (team_bulb.pokemon1_power + team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', pika_combined_power)


#task 3
class box:
    def __init__(self,list):
        self.height , self.width, self.breadth = list
        print('Creating a Box!')


print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
volume = b1.height * b1.width * b1.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
volume = b3.height * b3.width * b3.breadth
print(f"Volume of the box is {volume} cubic units.")



#Part B           
'''
one will be True
two will be True

The value of b2.width will be 100. Since b3 and b2 refer to the same object, any changes made to
the attributes of that object will be reflected regardless of which variable is used to access the object.
Therefore, when b3.width is updated to 100, b2.width will also be 100.
'''


#task 4
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f'Vector <{self.x}, {self.y}, {self.z}> has been created.')

# Write your driver code here
vector = Vector3D(2, -3, 1)
vector2 = Vector3D(-1, 4, 0)
print(f'Magnitude of the first vector = {(vector.x **2 + vector.y **2 + vector.z **2)**.5}')
print(f'Magnitude of the first vector = {(vector2.x **2 + vector2.y **2 + vector2.z **2)**.5}')
print(f'Dot product of the two vectors = {vector.x * vector2.x + vector.y * vector2.y + vector.z * vector2.z}')
vector3 = Vector3D(vector.y * vector2.z - vector.z * vector2.y, vector.z * vector2.x - vector.x * vector2.z, vector.x * vector2.y - vector.y * vector2.x)
print(f'Cross product of the two vectors = <{vector3.x}, {vector3.y}, {vector3.z}>')


#task 5
class Order:           
    def __init__(self,menu,item):
        self.menu = menu
        self.item = item.split(',')
        self.items = []
        for i in self.item:
            item , count = i.split('-')
            count = int(count)
            self.items.append(item)
            self.items.append(count)
            for j,k in menu.items():
                if j in i:
                    self.items.append(count*k)
                    break




menu = {
    'Chicken_Cheeseburger' : 249,
    'Mega_Cheeseburger' : 289,
    'Fries' : 139,
    'Hot_Wings' : 99,
    'Rice_Bowl' : 299,
    'Soft_Drinks' : 50
}

order1 = Order(menu, "Chicken_Cheeseburger-2, Fries-3, Soft_Drinks-3")
print(order1.items)
print()

print('-'*35)
print('Item           x Quantity :   Price')
print('--------------   --------   -------')

index = 0
total = 0
while index < len(order1.items):
  item = order1.items[index]
  quantity = order1.items[index+1]
  price = order1.items[index+2]

  print(f'{item:20} x {quantity:2} : {price:7.2f}')
  total += price
  index += 3 # Going to next item

print('-'*35)
print(f'Total:                      {total:7.2f}')
print('-'*35)
