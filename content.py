"""This part of the code links the CLI to the database"""
from tabulate import tabulate
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database import Students, Classes, Log, User

#initiate link to the database for operation
engine = create_engine("sqlite:///myproject_database.db")
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class attendance_register:
	def __init__(self):
		pass

	#check_in method
	def check_in(self):
		#Check if student in database first
		status = eval(input("Is student registered(True or False)?  "))

		if status == False:
			#Take user to Add_student method with a prompt message
			print("Add Student to register and check in from Add panel")

			attendance_register.student_add(self) 		#call the student_add function
			print("Student registered and checked in")

		else:
			status = eval(input("Is student In another class(True or False)? "))

			if status == False:
				student_id = int(input("Enter student Id:  "))
				class_id = int(input("Enter class Id in mind:  "))
				session.execute(update(Students).where(Students.id==student_id).values({"in_session":True, "class_id":class_id}))
				session.commit()
				print("Student Successfully assigned class")

			else:
				print("First check out student in current class to check in to another")

	#Check_out method
	def check_out(self):
		student_id = int(input("Enter student Id: ")) #prompt for student Id

		in_session = eval(input("Is student in session: (True or False)?:  ")) #check if student is in session

		if in_session == True:
			check_out_reason = str(input("Enter reason for checking out:  "))  #Reason for check out

			#change value of in_session in students table to False
			session.execute(update(Students).where(Students.id==student_id).values({"in_session":False, "class_id":0}))
			session.commit()

			print("Student checked_out successfully")

		else:
			print("Can not check out student")

	#method for initiating log_start
	def log_start(self):
		class_id = int(input("Enter the class id:  "))
		class_in =Log(class_id=class_id)

		start = str(input("Enter start time:  "))		
		starting = Log(class_id=class_id, start_time=start)
		session.add(starting)
		session.commit()

		log= []
		rows = session.query(Log).all()
		for row in rows:
			log.append((row.class_id, row.start_time, row.end_time))
		print(tabulate(log, headers=["class_id", "start_time", "end_time"], tablefmt="orgtbl"))

	#method for log end
	def log_end(self):
		class_id = int(input("Enter class id: "))
		
		end= str(input("Enter end time:  "))
		
		session.execute(update(Log).where(Log.class_id==class_id).values({"end_time":end}))
		session.commit()

		log= []
		rows = session.query(Log).all()
		for row in rows:
			log.append((row.class_id, row.start_time, row.end_time))
		print(tabulate(log, headers=["class_id", "start_time", "end_time"], tablefmt="orgtbl"))


	#Method to add student and automatically generate their id
	def student_add(self):
		new = input("Enter both first and surname separate with space:  ")     #prompt user for both names separated by a space or one name
		new_student = Students(student_name=new)

		in_class = eval(input("Is student in class: (True or False): "))
		student_session = Students(student_name=newStudent, in_session=in_class)			

		if in_class == True:
			class_id = int(input("Enter id of class in:  "))
			
		else:
			class_id = 0

		class_in = Students(student_name=new, in_session=in_class, class_id=clas_id)
		session.add(class_in)
		session.commit()

	#method to delete particular student based on their id
	def student_remove(self):
		student_id = int(input("Enter student id in question: "))
		session.query(Students).filter_by(id=student_id).delete()
		session.commit()


	#method to add new class and automatically generate an id		
	def class_add(self):
		new = input("Enter The Name of Class: ")
		new_class = Classes(class_name=new)

		class_on = eval(input("is the class in session(True or False):  "))
		class_session = Classes(class_name=new, session_on=class_on)
		session.add(class_session)
		session.commit()

	def class_remove(self):
		class_id = int(input("Enter id in question:  "))
		session.query(Classes).filter_by(id=class_id).delete()
		session.commit()
		
	def class_list(self):
		classes = []
		rows = session.query(Classes).all()
		for row in rows:
			classes.append((row.class_name, row.id, row.session_on))
		print(tabulate(classes, headers=["class_name", "id", "session_on"], tablefmt="orgtbl"))

	def student_list(self):
		students = []
		rows = session.query(Students).all()
		for row in rows:
			students.append((row.student_name, row.id, row.in_session, row.class_id))
		print(tabulate(students, headers=["student_name", "id", "in_session", "class_id"], tablefmt="orgtbl"))