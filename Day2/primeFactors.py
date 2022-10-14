#Write a program in Python to find prime factors of a given integer and write their count.
def factorsFinder(num):
        
    for i in range(2,num+1):
            if num%i == 0:
                list1.append(i)
                num = num // i
                break
                
    if (num > 1):
        factorsFinder(num)
    return list1
 
list1 = []
num = int(input("enter your numbers ::> "))
factors = factorsFinder(num)
print(f"all factors of {num} are {factors}")
print(f"Total prime factors are ::> {len(list1)}")


