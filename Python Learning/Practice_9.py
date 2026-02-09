# class Circle:
#     def __init__(self,r):
#         self.r = r
    
#     def area(self):
#         return (22/7) * self.r ** 2

#     def perimeter(self):
#         return 2 * (22/7) * self.r
        
# r1 = Circle(21)
# print(r1.area())
# print(r1.perimeter())


# ================== Employee =================


# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showdetails(self):
#         print("Role of Employee:", self.role)
#         print("Departmen of Employee:", self.department)
#         print("Salary of Employee:", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "60000")


# e1 = Engineer("Musk", 25)
# e1.showdetails()



# ================== Items ===================


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return o1.price > o2.price
        
o1 = Order("chips", 10)
o2 = Order("tea", 15)
print(o1 > o2)