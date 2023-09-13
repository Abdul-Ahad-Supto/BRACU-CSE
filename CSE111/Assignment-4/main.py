#Classwork
#task 1
class Customer:
    def __init__(self,park = 'ABC Memorial Park'):
        self.park = park
        print(f'Welcome to {self.park}')
        self.sum = 0
        self.count = 1
    def buyTicket(self,name,age):

        if self.count > 3:
            print("You can't buy more than 3 tickets")
        else:
            print(f'Successfully purchased a ticket for {name}! ')
            if age <= 10:
                self.sum += 50
            else:
                self.sum += 100
            self.count += 1
    def showDetails(self):
        print(f'Amount of tickets: {self.count-1}\nTotal price: {self.sum} Taka ')



print('1-------------------------')
customer1 = Customer()
print('2-------------------------')
customer1.buyTicket('Bob', 23)
customer1.buyTicket('Henry', 7)
customer1.buyTicket('Alexa', 30)
customer1.buyTicket('Jonas', 43)
print('3-------------------------')
customer1.showDetails()
print('4-------------------------')
customer2 = Customer()
print('5-------------------------')
customer2.buyTicket('Harry', 60)
customer2.buyTicket('Tomas', 28)
print('6-------------------------')
customer2.showDetails()


#task 2 
class SentenceAnalyzer:
    def __init__(self, word='supto'):
        self.word = word

    def set_sentence(self, sentence):
        self.word = sentence

    def get_word_count(self, count=None):
        words = self.word.split()
        if count is None:
            print("Number of words in the sentence:", len(words))
        else:
            count_words = []
            for i in words:
                if len(i) == count:
                    count_words.append(i)
            print(f"Number of words with {count} characters in the sentence: {len(count_words)}")


analyzer1 = SentenceAnalyzer()
analyzer1.set_sentence("That's an easy one")
print("1--------------------------")
analyzer1.get_word_count()
print("2--------------------------")
analyzer2 = SentenceAnalyzer("Like I said it's easy")
print("3--------------------------")
analyzer2.get_word_count()
print("4--------------------------")
analyzer2.get_word_count(4)
print("5--------------------------")
analyzer1.get_word_count(5)


#task 3
class Student:
    def __init__(self,name,cgpa,credit=0,dept='CSE'):
        self.name = name
        self.cgpa = cgpa
        self.credit = credit
        self.dept = dept
        self.status = "YesYesYes"

    def checkScholarshipEligibility(self):
        if self.cgpa >= 3.5 and self.credit > 10:
            if self.cgpa >= 3.7:
                self.status = 'Merit-based scholarship'
                print(f'{self.name} is eligible for {self.status}')
            elif 3.5 <= self.cgpa < 3.7:
                self.status = 'Need-based scholarship'
                print(f'{self.name} is eligible for {self.status}')
        else:
            self.status = 'No scholarship'
            print(f'{self.name} is not eligible for scholarship.')

    def showDetails(self):
        print(f'Name: {self.name}\nDepartment: {self.dept}\nCGPA: {self.cgpa}\nNumber of Credits: {self.credit}\nScholarship Status: {self.status}')
print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()

#task 4
class Author:
    def __init__(self, name=None, *books):
        self.name = name
        if name == None:
            self.name = "Default"

        booklist = ""
        if len(books) > 0:
            for i in books:
                booklist += i + "\n"
            self.books = booklist

    def changeName(self, new_name):
        self.name = new_name

    def addBooks(self, *books):
        booklist = ""
        for i in books:
            booklist += i + "\n"

        self.books = booklist

    def printDetails(self):
        print(f"Author Name: {self.name}")
        print("------------")
        print(f"List of Books:")
        print(self.books)


auth1 = Author("Humayun Ahmed")
auth1.addBooks("Deyal", "Megher Opor Bari")
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName("Mario Puzo")
auth2.addBooks("The Godfather", "Omerta", "The Sicilian")
print("===================")
auth2.printDetails()
print("===================")
auth3 = Author("Paolo Coelho", "The Alchemist", "The Fifth Mountain")
auth3.printDetails()


