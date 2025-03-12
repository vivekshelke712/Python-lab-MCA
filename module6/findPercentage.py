# Write a Program to Read marks from user and Find the percentage of marks of student. 

def findPercentage():
    marks = int(input("Enter the marks: "))
    totalMarks = 600
    percentage = (marks / totalMarks) * 100
    print("Percentage of marks is: ", percentage)

if __name__ == "__main__":
    findPercentage()
    