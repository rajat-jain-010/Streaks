#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 

string = input("Enter words seprated by comma ::> ").split(",")
string = list(set(string))
string.sort()
string = ",".join(string)
print(f"sorted words list is ::>  {string}")