#Python program to count vowels numbers special cracters and consonants in the string

vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}

def counter(string):
     vowel, consonant, numbers, specials = 0, 0, 0, 0
     for i in string:
         if i in vowels:
             vowel = vowel + 1
         elif ord(i) > 47 and ord(i) < 58:
             numbers = numbers + 1
         elif ((ord(i) > 64 and ord (i) < 91) or (ord(i) > 96 and ord(i) < 123))  and i not in vowels:
             consonant += 1
         else:
             specials += 1
     
     print(f"total consonant in string is/are {consonant}")
     print(f"total vowel in string is/are {vowel}")
     print(f"total number in string is/are {numbers}")
     print(f"total special character in string is/are {specials}")

myString = input("enter the string ::> ")
counter(myString)