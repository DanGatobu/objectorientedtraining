def beginner():
    print("hi there")
    print("welcome")
    
    
beginner()



def beginner(firstname,lastname):
    print(f"hi {firstname} {lastname}")
    print("welcome")
    
    
beginner("Dan","Newton")
beginner("Newton","Dan")

#return function
def greeting(name):
    return f"hi {name}"
message=greeting("Dan")
print(message)


def increment (number,by):
    return number + by
result=increment(5,6)
print(result)

#this mmakes parameters optional
def increment (number,by=1):
    return number + by
result=increment(5,6)
print(result)


def multiply(*numbers):
    total=1
    for number in numbers:
        total=total * number

print(multiply(2,3,4,5))

def saveuser(**user):
    print(user["name"])
saveuser(id=1, name="john",age=22)

def greet(name):
    global message
    message="a"

def sendemail(name):
    message="b" # local variable
    
def fizbuzz(numb):
    if numb % 3 == 0 and numb % 7 != 0:
        print("FIZZ")
    elif numb % 7 == 0 and numb % 3 != 0:
        print("BUZZ")
    elif numb % 7==0 and numb % 3==0:
        print ("FIZBUZZ")
    else: 
        print(numb)

gat=fizbuzz(49)

