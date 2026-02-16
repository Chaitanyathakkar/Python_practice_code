
# list = [1, 3, 'harry', 'rahul', 23.5, True]

# i=0
# while(i<len(list)):
#     print(list[i])
#     i+=1




# =============== multiplication table ================


# num = int(input("Enter number: "))


# ---------------- Using while -------------------

# i=1
# while(i<11):
#     print(num,"*",i,"=", i*num)
#     print(f"{num} * {i} = {num*i}")
#     i+=1


# ----------------- Using for -------------------

# for i in range(1,11):
#     print(num,"*",i,"=", i*num)
    # print(f"{num} * {i} = {num*i}")





# ================ loops in list ==================


# list = ["Harry", "Soham", "Sachin", "Rahul"]


# ------------- Using while ---------------

# i=0
# while(i<len(list)):
#     if(list[i].startswith("S")):
#         print("Welcome", list[i])
#         i+=1
#     else:
#         i+=1


# -------------- Using for -----------------

# for name in list:
#     if(name.startswith("S")):
#         print("Welcome", name)





# ================= Prime or not ==================


# num = int(input("Enter num: "))

# for i in range(2,num):
#     if(num%i == 0):
#         print("Number is not Prime")
#         break
# else:
#     print("Number is prime")




# ================== Sum of n natural nos ==================


# num = 5
# i=1
# n=0
# while(i<=num):
#     n+=i
#     i+=1

# print(n)




# ================= factorial using for ====================


# n = int(input("Enter a num: "))
# fact = 1

# for i in range(1,n+1):
#     fact*=i

# print(fact)




# ================= Pattern ================


# n  = int(input("Enter a num: "))

# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1))



# ================ Pattern =================


# n  = int(input("Enter a num: "))

# for i in range(1,n+1):
#     print("*"* (i))



# ================= Pattern ================


# n = int(input("Enter a num: "))

# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n)
#     else:
#         print("*",end="")
#         print(" "* (n-2), end="")
#         print("*")



# ================= multiplication table in reverse ==================


n = int(input("Enter a num: "))

for i in range(10,0,-1):
    print(n,"*",i,"=",n*i)