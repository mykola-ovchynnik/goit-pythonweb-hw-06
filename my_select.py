import logging
from sqlalchemy import func, desc
from app.database import SessionLocal
from app.models import Student, Grade, Subject, Teacher, Group

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def select_1():
    session = SessionLocal()
    result = (session.query(Student.id, Student.first_name, Student.last_name,
                            func.round(func.avg(Grade.grade_value), 2).label("avg_grade"))
              .join(Grade, Student.id == Grade.student_id)
              .group_by(Student.id, Student.first_name, Student.last_name)
              .order_by(desc("avg_grade"))
              .limit(5)
              .all())
    session.close()
    return result

def select_2(subject_id: int):
    session = SessionLocal()
    result = (session.query(Student.id, Student.first_name, Student.last_name,
                            func.avg(Grade.grade_value).label("avg_grade"))
              .join(Grade, Student.id == Grade.student_id)
              .filter(Grade.subject_id == subject_id)
              .group_by(Student.id)
              .order_by(desc("avg_grade"))
              .first())
    session.close()
    return result

def select_3(subject_id: int):
    session = SessionLocal()
    result = (session.query(Group.name, func.round(func.avg(Grade.grade_value), 2).label("avg_grade"))
              .join(Student, Group.id == Student.group_id)
              .join(Grade, Student.id == Grade.student_id)
              .filter(Grade.subject_id == subject_id)
              .group_by(Group.id)
              .all())
    session.close()
    return result

def select_4():
    session = SessionLocal()
    result = session.query(func.round(func.avg(Grade.grade_value), 2)).scalar()
    session.close()
    return result

def select_5(teacher_id: int):
    session = SessionLocal()
    result = (session.query(Subject.name)
              .join(Teacher, Subject.teacher_id == Teacher.id)
              .filter(Teacher.id == teacher_id)
              .all())
    session.close()
    return result

def select_6(group_id: int):
    session = SessionLocal()
    result = (session.query(Student.id, Student.first_name, Student.last_name)
              .filter(Student.group_id == group_id)
              .all())
    session.close()
    return result

def select_7(group_id: int, subject_id: int):
    session = SessionLocal()
    result = (session.query(Student.id, Student.first_name, Student.last_name, Grade.grade_value)
              .join(Grade, Student.id == Grade.student_id)
              .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
              .all())
    session.close()
    return result

def select_8(teacher_id: int):
    session = SessionLocal()
    result = (session.query(func.round(func.avg(Grade.grade_value), 2).label("avg_grade"))
              .join(Subject, Grade.subject_id == Subject.id)
              .filter(Subject.teacher_id == teacher_id)
              .scalar())
    session.close()
    return result

def select_9(student_id: int):
    session = SessionLocal()
    result = (session.query(Subject.name)
              .join(Grade, Subject.id == Grade.subject_id)
              .filter(Grade.student_id == student_id)
              .distinct()
              .all())
    session.close()
    return result

def select_10(student_id: int, teacher_id: int):
    session = SessionLocal()
    result = (session.query(Subject.name)
              .join(Grade, Subject.id == Grade.subject_id)
              .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
              .distinct()
              .all())
    session.close()
    return result

if __name__ == "__main__":
    logger.info("Top 5 students with the highest average grade: %s", select_1())
    logger.info("Student with the highest average grade in subject 1: %s", select_2(subject_id=1))
    logger.info("Average grade in groups for subject 2: %s", select_3(subject_id=2))
    logger.info("Average grade across all subjects: %s", select_4())
    logger.info("Courses taught by teacher 1: %s", select_5(teacher_id=1))
    logger.info("List of students in group 1: %s", select_6(group_id=1))
    logger.info("Grades of students in group 1 for subject 2: %s", select_7(group_id=1, subject_id=2))
    logger.info("Average grade given by teacher 1: %s", select_8(teacher_id=1))
    logger.info("Courses attended by student 1: %s", select_9(student_id=1))
    logger.info("Courses taught by teacher 1 to student 1: %s", select_10(student_id=1, teacher_id=1))