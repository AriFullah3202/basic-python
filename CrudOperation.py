course = []
while True:
    createlist = input("Enter choice ... what do you want to learn for course ? / add / read / update / delete / exit" , )
    if createlist == 'exit' :
        print('you exit from the course')
        break;
    elif createlist == 'read' :
        if len(course) == 0:
            print("you are not enrolled yet . please enroll the course")
        else:
            print("continue the course" , course)

    elif createlist == 'add':
            new_course = input("Enter the name of the course you want to add: ")
            course.append(new_course)
            print("Course added successfully!")

    elif createlist == 'update':
        if len(course) == 0:
            print("You are not enrolled in any courses yet. Please add a course first.")
        else:
            index = int(input("Enter the index of the course you want to update: "))
            if index < 0 or index >= len(course):
                print("Invalid index.")
            else:
                new_name = input("Enter the new name for the course: ")
                course[index] = new_name
                print("Course updated successfully!")

    elif createlist == 'delete':
        if len(course) == 0:
            print("You are not enrolled in any courses yet. Please add a course first.")
        else:
            index = int(input("Enter the index of the course you want to delete: "))
            if index < 0 or index >= len(course):
                print("Invalid index.")
            else:
                deleted_course = course.pop(index)
                print(f"Course '{deleted_course}' deleted successfully!")

    else:
        print("Incorrect input. Please try again.")