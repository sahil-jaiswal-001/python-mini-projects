import random

def check(bot,user):
    if bot==user:
        return 0
    
    if (bot==0 and user==1):
        return -1
    
    if (bot==0 and user==2):
        return 1
    
    if (bot==1 and user==2):
        return -1
    
    if (bot==1 and user==0):
        return 1
    
    if (bot==2 and user==0):
        return 1
    
    if (bot==2 and user==1):
        return -1
    
    return 1
    
bot = random.randint(0,2)
user = int(input("Enter 0 for snake,1 for water , 2 for gun:\n"))

print("YOU :", user)
print("BOT:",bot)

score = check(bot,user)
if (score == 0):
    print("its a draw")
elif (score==1):
    print("You won")
else:
    print("YOU LOSE")