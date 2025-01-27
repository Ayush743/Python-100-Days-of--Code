
#------BMI Calculator---------------->

height=float(input("Enter your height (m) : "))
weight=float(input("Enter your weight (kg): "))
BMI=int((weight)/(height*height))
print("BMI :",BMI)

#--------Use of f to include variable with multiple datatypes
iswin=True
name="Ayush"
age=21
print(f"my name is {name} and i am {age} years old and mywin is {iswin}")

#--------- Age analysis--------->
age=int(input("Enter your age:"))
years=90-age
months=years*12
weeks=years*52
days=years*365
print(f"you have {years} years,{months} months,{weeks} weeks and {days} days left")


#------->Tip Calculator------------>
print("Welcome to the tip calculator..")
bill=float(input("What was your total bill? $"))
tip_per=int(input("What percentage tip you like to give? 10,12 or 15 ? :"))
total_bill=bill +(bill*tip_per)/100
num_person=int(input("How many people to split the bill : "))
div_bill="{:.2f}".format(total_bill/num_person)
print(f"each person should pay ${div_bill}")