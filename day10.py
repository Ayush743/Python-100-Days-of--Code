#-------------functions with return values------------------->
def format_name(f_name,l_name):
    return f"{f_name.title()} {l_name.title()}"
#print(format_name("ayUsh","uchIha"))
#------------------Multiple return values---------------------->
def format():
    f_name=input("Enter your first name : ")
    l_name=input("Enter your last name : ")
    if(f_name=="" or l_name==""):
        return
    else:
         return f"{f_name.title()} {l_name.title()}"
# print(format())


#--------Calculating number of days based on the input month and year----->
days_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def leap_year(year):
    if(year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
def days_calc(year,month):
    """Calculate the number of days  based on given month and year"""
    if(month>12 or month<1):
         return "invalid Month"
    elif(leap_year(year) and month==2):
            return 29
    else:
        return(days_num[month-1])
# year=int(input("Enter the year : "))
# month=int(input("Enter the month : "))
# print(days_calc(year,month))
#-----------Calculator------------------------------->
def calc(a,b,op):
     match op:
        case "+":
               return a+b
        case "-":
               return a-b
        case "*":
               return a*b
        case "/":
                return a/b
        case _:
               return("invalid operator")
        
          
     
num1=int(input("Enter the first number : "))
while True:
    num2=int(input("Enter the second number : "))
    operator=input("Enter the type of operation \n1.) Add (+) \n2.) Subtract (-) \n3.) Multiply (*) \n4.) Division (/) :\n")
    print(f"{num1} {operator} {num2} = {calc(num1,num2,operator)}")
    prev_ans= calc(num1,num2,operator)
    ch=input(f"do you wish to continue the calculation (c) with {prev_ans}  or start again (s) : ").lower()
    if(ch=="c"):
         num1=prev_ans
       
    else:
        break


