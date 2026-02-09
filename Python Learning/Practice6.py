# cities = ["he", "klj", "ouy", "pour", "opt", "trup"]
# host = ["light", 34, 45, "pit"]

# def length_list(list):
#     for i in list:
#         print(i, end=" ")

# length_list(cities)
# length_list(host)


# ====================== fact of n using function ==================

# def fact(n):
#     fac = 1
#     for i in range(1,n+1):
#         fac*=i
#     print(fac)
#     return fact

# fact(5)



# ======================== USD to INR using function ===================


# def convert(USD_val):
#     IND_val=USD_val*90
#     print("USD_val:",USD_val, "= IND_val",IND_val)
#     return IND_val

# convert(4)



# ===================== ODD or EVEN using Function =====================


# def odd_even(num):
#     if(num%2!=0):
#         print("ODD")
#     else:
#         print("EVEN")
    
# odd_even(2)



# ==================== factorial using recursion ======================


# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1) * n

# print(fact(5))


# ==================== Sum of natural nos using recursion =====================


# def sum(n):
#     if (n==0):
#         return 0
#     return sum(n-1) + n

# print(sum(0))


# ==================== elements in list uaing recursion ======================



def list(list1,i):
    if(i==len(list1)):
        return
    print(list1[i])
    list(list1, i+1)

li = [1, 2, 3, 4, 5]
list(li,0)