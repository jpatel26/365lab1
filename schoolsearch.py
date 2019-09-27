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



# Convert list of attributes to a student object
# list -> Student
def createStudent(ls, students):
    new_student = Student(ls[0], ls[1], ls[2], ls[3], ls[4], ls[5], ls[6], ls[7])
    students.append(new_student)

# Read students.txt and populate the students list
def readStudentsFile(students):
    filepath = 'students.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            mystring = line.strip()
            mylist = mystring.split(",")
            createStudent(mylist, students)
            line = fp.readline()

def main():

    # A global list for students
    students = []
    readStudentsFile(students)

    # The prompt loop
    while True:
        q = input('Please enter a query. Example queries:\n\nS[tudent]: <lastname>'
        '[B[us]]\nT[eacher]: <lastname>\nB[us]: <number>\nG[rade]: <number>'
        '[H[igh]|L[ow]]\nA[verage]: <number>\nI[nfo]\nQ[uit]\n\n')
        attrs = ["StLastName", "StFirstName"]
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

        if len(q.split()) < 2:
            continue

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
                print("")
            else:
                avgGPA = total / numStudents
                print(grade, round(avgGPA, 2))
            continue

        # Grade
        if "Grade:" in q or "G:" in q:
            split = q.split()
            grade = int(split[1])
            status = "" if len(split) <= 2 else split[2]
            st = None
            attr = ["StLastName", "StFirstName", "GPA", "Bus", "TLastName", "TFirstName"]
            if status == "High" or status == "H":
                highest = 0
                for s in students:
                    if (str(grade) == str(s.Grade)) and (float(s.GPA) > float(highest)):
                        st = s
                        highest = float(s.GPA)
                if st:
                    print(st.StLastName, st.StFirstName, st.GPA, st.Bus, st.TLastName, st.TFirstName)
            elif status == "Low" or status == "L":
                lowest = 100
                for s in students:
                    if (str(grade) == str(s.Grade)) and (float(s.GPA) < float(lowest)):
                        st = s
                        lowest = float(s.GPA)
                if st:
                    print(st.StLastName, st.StFirstName, st.GPA, st.Bus, st.TLastName, st.TFirstName)
            else:
                seq_search("Grade", q.split()[1], attr, students)

        if "Teacher:" in q or "T:" in q:
            seq_search("TLastName", q.split()[1], ["StLastName", "StFirstName"], students)

        if "Bus" in q or "B:" in q:
            seq_search("Bus", q.split()[1], ["StLastName", "StFirstName", "Grade", "Classroom"], students)

        if "Student" in q or "S:" in q:
            split = q.split()
            if len(split) == 3 and (split[2] == "B" or split[2] == "Bus"):
                seq_search("StLastName", split[1], ["StLastName", "StFirstName", "Bus"], students)
            else:
                attrs = ["StLastName", "StFirstName", "Grade", "Classroom", "TLastName", "TFirstName"]
                seq_search("StLastName", split[1], attrs, students)

        print("")

# attr: string, inp: string, print_attrs: list
# Takes the attribute to search, the given input, and a list of attributes to print, prints out all students within
# params
def seq_search(attr, inp, print_attrs, students):
    str = ""
    for s in students:
        if getattr(s, attr) == inp:
            str += ",".join(getattr(s, a) for a in print_attrs) + "\n"
    print(str)

if __name__ == "__main__":
    main()


