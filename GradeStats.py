# student_grades contains scores (out of 100) for 5 assignments
#Print the name and grade percentage of the student with the highest total of points.
#Find the average score of each assignment.
#Find and apply a curve to each student's total score, such that the best student has 100% of the total points.

student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

percent_grades = {}
names = list(student_grades.keys())
print(names)

total = 0
grades = []

for value in student_grades.values():
    for num in value:
        total += num
    grade = ((total / 500) *100)
    grades.append(grade)
    total = 0
    
print(grades)

for i in range(len(names)):
        percent_grades[names[i]] = grades[i]
        
print(percent_grades)

sorted_grades = sorted(percent_grades.values())
sorted_dict = {}
for i in sorted_grades:
    for k in percent_grades.keys():
        if percent_grades[k] == i:
            sorted_dict[k] = percent_grades[k]
print(sorted_dict)

    

