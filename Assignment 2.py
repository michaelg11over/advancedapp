# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Michael Glover
# Assignment Number: Assignment 2
# Due Date: 02/18/2026
# Purpose: Reads a text file where each line has a student name followed by
#          6 numeric scores. Computes each student's grade average and displays
#          the full class list ranked from highest to lowest average.
# Resources: Youtube


#opens the files to read
data_file = open("Assignment2input.txt", "r")
#dictionary
class_data = {}

for line in data_file:
    parts = line.strip().split()
    student_name = parts[0]
    score_sum = 0
    for score in parts[1:]:
        score_sum += float(score)
    #calculates the average
    class_data[student_name] = score_sum / 6

#closes file
data_file.close()

#sorts 
final_order = sorted(class_data, key=class_data.get, reverse=True)

#prints students name and rounds up by two decimals
for student_name in final_order:
    print(student_name, f"{class_data[student_name]:.2f}")