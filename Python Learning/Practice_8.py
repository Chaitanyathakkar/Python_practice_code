# =================== Class and object ==================


# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def average(self):
#         sum = 0
#         for i in self.marks:
#             sum+=i
#         print("Your avg_score is:", sum/3)
    

# s1 = Student("karan", [76, 89, 87])
# print(s1.name, s1.marks)
# s1.average()



# ================== Account class ===================


class Account:
    
    def __init__(self, balance,account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self,n):
        self.n = n
        self.balance = self.balance - self.n
        print(n, "Amount was debited from your accout")
        print("Total Balance: ", self.print_balance())

    def credit(self, m):
        self.balance = self.balance + m
        print(m, "Amount was Credited to your accout")
        print("Total Balance: ", self.print_balance())

    def print_balance(self):
        return self.balance
        
    
a1 = Account(12000, 12)
# print(a1.balance, a1.account_no)
a1.debit(1000)
a1.credit(2000)
# a1.print_balance()
