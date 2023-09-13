import csv
class BracPepol:
    departmentCodeDict = {
        'Archi': 1, 'CSE': 2, 'ESS': 3, 'EEE': 4, 'ENH': 5,                          #Given DeptCodeDict
        'MNS': 6, 'Pharma': 7, 'BBS': 8, 'Law': 9
    }
    serial_number = 1                                                                # Initialize the serial number as per as the total data

    def __init__(self, name, gender, location, birthdate, blood_group, phone, department, enrolled_year,
                 completed_credits, current_cgpa):
        self.name = name
        self.gender = gender
        self.location = location
        self.birthdate = birthdate
        self.blood_group = blood_group
        self.phone = phone
        self.department = department
        self.enrolled_year = enrolled_year
        self.completed_credits = int(completed_credits)
        self.current_cgpa = float(current_cgpa)
        self.student_id = self.generate_student_id()

    def generate_student_id(self):
        if self.department in BracPepol.departmentCodeDict:
            department_code = BracPepol.departmentCodeDict[self.department]
        else:
            department_code = 0

        serial_number = f"{str(BracPepol.serial_number).zfill(4)}"                              # Format serial number with leading zeros(Thats the work of zFill Func[more in https://www.w3schools.com/python/ref_string_zfill.asp])
        student_id = f"{self.enrolled_year[-2:]}{department_code}{serial_number}"
        BracPepol.serial_number += 1                                                            # Increment the serial number
        return student_id


    @classmethod
    def read_students_from_csv(cls, csv_filename):
        students = []
        with open(csv_filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)                                                         # filtering the first row
            for row in csv_reader:
                student = cls(*row)                                                  # Main line of the project where We are sending each row with its location which will have a unique id per row
                students.append(student)
        return students
    @classmethod
    def male_female_ratio(cls, students):
        male_count = 0
        for i in students:
            if i.gender == 'Male':
                male_count += 1
        female_count = len(students) - male_count
        print(f"Male-Female Ratio: {male_count}:{female_count}")
        print()

    @classmethod
    def sibling_from_another_mother(cls, students, year, month=None):
        matched_students = []
        if month is not None:                                                          # month has value so we check both year and month
            for i in students:
                birthday_components = i.birthdate.split(", ")                          # Split the birthdate into its components
                birth_year = birthday_components[-1]                                   # Get the birth year
                birth_month = birthday_components[1][:3]                               # Get the first three characters of the birth month and avoid the date.
                if birth_year == year and birth_month == month:                        # match the birth year and month and filter out the names.
                    matched_students.append(i.name)
        else:                                                                          # month is none
            for i in students:
                birthday_components = i.birthdate.split(", ")                          # Split the birthdate into its components
                birth_year = birthday_components[-1]                                   # Get the birth year
                if birth_year == year:
                    matched_students.append(i.name)

        print(matched_students)
        # for name in matching_students:
        #     print(name)
        print()

    @classmethod
    def available_blood_donor_by_location(cls, all_Students, blood_group, location, count=10):
        c = 1
        matched_students = []
        for i in all_Students:                                                                    #first we iterate over all student data and match 2 criteria we need
            if i.blood_group == blood_group and i.location == location:
                matched_students.append((i.name, i.phone))                                        #we append those values in tuple so when we print we can unpack two value in per turn of a loop
                if len(matched_students) == count:
                    break
        print("Available Blood Donors by location:")
        for name, phone in matched_students:
            print(f"{c}. Name: {name}, Phone: {phone}")
            c += 1
        print()

    @classmethod
    def available_blood_donor_by_dept(cls, students, blood_group, dept=None, count=10):
        c = 1
        matching_students = []
        if dept is None:
            m_c = 0                                                                              #this is for the 25 counting as the dept is none
            for i in students:
                if i.blood_group == blood_group:
                    matching_students.append((i.name, i.phone, i.location))
                    m_c += 1
                if m_c == 25:
                    break
        else:
            for i in students:
                if i.blood_group == blood_group and i.department == dept:
                    matching_students.append((i.name, i.phone, i.location))
                    if len(matching_students) == count:
                        break
        print("Available Blood Donors by Department:")
        for name, phone, address in matching_students:                                            #Tuple Unpacking
            print(f"{c}. Name: {name}, Phone: {phone}, Address: {address}")
            c += 1
        print()
    @classmethod
    def generate_probation_student_info(cls, students, dept="CSE"):
        c = 1
        print(f"Probation Students in {dept} Department:")
        for i in students:
            if i.department == dept and i.current_cgpa < 2.00:
                print(f"{c}. Name: {i.name}, ID: {i.student_id}, Department: {i.department}, Phone: {i.phone}, CGPA: {i.current_cgpa:.2f}")
                c += 1
        print()
    @classmethod
    def find_valedictorian_candidates(cls, students):
        sorted_students = sorted(students, key=lambda x: (x.current_cgpa, x.completed_credits, x.enrolled_year), reverse=True)                   #Sorting on descending order
        print("Top 5 Valedictorian Candidates:")
        count = 1
        # print(sorted_students)
        for i in sorted_students:
            if i.completed_credits >= 130:
                print(f"{count}. Name: {i.name}, UID: {i.student_id}, Department: {i.department}, CGPA: {i.current_cgpa:.2f}")
                count += 1
                if count == 6:
                    break
        print()

    @classmethod
    def find_gold_medalist_candidates(cls, students):
        c = 1
        gold_medalists = {}
        for i in students:
            if i.completed_credits >= 130:
                if i.department not in gold_medalists or i.current_cgpa > gold_medalists[i.department].current_cgpa:
                    gold_medalists[i.department] = i
        print("Gold Medalist Candidates:")
        for dept, student in gold_medalists.items():
            print(f"{c}. Department: {dept}, Name: {student.name}, UID: {student.student_id}, CGPA: {student.current_cgpa}")
            c += 1
        print()
    @classmethod
    def find_female_coder_championship_candidates(cls,students):
        c = 1
        female_coders = []
        for i in students:
            if i.gender == 'Female' and i.department == 'CSE' and i.current_cgpa > 3.5 and i.completed_credits >= 30:
                female_coders += [i]
        female_coders.sort(key=lambda x: x.completed_credits)                                                                             #Sorting on ascending order
        print("Female Coder Championship Candidates:")
        for student in female_coders[:10]:
            print(f"{c}. Name: {student.name}, UID: {student.student_id}")
            c += 1
        print()
    @classmethod
    def find_SIM_users(cls, students, operatorName):
        c = 1
        Number_Info = {                                                                                                                  #Operator detection dictionary
            "Grameenphone": [3, 7],
            "Banglalink": [4, 9],
            "TeleTalk": [5],
            "Robi": [6, 8]
        }
        matched_students = []
        for i in students:
            for j,k in Number_Info.items():
                if operatorName == j:
                    if int(i.phone[5]) in k:                                                                                           #checking the value of the key that determine operator
                        matched_students += [i]
        print(f"Students using {operatorName} SIM:")
        for i in matched_students:
            print(f"{c}. Name: {i.name}, Location: {i.location}, Phone: {i.phone}")
            c += 1


csv_filename = 'F:\Project\data.csv'   # Provide the correct path to the CSV file
students = BracPepol.read_students_from_csv(csv_filename)
BracPepol.male_female_ratio(students)
BracPepol.sibling_from_another_mother(students, "2000", "Jun")                                         #here the main student with the rows of locations are passing in the class codes
BracPepol.available_blood_donor_by_location(students, "AB+", "Wari")
BracPepol.available_blood_donor_by_dept(students, "B+")
BracPepol.generate_probation_student_info(students, dept= "BBS")
BracPepol.find_valedictorian_candidates(students)
BracPepol.find_gold_medalist_candidates(students)
BracPepol.find_female_coder_championship_candidates(students)
BracPepol.find_SIM_users(students, "TeleTalk")
