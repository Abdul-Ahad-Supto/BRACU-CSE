#Classwork
#task 1
class Employee:
  def __init__(self,name, id, dept):
      self.name = name
      self.id = id
      self.dept = dept
      self.salary = 30000
  def workDistribution(self,a):
      if a == "Human Resource":
          print('Collect work distribution details from the manager.')
      else:
          print('Collect work distribution loads from the HR department.')
  def increment(self):
      self.salary += self.salary * .1
  def employeeDetails(self):
      print(f'Name:{self.name}, Dept {self.dept}\nEmployee id: {self.id}, Salary: {float(self.salary)}')
class Foreign_employee(Employee):
    def __init__(self, name, id, dept):
        super().__init__(name, id, dept)
        self.type = 'Foreign'
    def increment(self):
        self.salary += self.salary * .15

    def employeeDetails(self):
        print(f'Name:{self.name}, Dept {self.dept}\nEmployee id: {self.id}, Salary: {float(self.salary)}\nEmployee Type: {self.type}')
class Part_time_employee(Employee):
    def __init__(self, name , id, dept):
        self.name = name
        self.id = id
        self.dept = dept
        super().__init__(name, id, dept)
        self.salary = 15000
        self.type = 'Part time'
    def increment(self):
        print('Sadly, there is no increment for the part time employees!!')
    def employeeDetails(self):
        print(f'Name:{self.name}, Dept {self.dept}\nEmployee id: {self.id}, Salary: {float(self.salary)}\nEmployee Type: {self.type}')
print("1------------------------------------------")
emp1=Employee("Nawaz Ali", 102, "Marketing")
print("2------------------------------------------")
emp1.employeeDetails()
print("3------------------------------------------")
emp1.workDistribution("Marketing")
print("4------------------------------------------")
emp1.increment()
emp1.employeeDetails()
print("5------------------------------------------")
f_emp=Foreign_employee("Nadvi", 311, "Human Resource")
f_emp.employeeDetails()
print("6------------------------------------------")
f_emp.workDistribution("Human Resource")
print("7------------------------------------------")
f_emp.increment()
f_emp.employeeDetails()
print("8------------------------------------------")
p1_emp=Part_time_employee("Asif", 210, "Sales")
p2_emp=Part_time_employee("Olive", 223, "Accounts")
print("9------------------------------------------")
p1_emp.employeeDetails()
print("10------------------------------------------")
p1_emp.workDistribution("Sales")
print("11------------------------------------------")
p2_emp.increment()
print("12------------------------------------------")
p2_emp.employeeDetails()



#task 2
class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.area = 0


  def calculate_area(self):
    return self.area


  def print_details(self):
    print("--------- Printing details ----------")
    print(f'Co-ordinate: ({self.x},{self.y})')
    print(f'Area: {self.area}')

class Circle(Point):
    def __init__(self,radius = 0, x = 0, y = 0):
        self.radius = radius
        super().__init__(x,y)
        self.area = 3.1416 * self.radius**2

    def print_details(self):
        super().print_details()
        print(f'Radius: {self.radius}')

class Sphere(Point):
    def __init__(self,radius = 0, x = 0, y = 0):
        self.radius = radius
        super().__init__(x,y)
        self.area = 4 * 3.1416 * self.radius**2

    def print_details(self):
        super().print_details()
        print(f'Radius: {self.radius}')


print("--------------1---------------")
p1 = Point(2,3)
print(f'Area of p1: {p1.calculate_area()}')
print("--------------2---------------")
p1.print_details()
print("--------------3---------------")
p2 = Point()
p2.print_details()
print("--------------4---------------")
c1 = Circle(4,0,3)
print(f'Area of c1: {c1.calculate_area()}')
print("--------------5---------------")
c1.print_details()
print("--------------6---------------")
c2 = Circle(7)
print(f'Area of c2: {c2.calculate_area()}')
print("--------------7---------------")
sph1 = Sphere(3,0,2)
print(f'Area of sph1: {sph1.calculate_area()}')
print("--------------8---------------")
sph1.print_details()
print("--------------9---------------")
sph2 = Sphere(6)
print(f'Area of sph2: {sph2.calculate_area()}')

 
#task 3
class Account:
    def __init__(self, account_number, balance):
      self.account_number = account_number
      self.balance = balance
      self.account_type = "General"
      self.maturity = 0


    def print_details(self):
      print("------ Account details ------")
      print(f"Account Type: {self.account_type}, Maturity: {self.maturity} years")
      print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")


    def deposit(self, amount):
      self.balance += amount
      print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")


    def withdraw(self, amount):
      if self.balance >= amount:
          self.balance -= amount
          print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
      else:
          print("Insufficient funds.")


    def year_passed(self, year):
      self.maturity += year
      print(f"Maturity of the account: {self.maturity} years")
