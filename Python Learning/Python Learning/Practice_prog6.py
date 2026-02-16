# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# d = int(input("Enter a number: "))

# if(a>b and a>c and a>d):
#     print("A is greatest")
# elif(b>c and b>d):
#     print("B is greatest")
# elif(c>d):
#     print("C is greatest")
# else:
#     print("D is greatest")

# print("End")



# =================== pass or fail ====================



# mark1 = int(input("Enter marks of subject1: "))
# mark2 = int(input("Enter marks of subject2: "))
# mark3 = int(input("Enter marks of subject3: "))

# total = ((mark1+mark2+mark3)/300)*100
# print(total)

# if(mark1>=33 and mark2>=33 and mark3>=33 and total>40):
#     print("pass")
# else:
#     print("fail")



# ================= spam or not =================

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this now"
# p4 = "click this"

# message = input("Enter a comment: ")

# if(p1 in message or p2 in message or p3 in message or p4 in message):
#     print("it is a spam")
# else:
#     print("not a spam")



# ================ if else condition ===============


# username = "rahul@1234"

# if(len(username)<10):
#     print("Username has less than 10 characters")
# else:
#     print("Username has more or equal to 10 characters")



# ================== find in list ===================



# list = ['rahul', 'amar', 'mahesh', 'divya', 'dheer']

# username = input("Enter your username: ")

# if(username in list):
#     print("your username is on the list ")
# else:
#     print("Your username is not in the list")



# ================= grade of students =================


# stu_name = input("Enter your name: ")
# stu_marks = int(input("Enter you marks: "))


# ------------- method 1 ---------------

# if(stu_marks in range(91,101)):
#     print("Ex")
# elif(stu_marks in range(81,91)):
#     print("A")
# elif(stu_marks in range(71,81)):
#     print("B")
# elif(stu_marks in range(61,71)):
#     print("C")
# elif(stu_marks in range(51,61)):
#     print("D")
# else:
#     print("F")


# --------------- method 2 ---------------

# if(91<=stu_marks<=100):
#     print("Ex")
# elif(81<=stu_marks<=90):
#     print("A")
# elif(71<=stu_marks<=80):
#     print("B")
# elif(61<=stu_marks<=70):
#     print("C")
# elif(51<=stu_marks<=60):
#     print("D")
# else:
#     print("F")



# =================== word check using if else ==================


post = input("Enter thst you want to post")


if("Harry".lower() in post.lower()):
    print("It is talking about harry")
else:
    print("It is not talking about harry")
