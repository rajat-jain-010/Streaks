#Python program to remove spaces from string without inbuilt function

def remover(string):
    temp = string
    string = ""
    for i in temp:
        if i != " ":
            string += i
    
    print(f"String without spaces is {string}")

myString = input("enter your string ::> ")
remover(myString)
