#Classwork
#task 1
class KK_tea:
  total_sales1 = {'KK Regular Tea': 0}  # Class variable to track total sales

  def __init__(self, price, tea_bags):
    self.name = "KK Regular Tea"
    self.price = price
    self.tea_bags = tea_bags
    self.weight = self.tea_bags * 2
    self.status = False


  def product_detail(self):
    print(f"Name: {self.name}, Weight: {self.weight}")
    print(f"Tea Bags: {self.tea_bags}, Price: {self.price}")
    print(f"Status: {self.status}")
  @classmethod
  def update_sold_status_regular(cls,*teas):
    for tea in teas:
      tea.status = True
      KK_tea.total_sales1[tea.name] = KK_tea.total_sales1.get(tea.name, 0) + 1

  @classmethod
  def total_sales(cls):
    print("Total sales:", KK_tea.total_sales1)


class KK_flavoured_tea(KK_tea):
  def __init__(self, flavor, price, tea_bags):
    super().__init__(price, tea_bags)
    self.name = f"KK {flavor} Tea"
    self.weight = self.tea_bags * 2

  @classmethod
  def update_sold_status_flavoured(cls, *teas):
    for tea in teas:
      tea.status = True
      KK_tea.total_sales1[tea.name] = KK_tea.total_sales1.get(tea.name, 0) + 1


t1 = KK_tea(250, 50)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1,t2,t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()



#task 2
class TwoDVector:
  def __init__(self, x,y):
    self.__x = x
    self.__y = y
  def setx(self,p):
    self.__x=p
  def getx(self):
    return self.__x
  def sety(self,q):
    self.__y=q
  def gety(self):
    return self.__y
  def add2DVectors(self, *vectors):
    for i in vectors:
      self.__x += i.__x
      self.__y += i.__y
  def print2DVector(self):
    if self.__y >= 0:
      y = "+ "+str(self.__y)
    else:
      y = str(self.__y)
    print(f"{self.__x}i {y}j")
class ThreeDVector(TwoDVector):
  def __init__(self,x,y,z):
    super().__init__(x,y)
    self.__z=z
  def add3DVectors(self,*vectors):
    for i in vectors:
      self.add2DVectors(i)
      self.__z+=i.__z
  def print3DVector(self):
    if self.gety() >= 0:
      y = "+ "+str(self.gety())
    else:
      y = str(self.gety())
    if self.__z >= 0:
      z = "+ "+str(self.__z)
    else:
      z = str(self.__z)
    print(f"{self.getx()}i {y}j {z}k")
  def calculateLength(self):
    return ((((self.getx())**2)+((self.gety())**2)+((self.__z)**2))**(0.5))
  def multiplyScalar(self,b):
    self.setx(self.getx()*b)
    self.sety(self.gety()*b)
    self.__z*=b
TwoDV1 = TwoDVector(5, 6)
TwoDV2 = TwoDVector(3, 7)
TwoDV3 = TwoDVector(1, 8)
print("===============")
TwoDV1.add2DVectors(TwoDV2, TwoDV3)
TwoDV1.print2DVector()
print("===============")
ThreeDV1 = ThreeDVector(5, 6, 1)
ThreeDV2 = ThreeDVector(1, 9, -7)
ThreeDV3 = ThreeDVector(8, 2, 4)
print("===============")
ThreeDV1.add3DVectors(ThreeDV2,ThreeDV3)
ThreeDV1.print3DVector()
print("===============")
ThreeDV1.multiplyScalar(3)
ThreeDV1.print3DVector()
print("===============")
print(ThreeDV1.calculateLength())

 
#task 3
class File:
  files_directory = []
  def __init__(self, name, size, date_of_creation):
    self.name = name
    self.size = size
    self.date_of_creation = date_of_creation
    self.description = ''
    File.files_directory.append(self)
  def renameFile(self, n):
    self.name = n
  def updateDescription(self, txt):
    self.description = txt
  def previewFile(self):
    print(f"Name of file: {self.name}\nDescription: {self.description}\nSize: {self.size}\nDate created: {self.date_of_creation}")
  @classmethod
  def previewAllFiles(cls):
    for i in File.files_directory:
      print("===")
      i.previewFile()
