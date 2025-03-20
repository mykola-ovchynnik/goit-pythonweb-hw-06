import random
from faker import Faker
from app.database import SessionLocal
from app.models import Group, Student, Teacher, Subject, Grade


def create_groups(session, fake):
    groups = []
    for i in range(3):
        group = Group(name=f"Group_{fake.word().capitalize()}")
        session.add(group)
        groups.append(group)
    return groups


def create_teachers(session, fake):
    teachers = []
    for _ in range(4):
        t = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(t)
        teachers.append(t)
    return teachers


def create_subjects(session, teachers):
    subjects = []
    subject_names = ["Math", "Science", "History", "Art", "Music", "Physical Education"]
    for name in subject_names:
        subj = Subject(
            name=name,
            teacher=random.choice(teachers)
        )
        session.add(subj)
        subjects.append(subj)
    return subjects


def create_students(session, fake, groups):
    students = []
    for _ in range(30):
        st = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group=random.choice(groups)
        )
        session.add(st)
        students.append(st)
    return students


def create_grades(session, students, subjects):
    for student in students:
        for _ in range(random.randint(10, 20)):
            grade = Grade(
                student=student,
                subject=random.choice(subjects),
                grade_value=random.randint(60, 100)
            )
            session.add(grade)


def create_fake_data():
    fake = Faker()
    session = SessionLocal()

    groups = create_groups(session, fake)
    teachers = create_teachers(session, fake)
    subjects = create_subjects(session, teachers)
    session.commit()

    students = create_students(session, fake, groups)
    session.commit()

    create_grades(session, students, subjects)
    session.commit()
    session.close()


if __name__ == "__main__":
    create_fake_data()
