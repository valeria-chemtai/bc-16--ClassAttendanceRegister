import os
import sys
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#create table called students
class Students(Base):
    __tablename__ = "students"
    student_name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True, autoincrement=True)
    in_session = Column(Boolean)
	

#create table called lessons
class Classes(Base):
    __tablename__ = "classes"
    class_name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    session_on = Column(Boolean)


#create table called log_hours
class Log(Base):
    __tablename__ = "log hours"
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey("classes.id"), primary_key=True, nullable=False)
    log_hours = relationship("Classes")
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True, nullable=False)
    log_hours = relationship("Students")
    start_time = Column(Float, nullable=False)
    end_time = Column(Float, nullable=False)
    check_out_reason = Column(String(250), nullable=False)


class User(Base):
	__tablename__ = "User_details"
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(250), nullable=False)
	password = Column(String(10), nullable=False)




engine = create_engine("sqlite:///myproject_database.db") #Create engine that stores data in local directory

Base.metadata.create_all(engine)   #create tables in the engine