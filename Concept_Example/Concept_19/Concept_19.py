# According to the above Concept_19, we are now going to implement of this topic with  the following example.

# Concept_19   is : if__name__ == "__main__"

# it is construct is a common idom in python that alow to 
# run code only if the script was executed Directly 
# and not when it is imported as a module in an other script.

# it is modtly used:
# 1. writing module level code
# 2. writing test code
# 3. reusing the code


# Example_1:
#---------------------------------------------
# lets i have two files main.py and modul1.py

# main.py
#---------------------------------------------
# in this file we create some functions like 
# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# wehen we calling the functions 
# print(add(2,3))  # 5
# print(sub(5,1))  # 4
# print(mul(2,3))  # 6

# output:
# 5
# 4
# 6


# now i am working on modul1.py
# in modul1.py file i need some functions like add, and mul
# for this i have two options

# 1. copy the functions from main.py to modul1.py
# 2. import the functions from main.py to modul1.py

# i am going to use the second option(best approach)
# i am going to import the functions from main.py to modul1.py

# modul1.py
#---------------------------------------------
# import main
# print(main.add(20,30))
# print(main.mul(4,5))

# output:
# 5
# 4
# 6
# 50
# 20

# problem is that when i run the modul1.py file
#  it will also run and execute code  all  the main.py function  file

# but i want to run only the code or function that i resued from
# main.py file in modul1.py file(add, and mul)

# for this i am going to use the if__name__ == "__main__" construct 
# in main.py file like this 


# main.py
#---------------------------------------------
# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# if __name__ == "__main__":
#     print(add(2,3))
#     print(sub(5,1))
#     print(mul(2,3))
#
# and you can check is this file is run directly or imported
# by using the following code
# print(__name__)

# when i run main.py file it will run properly
# not any effect of using the this construct
# output:
# 5
# 4
# 6


# now i am going to run the modul1.py file

# modul1.py
#---------------------------------------------

# import main
# print(main.add(20,30))
# print(main.mul(4,5))

# output:
# 50
# 20


# now it is working fine

# this is a common idom in python that alow to
# run code only if the script was executed Directly

# and not when it is imported as a module in an other script.

# it is modtly used:
# 1. writing module level code
# 2. writing test code
# 3. reusing the code

# this is a concept of if__name__ == "__main__" in python

#so, this is the example of Concept_19
#---------------------------------------------
# sorces:
# https://youtu.be/5Q9jzDL7G-8?si=jGWvSEkDDqhBrqoW



