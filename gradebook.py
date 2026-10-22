gradebook={
        "math":[75,92,100],"english":[90,93,96],"science":[88,92,94],"french":[98,99,97]
    }
def main():
    course = input("what class would you like to add a grade for? ")
    grade = int(input("what grade are you adding"))
    add_grade(course, grade)
    

def add_grade(subject, grade):#takes in subj with grade and adds grade to subj if subj i new it crates a new subj in gradebook
    if subject in gradebook:
        gradebook[subject].append[grade]
    else:
        gradebook[subject] = [grade]

def print_average(subject):#gets the average grade of the subject that is the parameter
    grades = gradebook[subject]
    avgGrade = sum(grades)/len(grades)
    print ("your grade average in "+subject+ "is "+ avgGrade)

def print_grades(subject):#print all the grades in a given subject
    grades = gradebook[subject]
    print("your grades in "+subject+ "are "+ grades)

def print_all_averages():#gives the average of all the classes and tells the user their lowest class and their highest class
    averages=[]
    for subject in gradebook:
        grades = gradebook[subject]
        avgGrade = sum(grades)/len(grades)
        averages.append(avgGrade)
    i=0
    for subject in gradebook:
        print("your average grade in "+subject+"is "+averages[i])
        i+=1
    low=0
    for i in range (len(gradebook)-1):
        if averages[i]<averages[i+1]:
            low=i
    high=0
    for i in range (len(gradebook)-1):
            if averages[i]>averages[i+1]:
                high=i
    print("your lowest grade is "+ gradebook[low]+" with an average of "+averages[low])
    print("your highest grade is "+ gradebook[high]+" with an average of "+averages[high])



if __name__ == "__main__":#runs the whole project
    main()