#WAP to calculate lcm of two numbers

def lcm(a, b):
    greater = a if a>b else b
    while(True):
        if (greater%a == 0 and greater%b == 0):
            return greater
            break
        greater = greater + 1
        

a = int(input("enter value of first nymber ::> "))
b = int(input("enter value of first nymber ::> "))
print(f"lcm of {a} and {b} is ::>",lcm(a, b))



