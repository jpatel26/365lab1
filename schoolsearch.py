# A class representing a student
class Student:
    def __init__(self, StLastName, StFirstName, Grade, Classroom,
            Bus, GPA, TLastName, TFirstName):
        self.StLastName = StLastName
        self.StFirstName = StFirstName
        self.Grade = Grade
        self.Classroom = Classroom
        self.Bus = Bus
        self.GPA = GPA
        self.TLastName = TLastName
        self.TFirstName = TFirstName

# A global list for students
students = []

# Convert list of attributes to a student object
# list -> Student
def createStudent(ls):
    new_student = Student(ls[0], ls[1], ls[2], ls[3], ls[4], ls[5], ls[6], ls[7])
    students.append(new_student)

# Read students.txt and populate the students list
def readStudentsFile():
    filepath = 'students.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            mystring = line.strip()
            mylist = mystring.split(",")
            createStudent(mylist)
            line = fp.readline()


readStudentsFile()

# The prompt loop
while True:
    q = input('Please enter a query. Example queries:\n\nS[tudent]: <lastname>'
    '[B[us]]\nT[eacher]: <lastname>\nB[us]: <number>\nG[rade]: <number>'
    '[H[igh]|L[ow]]\nA[verage]: <number>\nI[nfo]\nQ[uit]\n\n')
    
    # Switch statement

    # Information 
    if q == "Info" or q == 'I':
        print("Information")
        grades = [0,0,0,0,0,0,0]
        for s in students:
            grades[int(s.Grade)] = grades[int(s.Grade)] + 1
            x = 0
        for g in grades:
            print(str(x) + ":" + str(g))
            x = x + 1
        print("")
        continue

    # Quit
    if q == "Quit" or q == 'Q':
        break

    # Average
    if "Average:" in q or "A:" in q:
        grade = int(q.split(":")[1])
        total = 0
        numStudents = 0
        for s in students:
            if str(s.Grade) == str(grade):
                numStudents = numStudents + 1
                total = total + float(s.GPA)
        if numStudents == 0:
            print("There are no students in grade ", grade, "\n")
        else:
            avgGPA = total / numStudents
            print("The average GPA for grade ", grade, " is ", avgGPA)
        continue

    # Grade 
    if "Grade:" in q or "G:" in q: 
        grade = int(q.split(" ")[1])
        status = q.split(" ")[2]
        st = None
        if status == "High" or status == "H":
            highest = 0
            for s in students:
                if (str(grade) == str(s.Grade)) and (float(s.GPA) > float(highest)):
                    st = s
                    highest = float(s.GPA)
            if st:
                print("Name: ", st.StFirstName, st.StLastName, 
                        " GPA: ", st.GPA, " Bus: ", st.Bus, " Teacher: ", 
                        st.TFirstName, st.TLastName)
            highest = 0
            st = None
        elif status == "Low" or status == "L":
            lowest = 100
            for s in students:
                if (str(grade) == str(s.Grade)) and (float(s.GPA) < float(lowest)):
                    st = s
                    lowest = float(s.GPA)
            if st:
                print("Name: ", st.StFirstName, st.StLastName, 
                        " GPA: ", st.GPA, " Bus: ", st.Bus, " Teacher: ", 
                        st.TFirstName, st.TLastName)
            lowest = 100
            st = None

    print("")
        

        
