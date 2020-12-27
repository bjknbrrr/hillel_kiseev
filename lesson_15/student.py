class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        self.__grades = grades

    def add_grade(self, grade):
        self.__grades.append(grade)

    def __str__(self):
        return 'Name: {n}, age: {a}, grades: {g}'.format(
            n=self.__name,
            a=self.__age,
            g=', '.join(str(grade) for grade in self.__grades)
        )


# s1 = Student('Tom', 25)
# lst = [6, 7, 3, 6, 9, 12]
# s1.grades = lst
# print(s1)
# del lst
# print(s1)

