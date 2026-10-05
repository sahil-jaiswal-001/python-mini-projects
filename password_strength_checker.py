import string

password=input("enter your password : ")

score =0
#for length
if len(password) > 8:
    score += 1

#checking lower case
if any(char.islower() for char in password):
    score +=1
    
#checking upper case
if any(char.isupper() for char in password):
    score +=1
    
#checking number
if any(char.isdigit() for char in password):
    score +=1
    
#cheking punctuations
if any (char in string.punctuation for char in password):
    score +=1
    
if (score<=2):
    print("Your password strength is weak")
elif(score <=4 ):
    print(" Your password strength is moderate")
else:
    print("Your password is strong")
    
    