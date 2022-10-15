#Write a Python function to insert a string in the middle of a string

a = input("enter your String ::> ")
b = input("Enter the substring u want to add in middle ::> ")
lengthOfa = len(a)
q = ""
for i in range(0,lengthOfa//2):
    q = q + a[i]

q = q + b

for i in range(lengthOfa//2,lengthOfa):
    q = q + a[i]
    
print(q)
    