class SavingsAccount(Account):
    def __init__(self,account_type,account_number, balance, rate, minlimit):
        super().__init__(account_number, balance)
        self.account_type = account_type
        self.rate = rate
        self.minlimit = minlimit
        self.maturity = 0
    def print_details(self):
      super().print_details()
      print(f'Interest Rate: {self.rate} Minimum Limit: ${self.minlimit}')


    def deposit(self, amount):
      super().deposit(amount)


    def withdraw(self, amount):
      if self.balance - self.minlimit >= amount:
          super().withdraw(amount)
      else:
          print("Insufficient funds.")

    def year_passed(self, year):
      super().year_passed(year)

    def apply_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.rate
            print(f'Interest applied. New Balance: ${self.balance}')
        print('Insufficient funds')

class FixedDepositAccount(Account):
    def __init__(self,account_type,account_number, balance, maturit):
        super().__init__(account_number, balance)
        self.account_type = account_type
        self.maturit = maturit

    def print_details(self):
      super().print_details()

    def deposit(self, amount):
      print('You can not deposit in a fixed deposit account.')


    def withdraw(self, amount):
        if self.maturity > self.maturit:
          super().withdraw(amount)
        else:
            print('Can not withdraw, Account is not matured')


    def year_passed(self, year):
      super().year_passed(year)


print("-----------1------------")
account = Account("A203", 2000)
account.print_details()
print("-----------2------------")
account.deposit(400)
account.withdraw(1500)
account.year_passed(2)
print("-----------3------------")
account.print_details()
print("-----------4------------")
savings_account = SavingsAccount("Savings","SA123", 1000, 0.05, 500)
savings_account.print_details()
print("-----------5------------")
savings_account.deposit(400)
print("-----------6------------")
savings_account.withdraw(1000)
print("-----------7------------")
savings_account.withdraw(800)
print("-----------8------------")
savings_account.apply_interest()
print("-----------9------------")
savings_account.print_details()
print("-----------10------------")
fixed_account1= FixedDepositAccount("Fixed Deposit","FDA321", 10000, 5)
fixed_account1.print_details()
print("-----------11------------")
fixed_account1.deposit(400)
print("-----------12------------")
fixed_account1.year_passed(6)
print("-----------13------------")
fixed_account1.withdraw(10000)
print("-----------14------------")
fixed_account1.print_details()
print("-----------15------------")
fixed_account2 = FixedDepositAccount("Fixed Deposit","FDA300", 50000, 7)
fixed_account2.print_details()
print("-----------16------------")
fixed_account2.withdraw(10000)



#Homework
#task 1
class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin

class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the',f.getName(),'.')
            print(f)
        else:
            print('Eat the',f.getName(),'.')
            print(f)
class Mango(Fruit):
  def __init__(self,formalin= True, name='Mango'):
    super().__init__(formalin,name)
  def getName(self):
    return super().getName()
  def hasFormalin(self):
    return super().hasFormalin()
  def __str__(self):
    if super().hasFormalin() is True:
      return f'{super().getName()} are bad for you'
    else:
      return f'{super().getName()} are good for you'
class Jackfruit(Fruit):
  def __init__(self,formalin=False, name='Jackfruit'):
    super().__init__(formalin,name)
  def getName(self):
    return super().getName()
  def hasFormalin(self):
      return super().hasFormalin()
  def __str__(self):
    if super().hasFormalin() is True:
      return f'{super().getName()} are bad for you'
    else:
      return f'{super().getName()} are good for you'

m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)




#task 2 
class Exam:
    def __init__(self, marks):
        self.marks = marks
        self.time = 60

    def examSyllabus(self):
        return "Maths , English"

    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"


class ScienceExam(Exam):
    def __init__(self,marks, time, *sub):
        self.s = super().examSyllabus()
        self.c = 3
        self.parts = super().examParts()
        super().__init__(marks)
        self.time = time
        for i in sub:
            self.s += ', ' + str(i)
            self.parts += f'Part {self.c} - {str(i)}\n'

            self.c += 1

    def examSyllabus(self):
        return self.s

    def examParts(self):
        return self.parts
    def __str__(self):
        return f'Marks: {self.marks} Time: {self.time} minutes Number of Parts: {self.c-1}'



engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())


#task 3
class PokemonBasic:
    
    def __init__(self, name='Default', hp=0, weakness='None', type='Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type

    def get_type(self):
        return 'Main type: ' + self.type

    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'

    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness


class PokemonExtra(PokemonBasic):
    def __init__(self, name="Defalut", hp=0, weakness=None, type=None, secondary=None, *extra_moves):
        super().__init__(name, hp, weakness, type)
        self.secondary = secondary
        self.extra_moves = extra_moves
        self.move_lst = list(self.extra_moves)
        self.var1 = []
        self.var2 = ""
        for i in self.extra_moves:
            self.var1 += list(i)
        # self.var2 += ', '.join(self.var1)
        if len(extra_moves) > 0:
            self.var2 += self.var1[0]
            for i in self.var1[1:]:
                self.var2 += ', ' + str(i)

    def get_type(self):
        if self.secondary == None:
            return f"Main type: {self.type}"
        else:
            return f"Main type: {self.type} Secondary type: {self.secondary}"

    def get_move(self):
        if len(self.extra_moves) == 0:
            return "Basic move: Quick Attack"
        else:
            return f"Basic move: Quick Attack\nOther move: {str(self.var2)}"


print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())


#task 4
class Cakes:
    order_list = {}
    feedback = {}
    def __init__(self, flavor, weight):
        self.flavor = flavor
        self.weight = weight
        self.sweetness = 'Moderate'
        self.type = 'Whipped Cream'
        self.price = 1.2 * weight
        cake_key = f'{self.flavor} Cake {self.weight}gm'
        if cake_key in Cakes.order_list.keys():
            Cakes.order_list[cake_key] += 1
        else:
            Cakes.order_list[cake_key] = 1

    def cake_details(self):
        print(f'Flavor: {self.flavor} Cake, Weight: {self.weight} gm\nSweetness: {self.sweetness} sugar, Cream Type: {self.type}\nPrice: {self.price:.1f} Taka')

    def add_customization(self,*c):
            if len(c) == 2:
                self.sweetness = c[0]
                self.type = c[1]
            else:
                self.sweetness = c[0]
    @classmethod
    def give_feedbacks(cls,*f):
        if f[0] not in Cakes.feedback.keys():
            Cakes.feedback[f[0]] = [f[1]]
        else:
            Cakes.feedback[f[0]] += [f[1]]
        print('Thanks for your valuable feedback!')
    @classmethod
    def show_feedbacks(cls):
        print(Cakes.feedback)

class Cheese_Cakes(Cakes):
    def __init__(self,flavor, weight, type1='Baked'):
        super().__init__(flavor, weight)
        self.type1 = type1
        self.price = weight * 1.5
        self.sweetness = 'Moderate'
        self.type = 'Cream Cheese'

    def cake_details(self):
        print(f'Flavor: {self.flavor} Cheese Cake, Weight: {self.weight} gm\nSweetness: {self.sweetness} sugar, Cream Type: {self.type}\nCake Type: {self.type1} Price: {self.price:.1f} Taka')

    def add_customization(self, *c):
        if len(c) == 0:
            print(f'Sorry! No customization available for Cheese cakes.')
        else:
            super().add_customization(*c)

    @classmethod
    def give_feedbacks(cls, *f):
        super().give_feedbacks(*f)
        print('You will get 10% discount for your next purchase!')

    @classmethod
    def show_feedbacks(cls):
        super().show_feedbacks()

order_1=Cakes("Chocolate",500)
order_2=Cakes("Vanilla",800)
print("(1)**********************************")
order_1.cake_details()
print("(1.1)**********************************")
print(Cakes.order_list)
print("(2)**********************************")
order_2.add_customization("Zero","Butter Cream")
order_2.cake_details()
print("(3)**********************************")
Cakes.give_feedbacks("Chocolate Cake","Very Delicious")
Cakes.give_feedbacks("Chocolate Cake","Yummy")
print("(4)**********************************")
Cakes.show_feedbacks()
print("(5)**********************************")
ch_order1=Cheese_Cakes("Red velvet",700)
ch_order1.cake_details()
print("(6)**********************************")
ch_order1.add_customization()
print("(7)**********************************")
ch_order2=Cheese_Cakes("Blue Berry",900,"No Bake")
ch_order2.cake_details()
print("(8)**********************************")
print(Cakes.order_list)
print("(9)**********************************")
Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake","Average")
Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake","Liked it")
print("(10)**********************************")
Cakes.show_feedbacks()



#task 5