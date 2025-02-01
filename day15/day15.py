print("------------------------------𝓭𝓪𝔂 2---------------------------------------------->")

#--------------------Coffee Machine------------------------------------->
from coffee_data import data
import time
coffee_names=[]
for items in data:
    coffee_names.append(items["name"].lower())
print(coffee_names)

current_report={

    "water" : "500 ml",
    "milk" : "500 ml",
    "coffee" : "500 gm",
    "money" : "₹ 1000",
    }
s=1
a=1

def resource_updation(coffee):
     for item in data:
        if(item["name"].lower()==coffee):
            current_report["water"]=str(int(current_report["water"].split(" ")[0])-item["water"])+" ml"
            current_report["milk"]=str(int(current_report["milk"].split(" ")[0])-item["milk"])+" ml"
            current_report["coffee"]=str(int(current_report["coffee"].split(" ")[0])-item["coffee"])+" gm"
            current_report["money"]= "₹ " + str(float(current_report["money"].split(" ")[1]) + item["money"])
              
    
def sufficient(coffee):
    global s
    for items in data:
        if(items["name"].lower()==coffee):
            for item in items:
                if(item in ["water","coffee","milk"]):
                    if(items[item]>int(current_report[item].split(" ")[0])):
                        print(f"Sorry,there is not enough {item}")
                        s=0
                        
  

def return_amt(coffee,amt):
     global a
     for item in data:
        if(item["name"].lower()==coffee):
            if(amt<item["money"]):
                    print(f"you dont have enough money, pls pay ₹{round(item['money']-amt,2)} more and try again")
                    a=0
    
            else:
              print(f"Thanks for buying, here is the change : ₹{round(amt-item['money'],2)}")
              a=1
def calc(coffee):
     for item in data:
        if(item["name"].lower()==coffee):
            return item["money"]

while True:
    print("What would you like to have :")
    for coffee in data:
        print(coffee["name"],end=",")
    choice=input("\ntype here : ").lower()
    sufficient(choice)
    resource_updation(choice)
    if(choice=="report"):
        print("Here is the report for the machine :")
        for items in current_report:
            print(f"{items} : {current_report[items]}")
    elif(choice=="off"):
        break
    elif(choice in coffee_names):
        sufficient(choice)
        if(s==0):
            break
        money=calc(choice)
        amt=int(input(f"pls pay ₹{money} : "))
        return_amt(choice,amt)
        
        if(s==1 and a==1):
            print("pls wait while prepsring your refreshment coffee")
            print(".........")
            time.sleep(3)
            print(f"Thankyou,here is your {choice}.Enjoy it☕")
            ch=input("Do you want to have a taste of another ?(Y/N) : ").lower()
            if(ch in "Nn" or ch=="off"):
                  break
    else:
        print("invalid word.Pls try again")





