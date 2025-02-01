print("------------------------------𝓭𝓪𝔂 16---------------------------------------------->")
# from turtle import Turtle,Screen
 
# tom=Turtle()
# # tom.shape("turtle")
# # tom.color("red")
# # tom.forward(200)
# my_screen=Screen()
# print(my_screen.canvheight)
# # my_screen.exitonclick()
# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Pokemon_Name",["Arceus", "Mewtwo", "Rayquaza", "Groudon", "Kyogre", 
#                  "Zygarde", "Eternatus", "Dialga", 
#                  "Lugia", "Giratina "])
# table.add_column("Pokemon_Type",["Normal", "Psychic", "Dragon/Flying", "Ground", "Water", 
#                  "Dragon/Ground", "Poison/Dragon", "Steel/Dragon", 
#                  "Psychic/Flying", "Ghost/Dragon"])
# print(table)
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()
while True:
    options=menu.get_items()
    choice=input(f"what would you like to have {options} : ")
    if(choice=="report"):
        money_machine.report()
        coffee_maker.report()
    elif(choice=="off"):
        break
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and (money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)


