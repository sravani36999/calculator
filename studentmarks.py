total = 0 
subjects = ["Telugu", "Hindi", "English", "Science", "Social"]
isValid =  True


print("Enter marks of 5 subjects(out of 100): ")


for i in range(5):
    marks = int(input(f"{subjects[i]}: "))
    if marks > 100 or marks < 0 :
        print("Please! Check marks, Enter for out of 100")
        isValid = False
        break
    else:
        total += marks
        #print(total)

if isValid:
    percentage = total / 500 *100 

    print("Total:",total)
    print("percentage:",percentage,"%")


    print("Grades are Here...")

    if percentage >= 90:
        print("Grade A")
    elif percentage >=75:
        print("Grade B")
    elif percentage >= 60:
        print("Grade C")
    elif percentage >=35:
        print("Grade D")
    else:
        print("Fail")



'''I developed a Marks Calculator using Python.
It takes marks of five subjects, validates the 
input, calculates the total and percentage, and 
assigns a grade using conditional statements.'''