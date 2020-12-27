from lesson_15.student import Student
from lesson_15.group import Group


st1 = Student('Ivan', 25)
st1.grades = [5, 5, 5, 5, 4, 5]
st2 = Student('Petr I', 35)
st2.grades = [4, 4, 3, 4, 5, 5]
st3 = Student('Sergey', 20)
st3.grades = [2, 3, 4, 3, 2, 1]

g = Group('PTD-123')
g.add_students(st1, st2, st3)
print(g)
