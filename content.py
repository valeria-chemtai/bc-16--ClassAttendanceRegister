from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database import Students, Classes, Log_start, User

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
		student_id = int(input("Enter student Id: "))

		in_session = bool(input("Is student in session: (True or False)?: "))
		if in_session == True:
			check_out_reason = str(input("Enter reason for checking out: "))
			


			session.add(Students(in_session=False))
			session.commit()



			print("Student checked_out successfully")

		else:
			print("Can not check out student")

	def log_start(self):
		clas_id = int(input("Enter the class id: "))
		class_in =Log_start(class_id=clas_id)

		start = eval(input("Enter start time: "))
		starting = Log_start(class_id=clas_id, start_time=start)
		session.add(starting)
		session.commit()


	def log_end(self):
		clas_id = int(input("Enter class id: "))
		class_out = Log_start(class_id=clas_id)

		end= eval(input("Enter end time"))
		ending = Log_end(class_id=clas_id, end_time=end)
	def student_add(self):
		newStudent = input("Enter both first and surname separate with space: ")
		new_student = Students(student_name=newStudent)

		in_class = eval(input("Is student in class: (True or False): "))
		student_session = Students(student_name=newStudent, in_session=in_class)
			

		if in_class == True:
			classId = int(input("Enter id of class in: "))
			
		else:
			classId = 0

		class_in = Students(student_name=newStudent, in_session=in_class, class_id=classId)
		session.add(class_in)
		session.commit()


	def student_remove(student_id):
		student_id = int(input("Enter student id in question: "))
		session.query(Students).filter_by(id=student_id).delete()
		session.commit()	
		
	def class_add(self):
		newClass = input("Enter The Name of Class: ")
		new_class = Classes(class_name=newClass)
		
		class_on = eval(input("is the class in session(True or False): "))
		class_session = Classes(class_name=newClass, session_on=class_on)
		session.add(class_session)
		session.commit()

		#if class_on == True:
		#	number_of_students = int(input("Enter No. of Students currently in class: "))
		#else:
		#	number_of_students = 0

		#total = Classes(class_name=newClass, session_on=class_on, total_students=number_of_students)
		#session.add(total)
		#session.commit()



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
			students.append((row.student_name, row.id, row.in_session, row.class_id))
		return students

	