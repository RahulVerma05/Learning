'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        
    student.sort(key= lambda x: x[1])
    
    for i in range(1,len(student)):
        if student[i][1] > student[0][1]:
            second_min = student[i][1]
            break
    
    second_name = []
    for student_name in student:
        if student_name[1] == second_min:
            second_name.append(student_name[0])
    
    for name in sorted(second_name):
        print(name)
