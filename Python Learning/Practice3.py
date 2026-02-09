# list = []

# list.append(input("Enter Your most Favourite Movie: "))
# list.append(input("Enter Your Second most Favourite Movie: "))
# list.append(input("Enter Your Third most Favourite Movie: "))
# print(list)



# =============== Palindrome =================


# list1 = [1, 2, 3, 2, 1]
# list2 = []

# list2 = list1.copy()
# list2.reverse()
# print(list2)

# if(list2==list1):
#     print("list is palindrome")
# else:
#     print("list is not palindrome")



# =================== Count Grades in tuple ====================



# tup = ("C", "D", "A", "A", "B", "B", "A")

# print(tup.count("A"))



# =================== Ascending sort in list ========================


# grades = ["C", "D", "A", "A", "B", "B", "A"]

# grades.sort()
# print(grades)


# ================= if-elif-else ===============



n = int(input("Enter a Number between 1 to 100: "))

if(n%2!=0 and n<=100):
    print("Wierd")
elif(2<=n<=5):
    print("Not Wierd")
elif(6<=n<=20):
    print("Wierd")
elif(100>=n>20):
    print("Not Wierd")
else:
    print("Select the number in range")