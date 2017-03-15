from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database import Students, Classes

engine = create_engine("sqlite:///myproject_database.db")

Base = declarative_base()

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


class AttendanceRegister(object):
	def __init__(self):
		pass

	def check_in(self, student_id, class_id):
		pass
	def check_out(self):
		student_name = str(input("Enter student name: "))

		in_session = eval(input("Is student in session: (True or False)?"))
		if in_session == True:
			check_out_reason = str(input("Enter reason for checking out: "))
			valid_reason = Log(reason=check_out_reason)
			session.add(valid_reason)
			session.commit()

			session.add(Students(in_session=False))
			session.commit()



			print("Student checked_out successfully")

		else:
			print("Can not check out student")

	def log_start(self):


	def log_end(self):
		pass
	def student_add(self):
		newStudent = input("Enter both first and surname separate with space: ")
		new_student = Students(student_name=newStudent)
		session.add(new_student)
		session.commit()

		in_class = bool(input("Is student in class: (True or False): "))
		student_session = Students(student_name=newStudent, in_session=in_class)
		session.add(student_session)
		session.commit()	


	def student_remove(student_id):
		student_id = int(input("Enter student id in question: "))
		session.query(Students).filter_by(id=student_id).delete()
		session.commit()	
		
	def class_add(self):
		newClass = input("Enter The Name of Class: ")
		new_class = Classes(class_name=newClass)
		session.add(new_class)
		session.commit()

		class_on = bool(input("is the class in session(True or False): "))
		class_session = Classes(class_name=newClass, session_on=class_on)
		session.add(class_session)
		session.commit()

	def class_remove(self):
		class_id = int(input("Enter id in question: "))
		session.query(Classes).filter_by(id=class_id).delete()
		session.commit()
		
	def class_list(self):
		classes = []
		rows = session.query(Classes).all()
		for row in rows:
			classes.append((row.class_name, row.id, row.session_on))
		return classes

	def student_list(self):
		students = []
		rows = session.query(Students).all()
		for row in rows:
			students.append((row.student_name, row.id, row.in_session))
		return students

	