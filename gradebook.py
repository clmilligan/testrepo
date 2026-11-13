import csv
gradebook={}

    
def main():#runs all of the programs in a way that makes it easy for the user
    y=True
    with open('grades.csv','r') as f:
        data = csv.reader(f)
        for row in data:
            if row:
                    key=row[0]
                    values=[int(val) for val in row[1:] if val.strip()]
                    gradebook[key]=values
        print(gradebook)
    while y!=False:
        print ("What do you need help with? (1-5)")
        print ("1. Adding a grade/class?")
        print("2. Getting your average in a certain class? ")
        print("3. Printing all of your grades in a certain class?")
        print("4. Printing the averages of all the grades in all of your classes? ")
        pick=int(input("5. Getting your gpa? "))
        if(pick==1):
            course = input("what class would you like to add a grade for? ").lower()
            grade = int(input("what grade are you adding? "))
            add_grade(course,grade)
        elif (pick==2):
            course = input("what class would you like to get your average for? ").lower()
            print_average(course)
        elif (pick==3):
            course = input("what class would you like to get your grades for? ").lower()
            print_grades(course)
        elif(pick==4):
            print_all_averages()
        elif(pick==5):
            print(get_GPA())
        else:
            print("please pick a valid option")
        temp=input("Do you need any more help? (y/n)").lower()
        if temp=="y":
            y=True
        else:
            y=False
    with open("grades.csv","w",newline="")as file:#overides the csv and adds the info 
        writer=csv.writer(file)
        for key, value in gradebook.items():
            writer.writerow([key] + [str(v) for v in value])

        
    

def add_grade(subject, grade):#takes in subj with grade and adds grade to subj if subj i new it crates a new subj in gradebook
    if subject in gradebook:
        gradebook[subject].append(grade)
    else:
        gradebook[subject] = [grade]
    print(grade+"added to "+subject)

def print_average(subject):#gets the average grade of the subject that is the parameter
    grades = gradebook[subject]
    avgGrade = str(sum(grades)/len(grades))
    print ("your grade average in "+subject+ "is "+ avgGrade)

def print_grades(subject):#print all the grades in a given subject
    grades = gradebook[subject]
    grade=""
    for g in grades:
        hold=str(g)
        grade = grade+", "+hold
    print("your grades in "+subject+ " are "+ grade)

def print_all_averages():#gives the average of all the classes and tells the user their lowest class and their highest class
    averages=[]
    for subject in gradebook:
        grades = gradebook[subject]
        avgGrade = sum(grades)/len(grades)
        averages.append(avgGrade)
    i=0
    for subject in gradebook:
        print("your average grade in "+subject+" is "+str(averages[i]))
        i+=1
    low=0
    for i in range (len(gradebook)-1):
        if averages[i]<averages[i+1] and averages[i]<averages[low]:
            low=i
    high=0
    for i in range (len(gradebook)-1):
            if averages[i]>averages[i+1]and averages[i]>averages[high]:
                high=i
    print("your lowest grade is "+ (list(gradebook.keys())[low])+" with an average of "+str(averages[low]))
    print("your highest grade is "+ (list(gradebook.keys())[high])+" with an average of "+str(averages[high]))

def get_GPA():#prints the users gpa based on their average
    averages=[]
    for subject in gradebook:
        grades = gradebook[subject]
        avgGrade = sum(grades)/len(grades)
        averages.append(avgGrade)
    total=0
    for avg in averages:
        total+=avg
    total= total/(len(averages))
    if(total>=92.5):
        return ("4.0 or A")
    elif(total>=89.5):
        return("3.7 or A-")
    elif(total>=79.5):
        return("3.0 or B")
    elif(total>=69.5):
        return("2.0 or C")
    elif(total>=65):
        return("1.0 or D")
    else:
        return("0.0 or C")

def remove_grade(subject, grade):#removes a grade based on a given subject and grade
    if subject in gradebook and grade in gradebook[subject]:
        gradebook.subject.remove(grade)
        print("grade succesfully removed")
    else:
        print ("thet grade dosent exist in "+subject)



if __name__ == "__main__":#runs the whole project
    main()