#task 5
class TaxiLagbe:
    def __init__(self,taxi_no,location):
        self.taxi_no = taxi_no
        self.location = location
        self.count = 0
        self.list = ""
        self.sum = 0
    def addPassenger(self,*passenger):
        for i in passenger:
           passenger1 , cost = i.split("_")
           self.count += 1
           if self.count <= 4:
               self.list += passenger1 + " "
               self.sum += int(cost)
               print(f'Dear {passenger1}! Welcome to TaxiLagbe.')
           else:
               self.count -= 1
               print(f'Taxi Full! No more passengers can be added.')


    def printDetails(self):
        print(f'Trip info for Taxi number: {self.taxi_no}')
        print(f'This taxi can cover only {self.location} area.')
        print(f'Total passengers: {self.count}')
        print(f'Passenger list: \n{self.list}')
        print(f'Total collected fare: {self.sum} Taka')




taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()



#Homework
#task 1
class HackathonTeam:
  def __init__(self,team,*members):
    self.team = team
    self.members = members
  def information(self):
    if len(self.members) > 3:
      print('Members are more than 3')
    else:
      print(f'Team name: {self.team}\nParticipants:')
      for i in self.members:
        print(i)
team_1 = HackathonTeam("Atlantean", "Aquaman")
team_1.information()


print("=================")


team_2 = HackathonTeam("Avengers", "Ironman", "Thor", "Hulk")
team_2.information()


print("=================")


team_3 = HackathonTeam("X-Men", "Storm", "Mystique")
team_3.information()


#task 2 
class Foodie:
  def __init__(self,name):
    self.name = name
    self.l = []
    self.spent = 0

  def order(self,*items):
    self.c = []
    for i in items:
        global menu
        item , quantity = i.split('-')
        quantity = int(quantity)
        self.l.append(item)
        for j,k in menu.items():
            if item == j:
                print(f'Ordered - {self.l[0]}, quantity - {quantity}, price(per Unit) - {k}.')
                print(f'Total price - {quantity*k}')
                self.spent += quantity * k
  def show_orders(self):
      print(f'Frodo has {len(self.l)} item(s) in the cart.\nItems: {self.l}\nTotal spent: {self.spent}.')
  def pay_tips(self,tip = None):
      if tip != None:
          print(f'Gives {tip}/- tips to the waiter.')
          self.spent += tip
      else:
          print('No tips to the waiter.')




menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}
f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())


#task 3
class Farmer:
    def __init__(self,id = None):
        self.id = id
        if self.id == None:
            print('Welcome to your farm!')
        else:
            print(f'Welcome to your farm. Your farm ID is {self.id}! ')
        self.crop = []
        self.fish = []
    def addCrops(self, *crops):
        if len(crops) == 0:
            print('No crop(s) added.')
        else:
            print(f'{len(crops)} crop(s) added')
        for i in crops:
            self.crop.append(i)
    def addFishes(self,*fishes):
        if len(fishes) == 0:
            print('No fish added.')
        else:
            print(f'{len(fishes)} fish(s) added.')
        for i in fishes:
            self.fish.append(i)
    def showGoods(self):
        if len(self.fish)>0 and len(self.crop)> 0:
            print(f'You have {len(self.crop)} crop(s):')
            for i in range(len(self.crop)):
                if i == len(self.crop)-1:
                    print(self.crop[i],end='\n')
                else:
                    print(self.crop[i],end=',')
            print(f'You have {len(self.fish)} fish(s):')
            for i in range(len(self.fish)):
                if i == len(self.fish)-1:
                    print(self.fish[i],end='\n')
                else:
                    print(self.fish[i],end=',')
        elif len(self.fish)>0 and len(self.crop) == 0:
            print("You don't have any crop(s).")
            print(f'You have {len(self.fish)} fish(s):')
            for i in range(len(self.fish)):
                if i == len(self.fish) - 1:
                    print(self.fish[i], end='\n')
                else:
                    print(self.fish[i], end=',')
        elif len(self.fish) == 0 and len(self.crop)> 0:
            print(f'You have {len(self.crop)} crop(s):')
            for i in range(len(self.crop)):
                if i == len(self.crop) - 1:
                    print(self.crop[i], end='\n')
                else:
                    print(self.crop[i], end=',')
            print("You don't have any fish(s). ")



