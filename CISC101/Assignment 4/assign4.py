"""
This program contains 6 functions. 1 - Print students marks, 2 - Calculate average for the assignment, 3 - Calculate student's average,
4 - Print list of students with the highest mark, 5 - Increase all marks by 1, 6 - Add a new student and their marks to the list.
Then main() function runs all of them with different data.

Author:  D.Zaichenko
Student Number: 20378257
Date: 26 Oct 2022
"""

def printMark(students, name):
    """
    This function takes two parameters, students list and the name of a student.
    It prints student's assignment marks and print "No student found" if there's no student with the entered name.
    """ 
    
    check = 0
    
    for row in range(len(students)):
        if name in students[row]:
            check += 1                  #If student's name is in the list then check = 1
            new_list = students[row]    #Copying the list with entered name to the new list. [name, marks]
    
    if check == 1:
        print('The marks for', name, 'are:')    #Print students marks from the created list
        print('    A1:', new_list[1][0])
        print('    A2:', new_list[1][1])
        print('    A3:', new_list[1][2])
        print('    A4:', new_list[1][3])
    
    else:
        print('No student found by that name')  #If check != 1 (name is not in the list)

    
def averageAssignment(students, assignment):
    """
    This function takes two parameters, list of students and the assignment number.
    It calculates the assignment average and returns it. If the number of assignment is out of range,
    then the function returns -999.
    """

    total = 0
    
    if assignment >= 0 and assignment <= 3:     #Assignment number is between 0 and 3 (1-4)
        for k in range(len(students)):
            total += students[k][1][assignment] #Adds the entered assignment mark to the total
        total = total / len(students)       #Calculates the average
        return format(total, ',.2f')        #Returns formatted total
    
    else:
        return -999     #Assignment number is out of range, returns -999


def averageMark(list, name):
    """
    This function takes two parameters, list of students and student's name. 
    Returns the average overall mark for that student.  
    If the student name doesn't exist, it returns 0.
    """
    
    check = 0
    
    for row in range(len(list)):    #I use the same approach to check if entered name is in the list
        if name in list[row]:
            new_list = list[row]    #Creating a new list [name, marks] for the convenience
            check += 1
    
    if check == 1:
        return sum(new_list[1]) / 4     #Calculating the average
    else:
        return 0    #The function returns 0 if the name is not in the list.

    
def highestAverageMark(students):
    """
    This function takes one parameter, list of students and marks.
    It uses the previous function to calculate the average for all students,
    then returning the list of students with highest marks.
    """
    
    final = []      #Final list of student names with highest averages
    marks = []      #List of average marks
    names = []      #List of student names
    
    for k in range(len(students)):
        marks.append(averageMark(students, students[k][0]))     #Adds all averages to marks list
        names.append(students[k][0])                            #Adds all names to names list
    
    max_mark = max(marks)       #Calculates the max average and assigns it to the max_mark variable
    
    for b in range(len(marks)):
        if marks[b] == max_mark:
            final.append(names[b])  #If the mark in marks list equals to the max_mark variable, it adds the name of the student (with the same index as the mark) 
                                    #to the final list. 
    
    return final        #Returns the list of names with highest averages



def increaseMarks(students):
    """
    This function takes one parameter, list of students and marks.
    It adds 1 to all marks.
    """
   
    for k in range(len(students)):
        for b in range(len(students[k][1])):
            students[k][1][b] += 1
        



def addNewStudent(students):
    """
    This function takes one parameter, the list of students and marks.
    This function prompts the user for the name of the student and 4 marks.
    It adds this data to the existing students list. If students enters the name that already exists,
    it keeps asking for a unique name.

    It asks user to enter the assignment mark in the given range. If the user enters the integer out of range, it 
    keeps asking him for the correct number.
    """

    cont = 'y'

    while cont == 'y' or cont == 'Y':
        marks = []      #Creates an empty list for assignment marks
        check = 0
        
        name = input(str('Enter the name of a student (unique): '))
            
        for row in range(len(students)):        #I use familiar to you approach to check if the name is in list
            if name in students[row]:
                check += 1
        
        if check != 1:      #If the name is not in the list
            for k in range(4):
                rng = True  #Variable to keep the loop running
                
                while rng:
                    mark = int(input(('Enter the assignment mark (0-100): ')))  #Asks user for the mark

                    if mark < 0 or mark > 100:      #If the mark out of range, it keeps asking user for the correct inger.
                        print('Mark is out of range. Enter the correct number.')
                    
                    else:
                        marks.append(mark)  #If the mark is in range, we add it to the marks list
                        rng = False         #Stops the loop, k goes from 0 to 1 and repeats the loop
            
            
            cont = input('Do you want to add another student? (enter "y" or "Y" to continue): ')
            students.append(tuple((name, marks)))   #If everything was entered correct, it adds a tuple (name, marks) to the students list.
        
        else:
            print('This name already exists, enter another one.')   #If check == 1 and the name exists, it keeps asking for the correct name
            cont = 'y'



def main():
    students = [("Jane", [80, 74, 93, 60]), ("Xinrong", [72, 89, 55, 75]), ("Sima", [93, 80, 74, 60])]      #Data
    print("Here is the data set", students, '\n')
    

    print('Marks for 3 students: Xinrong, Sima, Dima')
    printMark(students, "Xinrong")       #Xinrong Marks
    printMark(students, "Sima")          #Sima Marks
    printMark(students, "Dima")          #Marks of the students who is not in the list, 'No student found by that name'
    print('')
    
    
    print('The average for the 1 assignment is:')
    print(averageAssignment(students, 0))   #Calculates the average for the 1 assignment
    print('')
    

    averageMark(students, "Jane")       #Average Mark function call, it returns an integer (Jane's average Mark)
    averageMark(students, "Dima")       #Average mark function call, it returns 0 (Dima is not in the list of students)


    print('People with highest averages:')
    print(highestAverageMark(students))     #List of people with highest marks
    print('')


    print('Please, add a new student to the existing list.')
    addNewStudent(students)     #Asking to add a new student
    print('')
    

    print('New student list:')
    print(students)
    print('')


    print('Now we increase all marks by 1')
    increaseMarks(students)     #Increasing every mark by 1
    print(students)
    
main()