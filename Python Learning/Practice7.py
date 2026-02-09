# f = open("demo.txt", "a")
# data = f.write("\nTomorrow Bye.")
# f.close()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# import os

# os.remove("Untitled-1.txt")



# ================ Create a file and add data ==============


# with open("practice.txt", "a") as f:
#     data = f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

    
# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     data = f.write(new_data)

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("FOUND")
    else:
        print("NOT FOUND")
