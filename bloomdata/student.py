import random


class Student():
    '''
    Class String: 
    '''
    def __init__(self, name, age, school) -> None:
        self.name = name
        self.age = age
        self.school = school


    def introduce_self(self):
        return f'''Hello! My name is {self.name}.
                I am {self.age} years old.
                I attend {self.school}'''
    
    def birthday(self):
        self.age += 1


class BloomTechStudent(Student):
    '''
    Class string:
    '''
    def __init__(self, name, age, school, track, cohort) -> None:
        super().__init__(name, age, school)
        self.track = track
        self.cohort = cohort
        self.graduated = False

    def flex(self):
        self.cohort += 1

    def graduate(self):
        self.graduated = True


def student_generator(num_students= 30):
    '''Function string:
    '''
    first_names = ['Ricardo', 'Sindy', 'Elizabeth', 'Victor', 'Gabriel', 'Mary']
    last_names = ['Ruiz', 'Garcia', 'Bueso', 'Castro', 'Serrano', 'Andino']

    random_first_name = random.choice(first_names)
    random_last_name = random.choice(last_names)

    random_name = random_first_name + ' ' + random_last_name

    age = random.randint(18, 60)

    school = 'Bloomtech'

    track = random.choice(['WEB', 'DS', 'Backend'])
    cohort = random.randint(1, 50)

    students = []

    for _ in range(num_students):
        students.append(BloomTechStudent(
            random_name, age, school, track, cohort))
    
    return students


student_list = student_generator()
print(student_list)

# print(student_list[0].name)
# print(student_list[0].age)
# print(student_list[0].school)
# print(student_list[0].introduce_self())
# student_list[0].birthday()
# print(student_list[0].age)
# print(student_list[0].track)
# print(student_list[0].cohort)
# student_list[0].flex()
# print(student_list[0].cohort)
# student_list[0].graduate()
# print(student_list[0].graduated)
