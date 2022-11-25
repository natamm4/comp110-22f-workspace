class Student:
    email: str

    def __init__(self, email: str):
        self.email = email


class Gradebook:
    grades: dict[Student. float]

    def __init__(self):
        self.grades = {}

    def add_student(self, student: Student, grade: float) -> None:
        self.grades[student] = grade

    def outreach(self) -> list[str]:
        emails: list[str] = []
        for student in self.grades:
            if self.grades[student] < 75:
                emails.append(student.email)
        return emails



def main():
    comp110: Gradebook = Gradebook()
    comp110.add_student(Student("bob@email.unc.edu"), 84.2)
    comp110.add_student(Student("sarah@email.unc.edu"), 54.2)
    comp110.add_student(Student("kris@email.unc.edu"), 14.2)
    print(comp110.outreach())


if __name__ == '__main__':
    main()