# i = 100
# while i>=1:
#     print(i)
#     i-=1


# ============== mulitipliaction table while ==============


# n = int(input("Enter a number: "))
# i=1

# while(i<=10):
#     print(i, "*", "=",n*i)
#     i+=1


# ===================== squares using while ==================


# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while(i<len(nums)):
#     print(nums[i])
#     i+=1
    


# ====================== Search for a number in tuple ===================


# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = int(input("Enter x: "))
# i=0
# while(i<=len(num)-1):
#     if(num[i]==x):
#         print("Found at Index", i)
#         break
#     else:
#         print("Finding")
#     i+=1


# ================== Print list ele using for loop ====================


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in nums:
    print(i)


# ================== Search number in tuple using for loop ==================

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x=int(input("Enter a number: "))
# c = 0
# for i in num:
#     if(x==i):
#         print("found at index", c)
#     c+=1



# ================== multiplication table using for & range =====================



# n = int(input("Enter n: "))

# for i in range(1,11):
#     print(n,"*", i, "=", n*i)



# ==================== sum of n Natural numbers using while ==================

# n= int(input("Enter n: "))
# i=1
# count=0
# while(i<=n):
#     count+=i
#     i+=1
# print(count)



# ===================== Factorial of n number ===================

# fact=1
# for i in range(1, 6):
#     fact*=i
# print(fact)