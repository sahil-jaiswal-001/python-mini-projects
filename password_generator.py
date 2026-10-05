import secrets
#to generator strong random numbers or alphabets
import string

length = int(input("Enter length of your password: "))
#string.ascii chooses random alphabet
#.digits generatos random value
#last one for characters
characters= (string.ascii_letters + string.digits + "!@#$%^&*")

password=""

for i in range(length):
   password += secrets.choice(characters)
#this picks from every characters above and generators passwpord
   
print("Generated password is :", password)