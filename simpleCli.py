from content import AttendanceRegister

def main():
	while True:
		print("selcet an option")
		print("\n1.Check in\n 2.Check out\n 3.Log start\n 4.Log end\n 5.student add\n 6.student remove\n 7.class add\n 8.class remove\n 9.class list\n 10.student list")
		option = int(input("enter a value"))
		register = AttendanceRegister()
		if option == 1:
			register.check_in()

		elif option == 2:
			register.check_out()

		elif option == 3:
			register.Log_start()

		elif option == 4:
			register.Log_end()

		elif option == 5:
			register.student_add()

		elif option == 6:
			register.student_remove()

		elif option == 7:
			register.class_add()

		elif option == 8:
			register.class_remove()

		elif option ==9:
			print(register.class_list())

		elif option == 10:
			print(register.student_list())
		

if __name__ == "__main__": main()

