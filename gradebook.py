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

if __name__ == "__main__":#runs the whole project
    main()