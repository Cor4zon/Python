from collections import defaultdict

students = {
    "Ben":  [90, 91],
    "Jude": [88, 77],
    "Paul": [99, 100],
}


def get_marks_naive(name):
    if name in students:
        return students[name]
    return []


def get_marks_better(name):
    return students.get(name, [])


def get_marks_with_assigment_naive(name):
    if name not in students:
        students[name] = []
    return students[name]


def get_marks_with_assigment_better(name):
    return students.setdefault(name, [])


def set_grades_naive(name, score):
    if name not in students:
        students[name] = []
    grades = students[name]
    grades.append(score)


def set_grades_better(name, score):
    grades = get_marks_with_assigment_better(name)
    grades.append(score)


# print(get_marks_naive("Ben"))
# print(get_marks_naive("Bella"))
# print(get_marks_better("Paul"))
# print(get_marks_better("Poul"))

# print(get_marks_with_assigment_naive("Ben"))
# print(get_marks_with_assigment_naive("Bob"))
# print(get_marks_with_assigment_better("Paul"))
# print(get_marks_with_assigment_better("Pamela"))

# set_grades_naive("John", 55)
# set_grades_better("Ben", 100)
# set_grades_better("Jude", 100)
# print(students.items())

students = defaultdict(list)


def set_grades_best(name, grade):
    students[name].append(grade)



students = defaultdict(lambda: 55)

print(students["Jack"])
print(students["Jack"] + 10)
print(students["Jack"])
students["Jack"] += 10
print(students["Jack"])