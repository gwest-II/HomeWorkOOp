class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def lecturer_score(self, lecturer, course, score):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.score:
                lecturer.score[course] += [score]
            else:
                lecturer.score[course] = [score]
        else:
            return 'Error'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Name:{self.name}\nSurname:{self.surname}'
        return some_reviewer


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.score = {}
        self.grade_score = []

    def gpa(self):
        self.grade_score =self.score.values() / len(self.score)

    def __str__(self):
        some_lecturer = f'Name:{self.name}\nSurname:{self.surname}\nGPA:{self.grade_score}'
        return some_lecturer

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Pop', 'Bronson')
cool_lecturer.courses_attached += ['Python']
best_student.lecturer_score(cool_lecturer, 'Python', 9)
best_student.lecturer_score(cool_lecturer, 'Python', 8)

some_reviewer = cool_reviewer
some_lecturer = cool_lecturer
print(best_student.grades)
print(cool_lecturer.score)
print(some_lecturer)