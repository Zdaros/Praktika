# Priklad 1
import sqlite3
# Клас для що описує працівників підприємства
class Worker():
 def __init__(self, **kwargs):
  self.name = kwargs.get('name')
  self.position = kwargs.get('position')
  self.work_from_date = kwargs.get('work_from_date')
  self.birth_date = kwargs.get('birth_date')
 def get_data(self):
  return self.name, self.position, self.work_from_date, self.birth_date

# створення екземпляра класу працівник з використанням непозиційних параметрів у конструкторі
w1 = Worker(name='Petrov Vadym', position='manager',
work_from_date='09-12-2019', birth_date='18-02-1990')
conn = sqlite3.connect("staff_db.db")
cursor = conn.cursor()
# Створення таблиці після першого запуску скрипта потрібно закоментувати
cursor.execute("""CREATE TABLE staff (name text, position text, work_from_date text, birth_date text)""")
# Створення першого запису в таблиці "вручну"
cursor.execute("""INSERT INTO staff VALUES ('Ivanov Ivan', 'director', '07-10-2019',  '2-12-1980')""")
# Створення першого запису в таблиці із екземпляра класу Worker
cursor.execute("""INSERT INTO staff VALUES (?,?,?,?)""", w1.get_data())
# Зберігаємо зміни
conn.commit()
# Вставляємо список з трьох працівників
all_workers = [('Borysov Mykola', 'ingeneer', '23-11-1976', '04-12-2019'), ('Pavlyik Inna', 'secretary', '12-09-1991', '22-01-2020'), ('Kolodych Leonid', 'ingeneer', '16-08-1986', '13-01-2020')]
cursor.executemany("INSERT INTO staff VALUES (?,?,?,?)",
all_workers)
conn.commit()
# Виведення на екран всіх записів

print("Записи в таблиці бази даних у вигляі списка:")
sql = "SELECT * FROM staff"
cursor.execute(sql)
print(cursor.fetchall())
# Редагування запису для конкретного працівника
sql = """ UPDATE staff SET position = 'main ingeneer' WHERE name = 'Kolodych Leonid' """
cursor.execute(sql)
conn.commit()
# Виводимо список всіх інженерів
print("Список всіх ingeneer:")
sql = "SELECT * FROM staff WHERE position=?"
cursor.execute(sql, [("ingeneer")])
print(cursor.fetchall())
# Виведення на екран всіх записів
print("Список всіх записів в таблиці:")
for row in cursor.execute("SELECT rowid, * FROM staff ORDER BY name"):
 print(row)

# Task 1

class Srudent_grades:
    name = ""
    num_of_lectiones = 0
    max_grade = 0
    num_of_praktic_sesons = 0
    cursor = None

    lections_visited = []
    grades_praktic = []
    def __init__(self, cursor):
        self.cursor = cursor
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

    def db_add_data (self):
        cursor.execute("""INSERT INTO Student VALUES ('""" + self.name + """', '""" + str(self.num_of_lectiones)+ """', '""" + str(self.max_grade) + """',  '""" + str(self.num_of_praktic_sesons) + """',  '""" + str(self.grade_return()) + """')""")
    def db_delete_data (self, name_to_delete):
        cursor.execute("""DELETE FROM Student WHERE name='""" + name_to_delete + """'""")
    def db_search (self, name):
        for row in cursor.execute("""SELECT * FROM Student WHERE name='""" + name+"""'"""):
            print(row)
conn = sqlite3.connect("Student_db.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE Student (name text, num_of_lectiones text, max_grade text, num_of_praktic_sesons text, av_grade text)""")

s1 = Srudent_grades(cursor)
s1.grades_p_init(5,2)
s1.lection_init(2)
print(s1.grade_return())
s2 = Srudent_grades(cursor)
s2.grades_p_init(5,2)
s2.lection_init(2)
print(s2.grade_return())

s1.db_add_data()
s2.db_add_data()
s1.db_search("Andrew Freziuk")
print()

for row in cursor.execute("""SELECT * FROM Student"""):
    print (row)
