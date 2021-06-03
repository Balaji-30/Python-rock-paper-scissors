import random
print("Enter your name:",end="")
name=input()
print("\nHello,",name)
a=[]
n=False
ch=input()
ch=ch.replace("'","").replace("[","").replace("]","").replace(" ","").replace("\"","")
print("Okay, let's start")
if ch=="":
    n=True
    a=["rock","paper","scissors"]
    lose_conditions = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
else:
    lose_conditions={}
    
file=open("rating.txt","r")
j=[]
for x in file:
    
    j.append(x.split(" "))
y=len(j)
g=0
for i in range(y):
        if name==j[i][0]:
            g+=int(j[i][1])
            f=1
            break
        else:
            f=0
if f==0:
    g=0
    
while 1:
    new = input()
    if n:
        choice = random.choice(a)
        if new == '!exit':
            print('Bye!')
            break
        elif new == "!rating":
            print("Your rating:",end="")
            print(g)           
        elif new not in a:
            print("Invalid input")
        elif lose_conditions[new] == choice :
            print("Sorry, but the computer chose " + choice)
        elif new == choice :
            print('There is a draw (' + choice + ')')
            g+=50
        else:
            print('Well done. The computer chose ' + choice + ' and failed')
            g+=100
    else:
            a=ch.split(",")
            b=ch.split(",")
            if new == '!exit':
                print('Bye!')
                break
            elif new == "!rating":
                print("Your rating:",end="")
                print(g)
                continue
            elif new not in b:
                print("Invalid input")
                continue
            choice = random.choice(a)
            x=a.index(new)
            a=a[x+1:]
            a.extend(b[:x])
            l=len(a)//2
            a=a[:l]          
            if  new == choice :
                print('There is a draw (' + choice + ')')
                g+=50    
            elif choice in a:
                print("Sorry, but the computer chose " + choice)
            else:
                print('Well done. The computer chose ' + choice + ' and failed')
                g+=100

