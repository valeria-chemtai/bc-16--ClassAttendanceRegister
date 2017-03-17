"""Database setup for class attendance register"""
import os
import sys
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#create table called students with columns student_name, id, in_session, class_id
class Students(Base):
    __tablename__ = "students"
    student_name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True, autoincrement=True)
    in_session = Column(Boolean, nullable=True)
    class_id = Column(Integer, nullable=True)

#create table called classes with columns class_name, id, session_on, 
class Classes(Base):
    __tablename__ = "classes"
    class_name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_on = Column(Boolean, nullable=True)
    
#create table called Log_start with columns class_id, start_time, end_time
class Log(Base):
    __tablename__ = "log"
    class_id = Column(Integer, primary_key=True,nullable=False)
    start_time = Column(String, primary_key=True, nullable=False)
    end_time = Column(String, primary_key=True, nullable=True)

class User(Base):
	__tablename__ = "user_details"
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(250), nullable=False)
	password = Column(String(10), nullable=False)


engine = create_engine("sqlite:///myproject_database.db") #Create engine that stores data in local directory

Base.metadata.create_all(engine)   #create tables in the engine