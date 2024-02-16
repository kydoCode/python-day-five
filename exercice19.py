class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def add_mark(self, mark):
        self.marks.append(mark)
    
    def compute_average(self):
        return sum(self.marks) / len(self.marks)

    def display_data(self):
        print(self.name)
        print(self.age)
        print(self.compute_average())

studentOne = Student("Eric", 24, [14, 12, 17])
studentTwo = Student("Jessica", 26, [8, 12, 13, 7])
studentThree = Student("Paresseux", 18, [6, 4, 8, 10])
studentFour = Student("Einstein", 22, [18, 17, 16, 19])

studentOne.add_mark(13)
studentOne.display_data()
studentThree.compute_average()
studentThree.display_data()
studentFour.display_data()