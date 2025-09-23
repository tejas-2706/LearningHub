class StudentRecord:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)
    


s1 = StudentRecord("tejas",23, (23,45,67,34,56))

print(s1.average())
print(s1.marks)
print(s1.name)
print(s1.roll_no)