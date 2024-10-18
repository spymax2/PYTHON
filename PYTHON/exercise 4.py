s1 = int(input("maths: "))
if s1 > 100:
    print("invalid input")
s2 = int(input("english: "))
if s2 > 100:
        print("invalid input")
s3 = int(input("chemistry: "))
if s3 > 100:
     print("invalid input")
s4 = int(input("biology: "))
if s4 > 100:
    print("invalid input")

s5 = int(input("computer: "))
if s5 > 100:
        print("invalid input")


average  = (s1+s2+s3+s4+s5)/5
print(average)

if average > 70 and average <= 100:
    print("A")

if average > 60 and average <= 70 :
    print("B")

if average > 50 and average <= 60:
    print("C")

if average >= 40 and average <= 50:
    print("D")

if average >=0 and average <= 39:
    print("E")

if average > 100:
    print("invalid")
