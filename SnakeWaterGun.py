import random
def game(p1,p2):
    if p1==p2:
        return "There is a tie"
    elif((p1=="s" and p2=="w") or (p1=="g" and p2=="s") or (p1=="w" and p2=="g")):
        return "You win"
    elif((p1=="w" and p2=="s") or (p1=="s" and p2=="g") or (p1=="g" and p2=="w")):
        return "You lose"
        
def p2Naming(p2):
    if(p2 == "s"):
        return "snake";
    elif(p2 == "w"):
        return "water"
    elif(p2 == "g"):
        return "gun"
        
li=["s","w","g"]
w_count=l_count=k=0
while(k<10):
    p2=random.choice(li)
    try:
        p1=input("What you choose: \nS for SNAKE\nW for WATER\nG for GUN\n\n")
        p1=p1.lower()    
        s=game(p1,p2)
        p2Chose= p2Naming(p2)
        print("Computer choose",p2Chose,"\n",s)
        if "win" in s:
            w_count+=1
        elif "lose" in s:
            l_count+=1
        else:
            pass
        print(9-k,"chances are left\n")
    except:
        print("You have entered wrong input and wasted one chance\n")
    k+=1
if w_count>l_count:
    print("\n\nWINNER\nYou win",w_count,"times!!!")
elif w_count==l_count:
    print("\n\nOo oh!!..There's a tie")
else:
    print("\n\nYou Loose!!!\nComputer wins",l_count,"times!!!")
