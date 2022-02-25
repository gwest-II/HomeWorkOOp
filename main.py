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

    def average_grades(self):
        if len(self.grades.values()) > 0:
            return sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])
        else:
            return 0

    def __str__(self):
        return f'Name:{self.name}\nSurname:{self.surname}\nGPA:{self.average_grades()}\n' \
               f'Курсы в процессе изучения:{self.courses_in_progress}\n' \
               f'Завершенные курсы:{self.finished_courses}'

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.average_grades() < other.average_grades():
                return True
            else:
                return False
        else:
            pass

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
        return f'Name:{self.name}\nSurname:{self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.score = {}

    def gpa(self):
        if len(self.score.values()) > 0:
            return sum(list(self.score.values())[0]) / len(list(self.score.values())[0])
        else:
            return 0

    def __str__(self):
        return f'Name:{self.name}\nSurname:{self.surname}\nGPA:{self.gpa()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.gpa() < other.gpa():
                return True
            else:
                return False
        else:
            pass


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
cool_student = Student('Peter', 'Parker', 'male')
cool_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(cool_student, 'Python', 8)
cool_reviewer.rate_hw(cool_student, 'Python', 7)

cool_lecturer = Lecturer('Pop', 'Bronson')
cool_lecturer.courses_attached += ['Python']

best_lecturer = Lecturer('Robert', 'Bruce')
best_lecturer.courses_attached += ['Python']
best_student.lecturer_score(best_lecturer, 'Python', 10)
cool_student.lecturer_score(best_lecturer,'Python', 10)
best_student.lecturer_score(cool_lecturer, 'Python', 9)
best_student.lecturer_score(cool_lecturer, 'Python', 8)

print(best_student.grades)
print(cool_lecturer.score)
print(cool_student)
print(cool_lecturer < best_lecturer)
print(best_student < cool_student)