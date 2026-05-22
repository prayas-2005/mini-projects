students = []

def add_student():
    name = input('Name :')
    father_name = input('Father Name :')
    roll_no = (int)(input('Roll No :'))
    course = input('Course :')
    
    student = {
        'name': name,
        'father_name': father_name,
        'roll_no': roll_no,
        'course': course
    }
    
    students.append(student)
    print('Student added successfully')
    
def view_information():
    for s in students:
        print('Name :', s['name'])
        print('Father_Name :', s['father_name'])
        print('Roll No :', s['roll_no'])
        print('Course :', s['course'])
        print('--'*20)

def search_student():
    search_roll = (int)(input("Enter student roll no to search"))
    for s in students:
        if s['roll_no'] == search_roll:
            print('Name :', s['name'])
            print('Father_Name :', s['father_name'])
            return
        print('Student not found')

def delete_student():
    del_roll = (int)(input("Enter student roll no to delete : "))
    for s in students:
        if s['roll_no'] == del_roll:
            students.remove(s)
            print('Student deleted successfully')
            return
        print('Student not found')



print('Welcome to the Student Management System')
print('--'*15)
print('1. Add Student Information')
print('2. View Information')
print('3. Search Information')
print('4. Delete Information')
print('5. Exit')
while True:    
    ch = (int)(input('Enter your choice :'))
    if (ch == 1):
        add_student()
    elif (ch == 2):
        view_information()
    elif (ch == 3):
        search_student()
    elif (ch == 4):
        delete_student()
    elif (ch == 5):
        print('Thank you for using the Student Management System')
        break
    else:
        print('Invalid choice, please try again')