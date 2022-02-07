mport numpy
def studentInputCount():
    global students
    global students2
    students = int(input("How many students do you want in class 1:"))
    students2 = int(input("How many students do you want in class 2:"))
studentInputCount()


grades = numpy.random.uniform(10, 101, students)
averageG = numpy.average(grades)
print("--- Class 1's average grade:")
print(averageG)
print("--- Class 2's average grade:")
#print(grades)
#print("---")
grades2 = numpy.random.uniform(10, 101, students2)
averageG2 = numpy.average(grades2)
#print("---")
print(averageG2)
print("--- What classes passed or failed:")
#print(grades2)
if averageG > 60:
    print("Class 1 passed")
else:
    print("Class 1 failed")

if averageG2 > 60:
    print("Class 2 passed")
else:
    print("Class 2 failed")
print("--- Who got the best overall grade:")
if averageG > averageG2:
    print("Class 1 won")
else:
    print("Class 2 won")
def extraInfo():
    global extra
    extra = input("Enter codes for more info:")
print("--- Extra info")
extraInfo()
if extra == "12231282":
    print(grades)
    print("---")
    print(grades2)
    extraInfo()
else:
    extraInfo()
