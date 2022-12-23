import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
#generate characters here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
digit1=random.randint(0,9)#Generate a random integer digit
digit2=random.randint(0,9)#Generate a random integer digit
punctuationSign1=chr(random.randint(33,152)) #Generate a random Lowercase letter (based on ASCII code)
punctuationSign2=chr(random.randint(33,152)) #Generate a random Lowercase letter (based on ASCII code)

#Generate password using all the characters, in random order
#make sure to concatenate in one format eg string using str()
password = uppercaseLetter1 + uppercaseLetter2 +lowercaseLetter1 +lowercaseLetter2 +str(digit1) +str(digit2) +str(punctuationSign2) +str(punctuationSign1)
password = shuffle(password)

#Ouput
print(password)
