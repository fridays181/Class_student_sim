#print(Xy)
#average
#median
#std
#var
#percentile
#10 students, we need to find the average grade and compare classes
# ^ 10 random numbers                 ^find the average randomized grade


#importing numpy
import numpy
#title
print("(---Ethans Class Simulation---)")
#user input function
def studentInputCount():
    global students
    global students2
    students = int(input("How many students do you want in class 1:"))
    students2 = int(input("How many students do you want in class 2:"))
#calling to the function
studentInputCount()
#generic grade system variables
basegrade = 10
topgrade = 101
#randomly generate a user inputted amount of grades
grades = numpy.random.randint(basegrade, topgrade, students)
#average of the random grades made
averageG = numpy.average(grades)

print("(---Results---)")
print("--- Class 1's average grade:")
#converts average to an integer
averageGB = int(averageG)
print(averageGB)
print("--- Class 2's average grade:")
grades2 = numpy.random.randint(basegrade, topgrade, students2)
averageG2 = numpy.average(grades2)
averageGB2 = int(averageG2)
print(averageGB2)
print("--- What classes passed or failed:")
#I made the passing average grade 60, this shows wheather of not the average of the class passed
if averageG > 60:
    print("Class 1 passed")
else:
    print("Class 1 failed")

if averageG2 > 60:
    print("Class 2 passed")
else:
    print("Class 2 failed")
print("--- Who got the best overall grade:")
#If one persons average is bigger they win
if averageG > averageG2:
    print("Class 1 won")
else:
    print("Class 2 won")
    #additional info area
def extraInfo():
    global extra
    extra = input("Enter codes for more info:")
print("--- Extra info")
extraInfo()
if extra == "ethan":
    grades.sort()
    grades2.sort()
    print("---All class 1 grades")
    print(grades)
    print("---All class 2 grades")
    print(grades2)
    extraInfo()
else:
    extraInfo()
#MAKE A SYSYEM ON HOW MANY STUDENTS PASSED
#^THIS NOTES FOR ME
