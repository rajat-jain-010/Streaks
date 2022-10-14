#Python program to check number representation is in binary

def binaryChecker(num):
    while(num>0):
        j=num%10
        if j!=0 and j!=1:
            print("num is not binary")
            break
        num=num//10
        if num==0:
            print("num is binary")

num = int(input("please give a number ::> "))
print(num)
binaryChecker(num) 