class Audio(File):
  def __init__(self,name,size,date_of_creation,duration,lyrics=None):
    super().__init__(name,size,date_of_creation)
    self.duration=duration
    self.ldic=lyrics
    if lyrics==None:
      self.lyrics=' (no lyric available).'
    else:
      self.lyrics=': (Lyric is given below):\n'
  def playAudio(self):
    self.previewFile()
    print(f"Playing Audio file now for {self.duration}{self.lyrics}")
    if self.ldic!=None:
      for k,v in self.ldic.items():
        print(f"{k}:{v}")
class Image(File):
  def __init__(self,name,size,date_of_creation,resolution):
    super().__init__(name,size,date_of_creation)
    self.width,self.height=resolution.split('x')
  def displayPicture(self):
    for i in range(int(self.height)):
      for k in range(int(self.width)):
        print('*',end='')
      print()
print("----------1----------")
text_file = File("New file", "2 MB", "19 July 2020")
binary_file = File("Bin", "100 Kb", "20 August 2021")
print("----------2----------")
text_file.previewFile()
print("----------3----------")
audio_file1 = Audio("Class recording", "258 MB", "13th february 2023", "2 hours")
print("----------4----------")
audio_file1.updateDescription("Contains recordings of the CSE dept CSE111 Class")
print("----------5----------")
audio_file1.previewFile()
print("----------6----------")
audio_file1.playAudio()
print("----------7----------")

lyric = {'0:00-0:05':"I have been reading books of old",
         '0:06-0:10': "The legends and the myths",
         '0:11-0:15':"Achilles and his gold",
         '0:16-0:20':"Hercules and his gifts",
         '0:21-0:25':"Spider Man's control" ,
         '0:26-0:30':"And Batman with his fists",
         '0:31-0:35':"And clearly I don't see myself upon that list"}

print("----------8----------")
video_file2 = Audio("The squeeze podcast", "200 MB", "17th July 2023", "35 seconds", lyric)
print("----------9----------")
video_file2.playAudio()
print("----------10----------")
image_file1 = Image("name", "2MB", "31st July", "10x5")
print("----------11----------")
image_file1.displayPicture()
print("----------12----------")
Image.previewAllFiles()




#Homework

class Employee:
    employee_count = {}

    def __init__(self, name, joining_date, work_experience, weekly_work_hour=40):
        self.name = name
        self.joining_date = joining_date
        self.work_experience = work_experience
        if weekly_work_hour > 60:
            print("Error: Weekly work hour cannot exceed 60 hours. Setting to default (40 hours).")
            self.weekly_work_hour = 40
        else:
            self.weekly_work_hour = weekly_work_hour
        self.update_employee_count()

    def update_employee_count(self):
        employee_type = self.__class__.__name__
        Employee.employee_count[employee_type] = Employee.employee_count.get(employee_type, 0) + 1

    @classmethod
    def showDetails(cls):
        total_count = sum(cls.employee_count.values())
        print(f"Total Employee/s: {total_count}")
        for employee_type, count in cls.employee_count.items():
            print(f"Total {employee_type} Employee/s: {count}")





class Programmer(Employee):
    designation_list = [
        'Junior Software Engineer',
        'Software Engineer',
        'Senior Software Engineer',
        'Technical Lead'
    ]

    def __init__(self, name, joining_date, work_experience, weekly_work_hour=40):
        super().__init__(name, joining_date, work_experience, weekly_work_hour)
        self.id = self.createProgrammerID()
        self.designation = self.calculateDesignation()

    def calculateDesignation(self):
        if self.work_experience < 3:
            return 'Junior Software Engineer'
        elif self.work_experience < 5:
            return 'Software Engineer'
        elif self.work_experience < 8:
            return 'Senior Software Engineer'
        else:
            return 'Technical Lead'

    def showProgrammerDetails(self):
        print(f"Programmer Name: {self.name}")
        print(f"Programmer ID: {self.id}")
        print(f"Joining Date: {self.joining_date}")
        print(f"Designation: {self.designation}")
        print(f"Salary: BDT {self.calculateSalary()}")

    def calculateSalary(self):
        base_salary = {
            'Junior Software Engineer': 30000,
            'Software Engineer': 45000,
            'Senior Software Engineer': 70000,
            'Technical Lead': 120000
        }
        salary = base_salary[self.designation]
        for _ in range(self.work_experience):
            salary += (salary * 0.15)
        return round(salary)

    def calculateOvertime(self):
        overtime_hours = max(0, self.weekly_work_hour - 60)
        if overtime_hours > 0:
            overtime_pay = overtime_hours * 500
            print(f"{self.name} will get BDT {overtime_pay} overtime.")
            return overtime_pay
        else:
            print(f"{self.name} will not get overtime.")
            return 0

    def createProgrammerID(self):
        joined_date = self.joining_date.replace('-', '')
        return f'P-{joined_date}-{Employee.employee_count["Programmer"]}'


