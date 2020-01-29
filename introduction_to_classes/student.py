#! /usr/bin/env python3.7

"""Simple class representing a student."""


class Student:
    """Model a student."""

    def __init__(self, first="", last="", student_id=0):
        """Init a Student object.

        Keyword Arguments:
            first {str} -- The student's first name. (default: {''})
            last {str} -- The student's last name. (default: {''})
            student_id {int} -- The student's ID number. (default: {0})
        """
        self._first = first
        self._last = last
        self._student_id = student_id
        self._gpa = 3.98

    def __str__(self):
        """Return a nicely formatted string representing the student."""
        return f"{self._student_id}: {self._first} {self._last}"


if __name__ == "__main__":
    student1 = Student("Carrol", "Smith", 1234)
    student2 = Student()

    print(student1)
    print(student2)
