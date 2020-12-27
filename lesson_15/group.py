
class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_students(self, *students):
        for student in students:
            self.__students.append(student)

    def __str__(self):
        return 'Group: {g}\n{st}\n'.format(
            g=self.__name,
            st='\n'.join(str(s) for s in self.__students)
        )



