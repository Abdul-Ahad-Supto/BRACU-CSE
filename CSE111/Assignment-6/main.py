#Classwork
#task 1
class NikeBangladesh:
    brance = []
    d = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    s = 0
    def __init__(self, outlet):
        self.outlet = outlet
        self.sold = 0
        NikeBangladesh.brance.append(self.outlet)
    def details(self):
        print(f'Nike Dhaka Banani outlet:\nProducts Currently Stocked:\n{NikeBangladesh.d}\nSold: {self.sold}')
    def restockProducts(self,di):
        for i,j in di.items():
            for l,k in NikeBangladesh.d.items():
                if i == l:
                    NikeBangladesh.d[l] += j
    @classmethod
    def status(cls):
        print(f'Nike Bangladesh Status:\nBranches Opened: {NikeBangladesh.brance}\nCureently Stocked\n{NikeBangladesh.d}\nSold: {NikeBangladesh.s}')

    def productSold(self,sold):
        for i,j in sold.items():
            for l,k in NikeBangladesh.d.items():
                if l == i:
                    NikeBangladesh.d[l] -= j
                    self.sold += j
                    NikeBangladesh.s += j


print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
    {"Air Jordan": 1200, "Cortez": 200, "Zoom Kobe": 200})
chittagong.restockProducts(
    {"Air Jordan": 1000, "Cortez": 250, "Zoom Kobe": 100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan": 760, "Cortez": 90})
chittagong.productSold({"Air Jordan": 520, "Zoom Kobe": 70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()


#task 2
class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice


class Quiz:
    total_quizzes = 0

    def __init__(self, quiz_name):
        self.name = quiz_name
        self.questions = []
        self.score = 0

    def add_question(self, *questions):
        self.questions.extend(questions)

    @classmethod
    def create_from_data(cls, quiz_name, question_data_list):
        quiz = cls(quiz_name)
        for data in question_data_list:
            question = Question(data['text'], data['choices'], data['correct_choice'])
            quiz.add_question(question)
        return quiz

    def attempt(self):
        print(f"--- {self.name} ---")

        for question in self.questions:
            print(question.text)
            for index, choice in enumerate(question.choices, start=1):
                print(f"{index}. {choice}")

            user_choice = int(input("Your answer (enter the choice number): "))

            if user_choice == question.correct_choice:
                self.score += 1
                print("Correct answer! 1 point for you.")
            else:
                print("Wrong answer!")

        print(f"Your total score: {self.score}/{len(self.questions)}")

# Test the Quiz Maker

quiz1 = Quiz("Math Quiz")

quiz1_question1 = Question("What is the result of 2 + 2?", ["3", "4", "5"], 2)
quiz1_question2 = Question("What is the result of 3 * 6?", ["15", "18", "20"], 2)

quiz1.add_question(quiz1_question1, quiz1_question2)

python_quiz_data = [
    {
        'text': "What is the keyword to define a function in Python?",
        'choices': ["func", "def", "function"],
        'correct_choice': 2
    },
    {
        'text': "Which one is NOT a built-in data type in Python?",
        'choices': ["int", "str", "double"],
        'correct_choice': 3
    }
]

quiz2 = Quiz.create_from_data("Python Quiz", python_quiz_data)

print("Total no. of quizzes: ", Quiz.total_quizzes)

quiz1.attempt()
quiz2.attempt()

 
#task 3
class Foodiz:
  total_sell = 0
  branch_info = []

  def __init__(self, branch_name):
    self.branch_name = branch_name
    self.branch_sell = 0
    Foodiz.branch_info.append(self)

  def sell_quantity(self, quantity):
    self.branch_sell = quantity * 300
    Foodiz.total_sell += self.branch_sell

  def branch_information(self):
    print(f"Branch Name: {self.branch_name}")
    print(f"Branch Sell: {self.branch_sell} Taka")


  @classmethod
  def details(cls):
    print(f"Total Number of branch(s): {len(cls.branch_info)}")
    print(f"Total Sell: {cls.total_sell} Taka")
    print("########################")
    for branch in cls.branch_info:
      print(f"Branch Name: {branch.branch_name}")
      print(f"Branch Sell: {branch.branch_sell} Taka")
      contribution = (branch.branch_sell / cls.total_sell) * 100 if cls.total_sell > 0 else 0
      print(f"Branch consists of total sell's: {contribution:.2f}%")



# Driver code
Foodiz.details()
print('1----------------------------------')
mohakhali = Foodiz('Mohakhali')
mohakhali.sell_quantity(25)
mohakhali.branch_information()
print('2----------------------------------')
Foodiz.details()
print('3========================')
banani = Foodiz('Banani')
banani.sell_quantity(15)
banani.branch_information()
print('4----------------------------------')
Foodiz.details()
print('5========================')
gulshan = Foodiz('Gulshan')
gulshan.sell_quantity(9)
gulshan.branch_information()
print('6----------------------------------')
Foodiz.details()




#Homework

class Movie:
    def __init__(self,name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration
    def movieInfo(self):
        return f'Movie Name: {self.name}\nMovie Genre: {self.genre}\nMovie Duration: {self.duration} minutes.'
    @classmethod
    def createMovie_fromString(cls,string):
        lst = string.split('-')
        return cls(lst[0], lst[1], lst[2])
class StarCinema:
    all_branch_info = {}
    def __init__(self,branch_name):
        self.branch_name = branch_name
        print(f'Welcome to the {self.branch_name} branch of StarCinema! ')
        self.movie_list = []
        self.movie_list.append(self.branch_name)
        if len(StarCinema.all_branch_info) == 0:
            StarCinema.all_branch_info[self.branch_name] = []
    def addMovies(self, *movie_objects):
        if self.branch_name not in StarCinema.all_branch_info.keys():
            StarCinema.all_branch_info[self.branch_name] = []
        for l in movie_objects:
            if l in self.movie_list:
                print('Movie is already added in this branch.')
            else:
                print(f'{l.name} added to {self.branch_name} branch. ')
                self.movie_list.append(l)
                StarCinema.all_branch_info[self.branch_name].append(l)
    def removeMovie(self, movie_object):
        if movie_object in self.movie_list:
            self.movie_list.remove(movie_object)
            StarCinema.all_branch_info[self.branch_name].remove(movie_object)
            print(f"Movie '{movie_object.name}' has been removed from the branch.")
        else:
            print(f"Movie '{movie_object.name}' is not found in this branch.")
    @classmethod
    def check(cls, string):
        streaming = False
        g = []
        d = []
        for i, j in StarCinema.all_branch_info.items():
            for k in j:
                if k.name == string:
                    print(f"'{string}' is being streamed in {i} branch.")
                    streaming = True
                    if len(g) == 0 and len(d) == 0:
                        g = k.genre
                        d = k.duration
        if streaming:
            print(f'It is of {g} genre and {d} minutes duration.')
        if not streaming:
            print(f"Movie '{string}' is not being streamed in any branch.")


    @classmethod
    def showAllBranchInfo(cls):
        for i, j in StarCinema.all_branch_info.items():
            print(f"Branch Name: {i}")
            c = 1
            for k in j:
                print(f"Movie No: {c}")
                c += 1
                print(k.movieInfo())
                print("..............................................")



movie1 = Movie('Oppenheimer', 'Biographical Drama', 180)
movie2 = Movie('Barbie', 'Fantasy Comedy', 114)
movie3 = Movie('Mission: Impossible – Dead Reckoning Part One', 'Action', 163)
print('1==========================================')
print(movie3.movieInfo())
print('2==========================================')
movie4 = Movie.createMovie_fromString('Prohelika-Drama-153')
print('3==========================================')
print(movie4.movieInfo())
print('4==========================================')
branch1 = StarCinema('Mohakhali')
print('5==========================================')
branch1.addMovies(movie1, movie2, movie4)
print('6==========================================')
branch1.addMovies(movie1, movie3)
print('7==========================================')
StarCinema.showAllBranchInfo()
print('8==========================================')
branch2 = StarCinema('Mirpur')
print('9==========================================')
branch2.addMovies(movie1, movie2, movie3)
print('10==========================================')
StarCinema.showAllBranchInfo()
print('11==========================================')
StarCinema.check('Oppenheimer')
print('12=========================================')
StarCinema.check('Sound of Freedom')
print('13=========================================')
branch1.removeMovie(movie2)
StarCinema.showAllBranchInfo()
print('14=========================================')
branch2.removeMovie(movie1)
StarCinema.showAllBranchInfo()