#program of a grading system#
#finding the marks of five subjects#
#marks-prompt the user to enter the marks of five subjects#
#if else#
print("subjects and marks")
print("enter marks against subjects")
OOP=int(input("enter the marks for OOP;"))
OOSAD=int(input("enter the marks for OOSAD;"))
MULTIMEDIA=int(input("enter the marks for MULTIMEDIA;"))
HCNA=int(input("enter the marks for HCNA;"))
DATABASE=int(input("enter the marks for DATABASE;"))
print("")
print("OOP=",OOP)
print("OOSAD=",OOSAD)
print("MULTIMEDIA=",MULTIMEDIA)
print("HCNA=",HCNA)
print("DATABASRE=",DATABASE)
#calculating the average
avg=(OOP+OOSAD+MULTIMEDIA+HCNA+DATABASE)/5
print("average=",avg)
#if statement
if avg>=80 and avg<=100:
     print("GRADE IS A")
elif avg>=70 and avg<=79:
    print("GRADE IS B")
elif avg >= 60 and avg <= 69:
    print("GRADE IS C")
elif avg >= 50 and avg <= 59:
    print("GRADE IS D")
elif avg >= 0 and avg <= 49:
    print("GRADE IS FAIL")
else:
    print("marks error,please try again")

