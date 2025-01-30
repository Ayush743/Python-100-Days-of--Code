print("------------------------------𝓭𝓪𝔂 4---------------------------------------------->")

#------------Using random module------------>

import math
import random
r=random.randint(1,10)
print(r)
f=math.floor(random.random()*5+1)
print(f)


#-----------Heads or Tails----------->

coin_value=random.randint(0,2)
if(coin_value==1):
    print('Heads')
else:
    print("Tails")



# ------------whose going to pay the bill------------>


names=input("Enter the names of members seperated by ',' : ")
namelist=names.split(",")
x=random.randint(0,len(namelist)-1)
#print(namelist[x],"will pay the bill")
#----- or-------------->
print(random.choice(namelist),"will pay the bill for meal today")

#----Place the treasure------------------->

row1=["🌫️","🌫️","🌫️"]
row2=["🌫️","🌫️","🌫️"]
row3=["🌫️","🌫️","🌫️"]
field=[row1,row2,row3 ]
print(f"{row1}\n{row2}\n{row3}")
coord=input("Enter the coordinates : ")
x=int(coord.split(" ")[0])-1
y=int(coord.split(" ")[1])-1
field[x][y]="❌"
row1=field[0]
row2=field[1]
row3=field[2]
print(f"{row1}\n{row2}\n{row3}")

#----------Rock-Paper-Scissor--------------------->


choice=int(input("Enter your choice 1(Rock) 2(Paper) 3(scissor) : "))
ch=[1,2,3]
ai=ch[random.randint(0,2)]
if(choice==1 and ai==1):
    print("you chose : 🪨")
    print("computer choose : 🪨")
    print("result : tie")
elif(choice==1 and ai==2):
    print("you chose : 🪨")
    print("computer choose : 📄")
    print("result : you loose 😔")
elif(choice==1 and ai==3):
    print("you chose : 🪨")
    print("computer choose : ✂️")
    print("result : you win 🔥")
elif(choice==2 and ai==1):
    print("you chose : 📄")
    print("computer choose : 🪨")
    print("result : you win 🔥")
elif(choice==2 and ai==2):
    print("you chose : 📄")
    print("computer choose : 📄")
    print("result : tie")
elif(choice==2 and ai==3):
    print("you chose : 📄")
    print("computer choose : ✂️")
    print("result : you loose 😔 ")
elif(choice==3 and ai==1):
    print("you chose : ✂️")
    print("computer choose : 🪨")
    print("result : you loose 😔")
elif(choice==3 and ai==2):
    print("you chose : ✂️")
    print("computer choose : 📄")
    print("result : you win 🔥")
elif(choice==3 and ai==3):
    print("you chose : ✂️")
    print("computer choose : ✂️")
    print("result : tie")

