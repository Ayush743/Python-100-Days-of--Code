# #-------------Eligible for vote ---------------->
# age =int(input("Enter your age :"))
# if(age>=18):
#     print("Eligible for vote")
# else:
#     print("not eligible for vote")
# #--------------------odd or even----------------
# num=int(input("Enter a number :"))
# if(num%2==0):
#     print(num,"is an even number")
# else:
#     print(num,"is an odd number")
# --------------------Prime number-------------->
# n=int(input("Enter a number :"))
# f=0
# for i in range(1,n+1):
#     if(n%i==0):
#         f+=1
# if(f==2):
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")
#   ---------------using ternary if else ------------>
# h=float(input("Enter your height in cm :"))
# if(h>120):
#    age=int(input("Enter your age :"))
#    result="u are eligible and ticket price is $12" if(age>18)   else "you are eligible and ticket price is $5"
#    print(result)
# else:
#    print("Sorry u are not eligible")
#--------------------------More nested and advance ------------------->
# bill=0
# if(h>120):
#     age=int(input("Enter your age : "))
   
#     if(age>=45 and age<=55):
#             bill=0
#     elif(age>18 ):
#          bill=12
#          print(f"u are eligible")
#     elif(age<=18 and age>12 ):
#         bill=7
#         print("u are eligible ")
#     elif(age<=12):
#             bill=5
#             print("u are eligible")
#     need_photo=input("Do you want photos (Y/N) : ")
#     if(need_photo in "Yy" and not(age>=45 and age<=55)):
#         print("Total bill : $",bill+3)
#     else:
#         print("Total bill : $",bill)
         
# else:
#       print("sorry you are not eligible")


       
         
         

#-----------------------------updated BMI------------------------------------->
# height=float(input("Enter your height (m) : "))
# weight=float(input("Enter your weight (kg): "))
# BMI=round((weight)/(height*height))
# print(BMI)
# if(BMI<=18.5):
#    print("underweight")
# elif (BMI>18.5 and BMI<=25):
#    print("normal weight")
# elif(BMI>25 and BMI<=30):
#    print("overweight")
# elif(BMI>30 and BMI<=35):
#    print("obese")
# else:
#    print("clinically obese")
#-------------------------------------------Leap Year--------------------------------------->
# year=int(input("Enter the year : "))
# if((year%4==0 and year%100!=0) or year%400==0):
#    print(f"{year} is a leap year")
# else:
#    print(f"{year} is not a leap year")
# #---------------or-------------------------->
# if(year%4==0):
#    if (year%100==0):
#         if(year%400==0):
#            print("its a leap year")
#         else:
#            print("its not a leap year")
      
#    else:
#       print("its a leap year")
# else:
#    print("not a leap year")
#-------------------------------------Python Pizza Delivery--------------------------------->
# print("------------Welcome to the Python Pizza Delivery-----------")
# while True:
#                  size=input("Enter the size of pizza (S/M/L) : ")
#                  pepperoni=input("Do you want Pepperoni (Y/N) :")
#                  cheeze=input("Do you want extra chezze (Y/N) :")
#                  piz_price=0
#                  if(size in "Ss"):
#                      piz_price=15
#                  elif(size in "Mm"):
#                      piz_price=20
#                  else:
#                      piz_price=25

#                  if(pepperoni in "Yy"):
#                          if(size in "Ss"):
#                            piz_price+=2
#                          if(size in "MLml"):
#                             piz_price+=3
              
#                  if(cheeze in "Yy"):
#                          piz_price+=1
                     
#                  print("Thanks for ordering your total bill is :$",piz_price)
#                  ch=input("Do you want to order again ? (Y/N) :")
#                  if(ch in "Nn"):
#                       break



#-------------True Love finder 💖😅------------------>
# yourname=input("Enter your name : ").lower()
# lovername=input("Enter your lover name : ").lower()
# name=yourname+lovername
# true=0
# love=0
# for i in name:
#     if(i in "true"):
#         true+=1
# for i in name:
#     if(i in "love"):
#         love+=1

# # print(f"The chances of ur true love({yourname}💖{lovername}) are {true}{love}%")
# score=str(true)+str(love)
# truelove=int(score)
# if(truelove<10 or truelove>90):
#     print(f"Your score is {truelove} ({yourname}💖{lovername}),you go together like coke and mentos.")
# elif(truelove>=40 and truelove<=50):
#     print(f"your score is {truelove} ({yourname}💖{lovername}) and you are alright togehter " )
# else:
#     print(f"your score is {truelove} ({yourname}💖{lovername})")


