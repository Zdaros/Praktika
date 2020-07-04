# Priklad 1

class Student:
 def set_marks(self, e1, e2, e3):
  self.e1 = e1
  self.e2 = e2
  self.e3 = e3
 def set_name(self, name):
  self.name = name
 def get_average_mark(self):
  print(self.name, ' - ', ((self.e1 + self.e2 + self.e3) / 3))
s1 = Student()
s2 = Student()
s1.set_name('Dmytro')
s1.set_marks(5, 4, 5)
s1.get_average_mark()
s2.set_name('Mykola')
s2.set_marks(4, 4, 4)
s2.get_average_mark()

# Task

class Srudent_grades:
    name = ""
    num_of_lectiones = 0
    max_grade = 0
    num_of_praktic_sesons = 0

    lections_visited = []
    grades_praktic = []
    def __init__(self):
        self.name = input("Enter name of a student: ")
        self.num_of_lectiones = int(input("Enter number of lectiones: "))
        self.max_grade = int(input("Enter the max grade:"))
        self.num_of_praktic_sesons = int(input("Enter nubert of praktic sesones: "))
        for i in range(0,self.num_of_praktic_sesons):
            self.grades_praktic.append(0)
        for i in range(0,self.num_of_lectiones):
               self.lections_visited.append(False)
                
    def grades_p_init (self,grade,num_of_praktic_s):
        if num_of_praktic_s > 0 and num_of_praktic_s <= self.num_of_praktic_sesons and grade > -1 and grade <= self.max_grade:
            self.grades_praktic[num_of_praktic_s-1] = grade

    def lection_init (self,lection_num_visited):
        if lection_num_visited > 0 and lection_num_visited <= self.num_of_lectiones:
            self.lections_visited[lection_num_visited-1] = True

    def grade_return (self):
        num = 0
        sum_ = 0
        for grade in self.grades_praktic:
            sum_ += grade
            num += 1
        return sum_ / num

s1 = Srudent_grades()
s1.grades_p_init(5,2)
s1.lection_init(2)
print(s1.grade_return())
