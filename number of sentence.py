numofletter = 0
numofwords = 0
numofdigist = 0

text = input("enter your name " )

for x in text:
    x = x.lower()
    if x >= 'a' and x >= 'z':
        numofletter =numofletter + 1

    elif x >= '0' and x <= '9':
        numofdigist = numofdigist + 1
    elif x == ' ' :
        numofwords = numofwords + 1
print("number of digits ",numofdigist)
print("number of words ",numofwords + 1)
print("number of letter  ",numofletter )