f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute","Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")


#task 4
class UniversalStudiosUser:
    def __init__(self,name,age,type):
        self.name = name
        self.age = age
        self.type = type
        self.ride = []
        self.amount = []
        self.total = 0
        print('Welcome to Universal Studios.')
    def selected_rides(self,*rides):
        for i in rides:
            name, amount = i.split('-')
            amount = int(amount)
            self.ride.append(name)
            self.amount.append(amount)
            self.total += amount
        if len(rides) > 0:
            print('Added ride(s) successfully.')
        else:
            print('Theres no ride to add')

    def show_details(self):
        print(f'Your information:\nName: {self.name}, Age: {self.age}, Category: {self.type}\nSelected rides:')
        for i in range(len(self.ride)):
            print(f'Ride: {self.ride[i]}, Amount: {self.amount[i]} dollar(s) ')
        if self.type == 'Special' and len(self.ride) > 3:
            print(f"Congratulations!!! You've got a 20% discount.\nPlease pay {float(self.total) - float(self.total) * .2} dollar(s).")
        else:
            print(f'Please pay {float(self.total)} dollar(s).')





customer_1 = UniversalStudiosUser("Alice", 21, "Special")
print("--------- 1 ---------")
customer_1.selected_rides("Waterworld-100", "Accelerator-200", "DinoSoarin-50")
print("--------- 2 ---------")
customer_1.show_details()


print("=================")


customer_2 = UniversalStudiosUser("Bob", 20, "Normal")
print("--------- 3 ---------")
customer_2.selected_rides("Enchanted Airways-300", "Jurassic Park-500", "Accelerator-200", "DinoSoarin-50")
print("--------- 4 ---------")
customer_2.show_details()


print("=================")


customer_3 = UniversalStudiosUser("Mark", 15, "Special")
print("--------- 5 ---------")
customer_3.selected_rides("Transformers-450", "Jurassic Park-500", "Waterworld-100", "DinoSoarin-50")
print("--------- 6 ---------")
customer_3.show_details()


#task 5
class Department:
    def __init__(self,dept='ChE Department',sec = 5):
        self.dept = dept
        self.sec = sec
        self.avg = 0
        print(f'The {self.dept} has {self.sec} sections.')
        self.sum1 = 0

    def add_students(self,*stu):
        sum = 0
        if self.sec != len(stu):
            print(f"The {self.dept} doesn't have {len(stu)} sections.")

        else:
            for i in stu:
               sum += i
            print(f'The {self.dept} has an average of {sum/len(stu)} students in each section.')
            self.avg = sum/len(stu)
            self.sum1 = self.avg * self.sec
    def merge_Department(self,*x):
        # total number of students
        # sum2 = self.sec # total num of sections
        for i in x:
            self.sum1 += i.avg * i.sec
        return self.sum1/self.sec

d1 = Department()
print('1-----------------------------------')
d2 = Department('MME Department')
print('2-----------------------------------')
d3 = Department('NCE Department',8)
print('3-----------------------------------')
d1.add_students(12,23,12,34,21)
print('4-----------------------------------')
d2.add_students(40,30,21)
print('5-----------------------------------')
d3.add_students(12,34,41,17,30,22,32,51)
print('6-----------------------------------')
mega = Department('Engineering Department',10)
print('7-----------------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------------')
print(mega.merge_Department(d1,d2))
print('9-----------------------------------')
print(mega.merge_Department(d3))

#task 6
