from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # зворотні зв'язки
    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=True)

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    # Зв'язок з предметом (для прикладу, 1 викладач може читати кілька предметів)
    subjects = relationship("Subject", back_populates="teacher")

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    grade_value = Column(Integer, nullable=False)
    date_of = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
