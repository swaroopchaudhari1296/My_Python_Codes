class Student:
  marks = 0

  def compute_marks(cls, obtained_marks):
    cls.marks = obtained_marks
    print('Obtained Marks:', cls.marks)

# convert compute_marks() to class method
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(88)

# Output: Obtained Marks: 88
