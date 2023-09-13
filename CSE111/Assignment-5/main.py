#Classwork
#task 1
class Student:
    def __init__(self,name,id,cg):
        self.name = name
        self.__id = id
        self.__cg = cg
    def getID(self):
        return self.__id
    def setId(self,x):
        self.__id = x
    def getcg(self):
        return self.__cg
    def setcg(self,x):
        self.__cg = x
class Department:
    def __init__(self,dep):
        self.dep = dep
        self.stu_dict ={}
        self.stud = 0
    def addStudent(self,*stu):
        for i in stu:
            if i.getID() not in self.stu_dict.keys():
                self.stu_dict[i.getID()] = [i.name,i.getcg()]
                print(f'Welcome to {self.dep} department, {i.name}')
                self.stud += 1
            else:
                print('Student with the same ID already exists, Please try with another ID')
    def findStudent(self,x):
        if x not in self.stu_dict.keys():
            print("Student with this ID doesn't exist, Please give a valid ID")
        else:
            for i,j in self.stu_dict.items():
                if x == i:
                    print(f'Student info:\nStudent Name: {j[0]}\nID: {i}\nCGPA: {j[1]}')

    def details(self):
        print(f'Department Name: {self.dep}\nNumber of student: {self.stud}\nDetails of the students:')
        for i,j in self.stu_dict.items():
            print(f'Student name: {j[0]}, ID: {i}, cgpa: {j[1]}')



s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()



#task 2
class Spaceship:
    def __init__(self,name,cap):
        self.name = name
        self.cap = cap
        self.w = 0
        self.cargo = []
    def load_cargo(self,g):
        if g.getweight() > self.cap - self.w:
            print(f'Warning: Unable to load {g.getName()} inside {self.name}. Exceeds capacity by {g.getweight() - (self.cap-self.w)}.')
        else:
            self.cargo.append(g.getName())
            self.cap - g.getweight()
            self.w += g.getweight()
    def display_details(self):
        print(f'Spaceship Name: {self.name}\nCapacity: {self.cap}\nCurrent Cargo Weight: {self.w}\nCargo: {self.cargo}')

class Cargo:
    def __init__(self,name,weight):
        self.__name = name
        self.__weight = weight

    def getName(self):
        return self.__name
    def setName(self,x):
        self.__name = x
    def getweight(self):
        return self.__weight
    def setweight(self,x):
        self.__weight = x

# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()


 
#task 3
class Song:
    def __init__(self, title, duration, artist="Unknown Artist"):
        self.__title = title
        self.__artist = artist
        self.__duration = duration

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def info(self):
        minutes = self.__duration // 60
        seconds = self.__duration % 60
        return f"{self.__title} by {self.__artist} ({minutes}:{seconds:02})"


class Playlist:
    def __init__(self, name, song_list= []):
        self.__name = name

        self.__song_list = song_list
        self.__now_id = -1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_song_list(self):
        return self.__song_list

    def set_song_list(self, song_list):
        self.__song_list = song_list

    def get_now_id(self):
        return self.__now_id

    def set_now_id(self, now_id):
        self.__now_id = now_id

    def play_next(self):
        if self.__now_id == len(self.__song_list) - 1:
            self.__now_id = 0
        else:
            self.__now_id += 1

    def play_prev(self):
        if self.__now_id == 0:
            print("Cannot go back from the first song.")
            self.__now_id = 0
        else:
            self.__now_id -= 1

    def add_songs(self, *songs):
        for song in songs:
            self.__song_list.append(song)

    def remove_song(self, x):
        self.__song_list.remove(x)

    def show_playlist(self):
        print(f"Playlist: {self.__name}")
        print(f"Total Songs: {len(self.__song_list)}")
        i= 1
        for song in self.__song_list:
            print(f"{i}. {song.info()}")
            i += 1


song1 = Song("Never Gonna Give You Up", 213, "Rick Astley")
song2 = Song("The Flower Duet", 86, "Leo Delibes")
song3 = Song("Winter", 223, "Vivaldi")
song4 = Song("Ride of the Valkyries", 137, "Wagner")
song5 = Song('Amar Sonar Bangla', 250, 'Kazi Najrul Islam')

playlist = Playlist("Rap")
playlist.add_songs(song1,song2,song3,song4,song5)

playlist.show_playlist()

playlist.play_next()
playlist.show_playlist()
playlist.remove_song(song4)
playlist.play_prev()
playlist.show_playlist()

playlist.play_prev()
playlist.show_playlist()




#Homework

class Book:
    def __init__(self, title, author, genre):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = True
        self.__borrower = None

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_availability(self):
        return self.__available

    def set_availability(self, available):
        self.__available = available

    def get_borrower(self):
        return self.__borrower

    def set_borrowed(self, borrower):
        self.__available = False
        self.__borrower = borrower

    def display_info(self):
        if self.__available is True:
          status = 'Available'
        else:
          status = "Borrowed by " + self.__borrower.get_name()
        print(f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Status: {status}")


class LibraryMember:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_books = []

    def get_member_id(self):
        return self.__member_id

    def set_member_id(self, member_id):
        self.__member_id = member_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def borrow_book(self, book):
        if not book.get_availability():
            print(f"'{book.get_title()}' is already borrowed by someone else.")
            return
        book.set_borrowed(self)
        self.__borrowed_books.append(book)

        print(f"{self.__name} has borrowed '{book.get_title()}'")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.set_availability(True)

            self.__borrowed_books.remove(book)
            print(f"{self.__name} has returned '{book.get_title()}'")
        else:
            print(f"{self.__name} did not borrow '{book.get_title()}'")

    def display_borrowed_books(self):
        print(f"Borrowed books by {self.__name}:")
        for book in self.__borrowed_books:
            print(f" - {book.get_title()}")


class Library:
    def __init__(self):
        self.__books_available = []
        self.__library_members = []

    def add_book(self, book):
        self.__books_available.append(book)

    def add_library_member(self, member):
        self.__library_members.append(member)

    def display_book_list(self):
        print("Available books in the library:")
        for book in self.__books_available:
            book.display_info()

    def display_library_members(self):
        print("Library Members:")
        for member in self.__library_members:
            print(f" - {member.get_name()} (Member ID: {member.get_member_id()})")


book1 = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fiction")
book2 = Book("Nothing Lasts Forever", "Sidney Sheldon", "Fiction")
book3 = Book("Calculus", "Gilbert Strang", "Education")
member1 = LibraryMember("22101397", "Abdul Ahad")
member2 = LibraryMember("22101356", "Madhuri Mazumder")
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_library_member(member1)
library.add_library_member(member2)
print("All the books in library are:")
library.display_book_list()
member1.borrow_book(book1)
member1.borrow_book(book2)
member2.borrow_book(book3)
member1.display_borrowed_books()
print("======================================")
member2.display_borrowed_books()
print("======================================")
print("All the books in library are:")
library.display_book_list()
member1.return_book(book1)
member1.display_borrowed_books()
print("======================================")
library.display_book_list()
print("All library members:")
library.display_library_members()
