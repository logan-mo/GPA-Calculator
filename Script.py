

class Subject:

    GPA = 0

    def __init__(self, name, creditHours, grade):
        self.name = name
        self.creditHours = creditHours
        self.grade = grade
        self.calculation()

    def calculation(self):
        self.qualityPoints = self.grade_to_Quality_points()
        self.points = self.total_points()
        self.subjectGPA()

    def grade_to_Quality_points(self):
        grade_points = {
            'A' : 4.00,
            'A-': 3.67,
            'B+': 3.33,
            'B' : 3.00,
            'B-': 2.67,
            'C+': 2.33,
            'C' : 2.00,
            'C-': 1.67,
            'D+': 1.33,
            'D' : 1.00,
            'F' : 0.00
        }

        if self.grade not in grade_points:
            print("Invalid Grade")
            raise ValueError

        return grade_points.get(self.grade)

    def total_points(self):
        points = self.qualityPoints * self.creditHours
        return points

    def subjectGPA(self):
        Subject.GPA += (self.points/self.creditHours)
        return Subject.GPA
    
    def output(self):
        print("")
        pass

def totalGPA(GPAs):
        global subjects
        return GPAs/subjects    

if __name__ == "__main__":  

    outputFile = open("output.txt", "w")

    subjects = int(input("How many subjects did you study?"))

    outputFile.writelines("\tSUBJECTS\tCREDIT HOURS\tGRADE\n")

    for x in range(subjects):
        print("Subject #",x , ":")

        subjectName = input("\tName: ")
        creditHours = int(input("\tCredit Hours (Lab + Theory): "))
        grade = input("\tGrade :")

        subject = Subject(subjectName, creditHours, grade)

        outputFile.writelines("%i\t%s\t\t%i\t\t%s\n" %(x,subjectName,creditHours,grade))

    GPA = totalGPA(Subject.GPA)
    outputFile.writelines("GPA = %s" %GPA)
    outputFile.close()
    
    with open("output.txt") as readFile:
        for line in readFile:
            print(line)