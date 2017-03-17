
from content import attendance_register

def main():
	#prompt user for an option
	while True:
		print("\nselect an option")
		print(" \n 1.Check in\n 2.Check out\n 3.Log start\n 4.Log end\n 5.student add\n 6.student remove\n 7.class add\n 8.class remove\n 9.class list\n 10.student list\n 0.Exit\n")

		option = int(input("Select Option: "))
		register = attendance_register()

		if option == 1:
			register.check_in() #call function check_in from attendance_register
			print(register.student_list()) 	#Added for demonstration purposes

		elif option == 2:
			register.check_out()	#call function check_out from attendance_register
			print(register.student_list()) 	#Added for demonstration purposes

		elif option == 3:
			register.log_start()	#call function log_start from attendance_register
			print("Class session started")

		elif option == 4:
			register.log_end()	#call function log_end from attendance_register
			print("class Session ended")

		elif option == 5:
			register.student_add()
			print(register.student_list()) 	#Added for demonstration purposes, this line of code can be omitted

		elif option == 6:
			register.student_remove()
			print(register.student_list())  #Added for demonstration purposes

		elif option == 7:
			register.class_add()
			print(register.class_list())

		elif option == 8:
			register.class_remove()

		elif option == 9:
			print(register.class_list())

		elif option == 10:
			print(register.student_list())

		elif option == 0:
			break				#system exit

		else:
			print("Enter a Valid option")
		

if __name__ == "__main__": main()