class HR(Employee):

    def __init__(self, name, joining_date, work_experience, weekly_work_hour=40):
        super().__init__(name, joining_date, work_experience, weekly_work_hour)
        self.id = self.createHREmployeeID()

    def showHREmployeeDeatails(self):
        print(f"HR Employee Name: {self.name}")
        print(f"HR Employee ID: {self.id}")
        print(f"Joining Date: {self.joining_date}")

    def createHREmployeeID(self):
        joined_date = self.joining_date.replace('-', '')
        return f'HR-{joined_date}-{Employee.employee_count["HR"]}'


class InternProgrammer(Employee):
    intern_count = 0

    def __init__(self, name, joining_date, intern_type='Unpaid'):
        super().__init__(name, joining_date, work_experience=0, weekly_work_hour=40)
        InternProgrammer.intern_count += 1
        self.temp_id = f'Temp_{InternProgrammer.intern_count}'
        self.intern_type = intern_type
        self.status = 'Eligible for promotion' if self.check_eligibility() else 'Not eligible for promotion'

    def check_eligibility(self):
        months_worked = (2023 - int(self.joining_date[:4])) * 12 + (8 - int(self.joining_date[5:7]))
        return months_worked >= 4

    def showInternDetails(self):
        print(f"Intern Programmer Name: {self.name}")
        print(f"Temporary ID: {self.temp_id}")
        print(f"Joining Date: {self.joining_date}")
        print(f"Intern Type: {self.intern_type}")
        print(f"Eligibility Status: {self.status}")

    def promoteToProgrammer(self):
        if self.check_eligibility():
            new_programmer = Programmer(self.name, self.joining_date, work_experience=0)
            new_programmer.showProgrammerDetails()
            print("The intern is promoted!")
            return new_programmer
        else:
            print("The intern cannot be promoted.")

Employee.showDetails()
print("=========1=========")
richard = Programmer("Richard Hendricks", "2021-06-08", 4, 48)
richard.calculateSalary()
print("=========2=========")
richard.showProgrammerDetails()
print("=========3=========")
richard.calculateOvertime()
print("=========4=========")
richard.showProgrammerDetails()
print("=========5=========")
monica = HR("Monica Hall", "2022-07-06", 2, 40)
print("=========6=========")
monica.showHREmployeeDeatails()
print("=========7=========")
Employee.showDetails()
print("=========8=========")
gilfoyle = Programmer("Bertram Gilfoyle", "2020-03-02", 6, 35)
gilfoyle.calculateSalary()
print("=========9=========")
gilfoyle.calculateOvertime()
print("=========10=========")
gilfoyle.showProgrammerDetails()
print("=========11=========")
gavin = Programmer("Gavin Belson", "2016-12-20", 9)
gavin.calculateSalary()
gavin.calculateOvertime()
gavin.showProgrammerDetails()
print("=========12=========")
yang = InternProgrammer("Jian Yang", "2023-01-01")
yang.showInternDetails()
print("=========13=========")
jared = InternProgrammer("Jared Dunn", "2023-06-05", "Paid")
jared.showInternDetails()
print("=========14=========")
jared = jared.promoteToProgrammer()
print("=========15=========")
Employee.showDetails()
print("=========16=========")
yang = yang.promoteToProgrammer()
yang.calculateSalary()
yang.showProgrammerDetails()
print("=========17=========")
Employee.showDetails()