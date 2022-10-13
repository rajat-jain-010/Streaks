#WAP to create otp generator 
import random

def generator(lengthOfOTP):
    otp = ""
    if lengthOfOTP > 2 :
        for i in range(lengthOfOTP):
            otp = otp + str(random.randint(0,9))
        print(f"the one time passwor  for you  is {otp}")
    else:
        print("enter a minimum length of atleast 3")
    
    return otp
        
        

lengthOfOTP = int(input("Enter the length of OTP you want us to generate ::> "))
generator(lengthOfOTP)

