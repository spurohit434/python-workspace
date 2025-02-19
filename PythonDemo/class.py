class Person:
    def __init__(self, new_full_name):
        print("parent called")
        self.full_name = new_full_name

    def get_full_name(self):
        return self.full_name


class Student(Person):
    def __init__(self, new_grades, new_name, new_full_name):
        super().__init__(new_full_name)
        print("Student called")
        self.grades = new_grades
        self.name = new_name

    def get_average(self):
        return sum(self.grades)/len(self.grades)




s1 = Student([88,91,99,97], "Jose", "Jose Peter Dave")
s2 = Student([88,93,95,90], "Sam", "Sam Immanuel")
print("New grades are:", s1.get_average(), "Name:", s1.full_name)
print("New grades are:", s2.get_average(), "Name:", s2.full_name)
print(s1.__class__)

# calling the methods of the student class without
# 1st method
print(s1.get_full_name())    # here we are calling the methods of the person using the object of the student class
print(Person.get_full_name(s1)) # here we are caliing the methods of the person class by creating an static function type implementation and python uses this under the hood
