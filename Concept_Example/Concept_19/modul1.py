def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b




# calling the functions
if __name__ == "__main__":
    print(add(2,3))
    print(sub(5,1))
    print(mul(2,3))


print(__name__)

# check run directly or imported
if __name__ == "__main__":
    print("main.py is run directly")
else:
    print("main.py is imported")


