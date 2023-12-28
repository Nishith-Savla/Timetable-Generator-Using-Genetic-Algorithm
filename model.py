class Class:

    def __init__(self, groups, teacher, subject, type, duration, classrooms):
        self.groups = groups
        self.teacher = teacher
        self.subject = subject
        self.type = type
        self.duration = duration
        self.classrooms = classrooms

    def __str__(self):
        return f"Groups {self.groups} | Teacher '{self.teacher}' | Subject '{self.subject}' | Type {self.type} | {self.duration} hours | Classrooms {self.classrooms} \n"

    def __repr__(self):
        return str(self)


class Classroom:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f"{self.name} - {self.type} \n"

    def __repr__(self):
        return str(self)


class Data:

    def __init__(self, groups, teachers, classes, classrooms):
        self.groups = groups
        self.teachers = teachers
        self.classes = classes
        self.classrooms = classrooms
