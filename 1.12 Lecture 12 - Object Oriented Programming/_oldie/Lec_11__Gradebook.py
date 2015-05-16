from Lec_10__Examples import *


class Grades(object):
    """ A mapping from students to a list of grades """
    def __init__(self):
        """ Create empty grade book """
        self.students = []    # list of Student objects
        self.grades   = {}    # maps idNum -> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        """ Assumes: student is of type Student
            Add student to the grade book """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """ Assumes: grade is a float
            Add grade to the list of grades for student """
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """ Return a list of grades for student """
        try:  # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """ Return a list of the students in the grade book """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]  # return copy of list of students


def gradeReport(course):
    """ Assumes: course is of type grades """
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)

for s in six00.allStudents():
    six00.addGrade(s, 75)
six00.addGrade(g1, 25)
six00.addGrade(g2, 100)

six00.addStudent(ug3)

print gradeReport(six00)