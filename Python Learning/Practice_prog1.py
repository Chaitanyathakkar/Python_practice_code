# =============== Square root ================

# num = int(input("Enter a number: "))

# result = num ** 0.5
# print(result)



# ================ Area of Triangle ===============


# base = float(input("Enter the base of Triangle: "))
# height = float(input("Enter the height of Triangle: "))

# area_trian = 0.5 * base * height
# print(area_trian)



# ================= Swap two variables ===============


# x = int(input("Enter a value: "))
# y = int(input("Enter a value: "))


# temp = x
# x = y
# y = temp

# print("Value of x is: ", x)
# print("Value of y is: ", y)


# ================= sum of n natural nos ================



# n = int(input("Enter a num: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i

# print(sum)


# ================= factorial using Recursion ===============


# def fact(n):
#     if (n==0):
#         return 1
#     return fact(n-1) * n

# print(fact(4))


# ================== Palindrome ==================


# text = input("Enter you name: ")
# l1 = list(text)
# l2 = []
# l2 = l1.copy()
# l2.reverse()
# # print(l2)
# if(l1 != l2):
#     print("Not Palindrome")
# else:
#     print("Palindrome")


# str = input("Enter your name: ")
# l1 = []
# l1[:0] = str
# print(l1)


# ================= fibonacci series ================

# n = int(input("Enter a num: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     a,b = b, a+b


# def fibo(n):
#     a= 0
#     b= 1
#     print(a)
#     print(b)
#     for i in range(2, n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
        
# fibo(9)



# ===================== for ================

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n*i, end=" ")



str = input("Enter a name: ")
# for i in range(0:len(str):2):
print(str[0:len(str):2])
    # str(0:len(str):2)