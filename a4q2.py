# David Emmanuel

# 11298443

# doe869

# jason coutu

students_list=[]
AES_list=[]

def create_student_list():
    global students_list
    students_list=[("kiara james", 50, False), ("michael jordan", 60, True),
                ("John snow", 32, False), ("Mirabel bell", 25, True),
                ("Sarah blue", 19, True), ("Randy orton", 44, False),
                ("Randy john", 21, False), ("Stephen mark", 29, True),
                ("Vanessa willy", 23, True), ("Bell sam", 80, True)]

def register_student():
    global students_list
    student_name = input("Enter Student Name: ")
    student_number = int(input("Enter Student Number: "))
    isAES = bool(int(input("Is Student AES ? 0 for False & 1 for True: ")))
    students_list.append((student_name, student_number, isAES))

def create_AES_list():
    global students_list, AES_list
    AES_list = [n for n in students_list if n[2] == True]

def delete_student():
    global students_list
    student_number = int(input("Enter Student number to unregister: "))
    for i in range(len(students_list)):
        if students_list[i][1] == student_number:
            del students_list[i]
            break

def print_students_info():
    global students_list
    for i in range(len(students_list)):
        print(students_list[i][0] + " | " + str(students_list[i][1]) + " | " + str(students_list[i][2]))

def print_AES_students_info():
    global AES_list
    for i in range(len(AES_list)):
        print(AES_list[i][0] + " | " + str(AES_list[i][1]) + " | " + str(AES_list[i][2]))

while True:
    print("1. Create Student List")
    print("2. Register a Student")
    print("3. Delete a Student")
    print("4. AES student list")
    print("5. Display student information")
    print("6. Display AES student information")
    print("7. Quit")
    inp = int(input("Enter Your Choice: "))
    if inp == 1:
        create_student_list()
    elif inp == 2:
        register_student()
    elif inp == 3:
        delete_student()
    elif inp == 4:
        create_AES_list()
    elif inp == 5:
        print_students_info()
    elif inp == 6:
        print_AES_students_info()
    else:
        break