''' _                                                                        _             
| |_ _ __ ___  __ _ ___ _   _ _ __ ___    __ _  __ _ _ __ ___   ___ _ __ | | __ _ _   _ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \  / _` |/ _` | '_ ` _ \ / _ \ '_ \| |/ _` | | | |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | (_| | (_| | | | | | |  __/ |_) | | (_| | |_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|  \__, |\__,_|_| |_| |_|\___| .__/|_|\__,_|\__, |
                                         |___/                     |_|            |___/ '''



print('''
    ⠀⠀⠀⠀⠀⠀⣀⡤⠶⠒⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠒⠶⣄⣀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀
⠀⠀⣴⠟⠀⠀⠀⢀⣠⣴⣶⣾⡛⣟⠻⢳⠖⡲⢒⠲⣒⠒⡖⣒⢒⠲⡒⣒⠒⡒⢒⡒⡒⢒⠒⣒⠒⣒⠒⣒⠒⡒⣒⢒⡒⣒⢒⡒⣒⢒⡒⣒⢒⡒⣒⢒⡒⣒⢒⡒⣒⢒⡒⣒⠲⣒⠛⡟⡶⣤⣀⠀⠀⠀⠈⠳⡄⠀
⠀⣼⠁⠀⠀⠀⣴⠟⠉⠉⠉⠉⠛⠳⢮⣅⠘⠀⠋⠐⠄⠉⠔⠐⠈⠐⠀⠀⢁⣈⣠⣴⣤⣥⣌⣀⡀⠀⠁⠀⠈⠐⠀⠂⠐⠀⠊⠐⠁⠊⠔⠁⠊⠔⠡⠊⠰⠁⠚⠰⠁⠚⠰⠁⠣⢈⠣⠘⠴⢡⠛⣷⣄⠀⠀⠀⠹⡆
⢸⠃⠀⠀⠀⣾⣃⣤⣤⠴⣤⣄⡀⠀⠀⠙⢷⣄⠀⠂⠀⠂⣀⣤⣶⣶⠿⣟⢿⡛⣏⢯⡹⣍⣛⡛⢿⠳⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠁⠀⠀⠠⠀⠐⠀⠀⠈⠀⠄⠈⠀⠀⠀⠁⠀⠂⠘⡐⠺⣄⠀⠀⠀⢹
⣿⠀⠀⠀⢸⣟⠋⠙⠻⣦⡀⠀⠙⢦⡀⠀⠀⠘⣦⣠⣶⡿⢿⣭⢳⣎⢿⡼⣳⣻⢽⣮⢳⡭⢖⡹⢆⠯⣔⢩⡙⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢺⠀⠀⠀⠸
⣿⠀⠀⠀⢸⡇⠀⠀⠀⠀⠻⣄⠀⠀⠹⣆⠀⢠⣾⢟⣣⣝⡳⣎⡷⣞⢯⡞⡷⣭⢷⣚⢧⡻⢬⠑⣊⠳⡌⢧⡜⢢⠜⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠠
⡟⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠘⣧⠀⠀⢈⣶⠿⣭⢺⡵⣎⢷⡹⣞⠽⣮⡝⣯⡳⣏⠾⣡⠏⢎⡱⢈⠵⡘⢥⢚⡵⣊⠥⡙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡇⠁⠀⠀⠀⠀⠀⠈⣧⣴⡿⢏⡷⢎⡗⡮⣝⢮⡳⣭⣛⢶⡹⢧⣟⡼⢣⢇⠚⡄⠒⠡⠂⠐⣈⠲⣘⠦⡓⢌⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡒⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡇⢈⠀⠀⠀⠀⠀⢠⣾⠯⣜⠯⡼⡹⢼⡱⣎⢧⢳⣣⠟⣮⡝⣯⢞⡵⢫⠜⠢⠌⠁⠀⠀⠁⠄⡂⢇⠳⣍⠎⣰⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠥⠀⠀⠀⠀
⡇⠀⠀⠀⢸⠆⡁⠀⠀⠀⠀⣰⣿⡹⢎⢧⡛⢶⡙⣦⣳⣜⣮⡳⡵⣛⢶⡹⣎⠿⣜⢧⡙⢆⠡⠀⠀⠀⠀⡐⠌⢎⡱⢎⣼⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⠇⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡃⠄⡁⠀⠀⣸⣿⢣⡝⣫⢖⣹⣶⣿⣿⣿⣿⣿⣿⣷⡝⣮⢳⣏⣟⢮⡳⡜⣌⠢⣁⠀⠠⠁⡜⢈⠦⡱⢎⣼⣿⣿⡟⢁⣠⣴⣤⣤⣤⣤⣤⣴⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡅⠒⡀⠁⢀⣿⣯⢓⡮⣵⣿⣿⣿⣿⡿⡟⣋⠿⣿⣿⣿⡼⣳⢞⡼⣏⢷⣙⠦⡓⣄⠊⠥⡘⢄⠣⡜⡱⢎⡲⡉⢿⣿⣿⣿⣿⡿⠛⠛⠛⠛⣿⡿⠛⠉⠀⠀⠀⠈⠙⣦⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
⡇⠀⠀⠀⢸⢎⠡⡐⠀⢘⣿⣧⢋⠶⣿⣿⣿⣿⢣⣱⣷⣌⡜⣻⣿⣿⣿⡱⣯⠽⣞⡯⣞⡳⡝⣤⢋⢖⡡⢊⠖⣡⠝⣎⠵⣨⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠉⣷⠀⠀⠀⠀⠀⠀⠀⡺⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡏⡐⠄⠀⠈⢻⣧⢏⡞⣽⣿⣿⣿⣆⣿⣿⣷⡬⢹⣿⣿⣿⡽⣎⡿⣝⡾⣽⣳⣽⢲⣫⢎⡵⡩⢎⡥⣛⡬⢳⣿⣿⣿⠃⠀⠀⠀⢀⣀⣄⡀⠀⡟⡇⠀⣴⠿⠛⣷⡄⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡳⢈⠆⠀⠀⢸⣿⢎⡶⡘⣿⣿⣿⣿⣿⣿⣿⡜⣣⣿⣿⣿⣟⣧⢿⣹⣞⣷⣻⣞⡿⣼⣫⢖⣝⡺⢴⢫⠴⣻⣿⣿⣿⠀⠀⠀⢠⣿⢛⢹⣿⢐⣦⡇⠰⣿⣷⣾⣿⠇⣹⠇⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣇⠃⡔⠀⠀⠀⣿⣧⢳⡝⡴⢻⣿⣿⡟⣏⡳⡜⣥⣿⣿⣿⣿⢮⢷⣛⣾⣳⣟⣾⣟⣷⣛⡾⡼⣭⠳⣍⢶⡿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⡿⠈⣼⠀⠀⠻⠿⠿⠋⢠⠟⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣎⠱⡀⠀⠀⠀⣼⣿⡳⣞⡵⣳⡜⣦⡝⣮⢳⡝⣲⣿⣿⣿⣿⢯⣞⡿⣞⡷⣯⡷⣿⡞⣧⢻⡵⢣⣛⣼⠟⠀⢿⣿⣿⣇⠀⠀⠀⠙⠛⠋⠀⣸⠃⠀⠀⠀⠀⢀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣏⠦⡑⠀⠀⠀⠀⣿⡿⣜⡳⢧⣛⡶⣹⣎⢷⣹⣿⣿⣿⣿⡿⣏⣾⡽⣯⢿⡷⣿⣳⢽⣚⢧⡛⣱⣾⠏⠀⠀⠈⢻⣿⣿⣦⣀⡀⠀⠀⢀⣼⣿⣷⣤⣤⣠⣤⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣯⡒⠥⠀⠄⠀⠀⢿⣿⣽⣝⡳⣏⣾⢳⣎⣷⣿⣿⣿⣿⣿⣻⡽⣾⡽⣟⣯⣟⡷⣹⢎⡳⠎⠐⣼⣿⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡿⠛⢻⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣷⡹⣌⢁⠂⠀⠀⢸⣿⣿⣾⣝⣳⢮⣷⣿⣿⣿⣿⣿⢿⣳⣽⣻⢷⣿⣻⡗⣯⢞⣧⡛⡔⠃⠀⢸⣟⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⠋⠀⠀⣼⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣿⡵⣊⠤⢂⠀⠄⠀⢿⣽⣻⢿⣿⣿⣿⣿⣿⣿⡿⣯⢯⡷⣯⣟⡿⣞⢧⣛⡧⣟⢦⡝⢬⡑⢠⠠⣿⣤⣶⢶⣄⠀⠀⠀⣼⣿⢿⠇⠀⢠⣾⣿⣿⠃⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠸⠿⣷⣣⠚⡤⠈⣀⡤⠈⢻⣽⢾⣽⣻⣟⣿⣿⣛⣷⣯⣿⣽⣳⣯⣟⣼⣫⢷⡹⣎⡳⣜⢦⣱⣯⣿⢿⣻⠅⡊⢿⡆⠀⣼⣿⣟⡿⢀⣴⣿⢟⣽⠃⠀⠀⠀⠀⠀⠉⠙⠛⠒⠀⠀⠀⢀⠤⠤⢤⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡄⠈⠉⠛⠛⠋⠁⠀⠀⢀⡹⢿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡿⣭⢟⣤⣻⣷⣾⣿⠻⣼⣷⡿⢿⣱⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠠⠂⠀⠀⠠⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣦⣤⣀⣀⣀⣀⣀⣠⠴⠋⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣯⣿⣿⣿⡿⣯⡯⣽⣿⡿⣙⣾⠿⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠖⠈⠀⠀⠀⠐⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡃⠀⠈⠉⠀⣀⣤⣤⣶⣾⢿⣿⡿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣟⡿⢯⢷⡻⣗⣿⣾⢯⡷⣭⣯⡀⠀⣠⡼⠟⣟⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠨⠀⠀⠀⠀
⡇⠀⠀⠀⢸⠄⠀⠀⢰⣿⣿⣿⣽⣶⣯⣾⢷⣻⣝⡳⣏⣷⣻⣼⢳⡝⣾⡽⣽⢯⣟⡽⣫⡽⣯⢿⡽⣳⢿⣼⣻⡵⣿⡻⣝⣎⢳⠽⣜⣯⣟⡷⣧⢾⡽⣿⣧⠀⠀⣿⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⢒⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡇⠀⠀⠈⠈⠏⠉⠉⠉⠙⣿⣯⢷⣫⣷⣿⣾⣽⢞⣣⢟⣶⣻⣽⡻⣜⡳⢭⣻⢵⣯⣻⡽⢯⣶⢻⣼⣏⡗⣣⢎⡱⣋⠾⣜⣯⢿⡽⣯⣟⣷⡞⠀⠀⣿⠀⠀⠀⠀⠀⢰⡃⠀⠀⠀⠀⠀⠀⢌⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡇⠠⠤⢀⣀⡀⠀⠀⠀⠀⠙⠛⠛⠛⠉⠁⠈⢻⣟⣮⣟⣾⣵⣿⣷⣍⣳⡹⣎⡿⢶⣯⡟⣯⣚⢳⢞⣯⣞⡱⢎⡵⣹⣿⠛⠚⠛⠛⠉⠉⣼⣀⣤⠾⠋⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⢊⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡇⡐⢠⠀⡀⠉⠙⠳⠦⣤⣤⣀⡀⠀⠀⠀⠀⠠⠉⣛⠉⠁⡀⠀⠻⣾⣧⢿⡽⣽⣿⣾⣽⢲⣍⡻⢮⣽⣳⡽⣎⡵⣫⣟⣷⣤⣤⣤⣤⣴⣾⡿⠃⠀⠀⠀⢠⡤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣗⡈⠄⠂⡔⢉⠆⡱⢐⠰⡈⠭⣙⠻⢷⠶⣤⣤⣀⡀⠈⠀⠀⠁⠠⠈⡉⠛⠉⠉⠀⢈⣻⣷⡮⣝⣻⢾⣟⣷⣿⣼⣷⣿⣾⣽⣯⠿⠿⠛⠉⠀⠀⠀⠀⢰⡏⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⠀⠀
⡇⠀⠀⠀⢸⣿⣷⣮⣥⣐⣀⢂⠁⠎⡰⢁⠞⡠⢍⢢⡙⢢⠍⡝⡛⡟⢶⣶⣤⣀⣀⠀⠀⣡⡴⠾⠋⠉⠈⠻⠾⣽⠿⠟⢋⣩⡴⠞⢻⡿⠀⠀⠀⠀⠀⠀⣀⣠⣞⣚⣿⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⣀⣐⠀⠀⠀⠀
⣷⠀⠀⠀⢼⣿⣷⡹⣎⣿⣿⣿⣶⣾⣤⣌⣂⡡⠊⡔⢨⠁⠞⡰⠱⢌⢣⠒⡬⢍⠏⡿⡟⠉⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⡛⡍⠂⠁⢀⣇⣠⣤⠶⠖⠛⠛⠉⠉⢁⣀⣀⣀⣀⣠⣀⣀⣀⣀⣀⣄⡉⠭⣙⢻⠀⠀⠀⠀
⣿⠀⠀⠀⢸⣿⣷⡛⡼⣿⣿⣻⣽⣿⣻⢿⣟⡿⣿⣶⣧⣮⣔⣡⠃⢌⠢⡉⠴⡉⠜⡰⡇⠀⠀⠀⠀⣀⣤⠶⢻⡿⢀⠃⠁⣐⣤⠶⠛⠉⠁⠀⣀⣤⣤⣶⣾⡿⣿⢿⣿⣻⡿⣿⢿⣿⣿⣿⣿⢿⣿⣿⣿⣿⠀⠀⠀⢀
⢸⡄⠀⠀⠈⣿⣷⢯⡵⣿⣯⢿⡽⣳⢯⣟⢾⣽⢳⣞⣿⣻⣟⡿⣿⣿⢶⣮⣴⣁⣎⠰⣇⢀⣠⡶⢟⠩⠑⠈⢀⡷⢠⣴⠟⠉⠀⠀⣠⣴⡾⣟⡻⣝⣮⣿⠾⠽⠿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠿⠿⠿⣿⣿⡟⠀⠀⠀⢸
⠈⢿⡀⠀⠀⠈⢻⣿⡶⣿⢯⡿⣽⣳⢯⣞⡳⣎⠻⣜⣿⣷⣯⣟⣷⣯⢷⣹⣿⣏⡛⣟⠿⡛⠣⢈⠀⠄⠠⠈⣠⣿⠏⠀⠀⢀⣴⣾⣿⣣⣿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⡀⠄⠢⠄⣐⢂⣾⠏⠀⠀⠀⢠⠇
⠀⠈⢳⡄⢀⠀⠀⠈⠛⠿⣿⣽⣷⣯⣿⣾⣵⣯⣿⣼⣿⣾⣷⣯⣿⣯⣿⣷⣿⣧⣿⣬⣷⣬⣶⣴⣮⣴⣥⣶⣿⣥⣤⣤⣴⣿⣿⣿⣿⣭⣤⣤⣤⣤⣤⣤⣤⣥⣴⣤⣦⣥⣴⣬⣴⣤⣦⣵⡾⠟⠋⠁⠀⠀⠀⣠⠋⠀
⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀
⠀⠀⠀⠀⠈⠉⠓⠶⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⡤⠶⠋⠁⠀⠀⠀⠀
''')
print('''.......              _                            _          _                                       _     _                 _ 
__      _____| | ___ ___  _ __ ___   ___  | |_ ___   | |_ _ __ ___  __ _ ___ _   _ _ __ ___  (_)___| | __ _ _ __   __| |
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '__/ _ \/ _` / __| | | | '__/ _ \ | / __| |/ _` | '_ \ / _` |
 \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | |  __/ (_| \__ \ |_| | | |  __/ | \__ \ | (_| | | | | (_| |
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_|  \___|\__,_|___/\__,_|_|  \___| |_|___/_|\__,_|_| |_|\__,_|........")
print(".......Welcome to the treasure island ,your mission is to find the hidden treasure........''')



direction=input("Do you want to go left or right ? :").lower()
if(direction=="left"):
    print("There is river ahead")
    swin_wait=input("Do want to swim or wait for the boat? :").lower()
    if(swin_wait=="wait"):
        print("there is a cave ahead")
        cave=input("Do you want to enter?(yes/no) : ").lower()
        if(cave=="no"):
            dir=input("Do you want to  turn left or right? :")
            if(dir=='right'):
                print("There is a strange portal ahead .....")
                portal=input("do you wish to enter yes/no  : ").lower()
                if(portal=='yes'):
                    print("The door of the portal closed from behind")
                    print("There are three doors in red,blue,green colour")
                    door=input("Which door you want to open (red,blue,green) :").lower()
                    if(door=="red"):
                        print("congratulations!!,you found the treasure 🪙🪙.....")
                    elif door=="blue":
                        print("oops!.Gameover you drowned with flood 🌊")
                    else:
                        print("oops!,GameOver you were eaten by lion ☠️")
                else:
                    print("Oops!,GameOver you turned into a rat by a wizard chasing you")
            else:
               print("Oops!,GameOver the dragon caught you with his claws 🐉")
        else:
            print("Oops!,GameOver you were eaten by snake 🐍")
    else:
        print("Oops!,GameOver you were eaten by crocodile 🐊")
else:
    print("Oops!,GameOver you fall into a pit 🕳️")