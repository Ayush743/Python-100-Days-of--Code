#-----------------------Loops in python-------------->
# student_heights=input("Enter the heights of the students seperated by space :").split(" ") #without using len() or sum() function
# s=0
# c=0
# for height in student_heights:
#     s+=int(height)
#     c+=1
# print("The average height of the students is ",round(s/c))
#---------------Highest score in the class-------------------->
# scores=input("Enter the list of the student's scores : ").split(" ")
# max=int(scores[0])
# for i in range(len(scores)):
#     if(int(scores[i])>max):
#         max=int(scores[i])
# print("The maximum score is :",max)

#--------------minimum score in the class--------------------->
# scores=input("Enter the list of the student's scores : ").split(" ")
# min=int(scores[0])
# for i in range(len(scores)):
#     if(int(scores[i])<min):
#         min=int(scores[i])
# print("The minimum  score is :",min)


#-----------------Calculating even sum from a range------------------------------>
# s=0
# for i in range(0,101,2):
#     s+=i
# print(s)

#-------------------FizzBuzz Challenge--------------------------------------------->
# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print("FizzBuzz",end=" ")
#     elif(i%3==0):
#         print("Fizz",end=" ")
#     elif(i%5==0):
#         print("Buzz",end=" ")
#     else:
#         print(i,end=" ")

#------------------------Random Password Generator---------------------------------------->
import random
print("........Welcome to the Password Generator...............")
# length=int(input("Enter the length of your password : "))
# n_sym=int(input("How many symbols do  you like in your password : "))
# numbers=int(input("How many numbers do  you like in your password : "))
# symbols='!@~$%^&*()_+}{":?><}.,;][\/'
# alphabets="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
# password=[]

# for i in range(numbers):
#     password.append(str(random.randint(0,9)))
# for i in range(n_sym):
#     r=random.randint(0,len(symbols)-1)
#     password.append(symbols[r])
# for i in range(length-(n_sym+numbers)):
#     r=random.randint(0,len(alphabets)-1)
#     password.append(alphabets[r])
# random.shuffle(password)

# print("Your generated password is :","".join(password))

#----------------another method---------------------------------------->
n_chr=int(input("Enter the number of characters in  your password : "))
n_sym=int(input("How many symbols do  you like in your password : "))
n_num=int(input("How many numbers do  you like in your password : "))
password=[]
alphabets=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",":",";","'","<",",",">",".","?","/"]
for i in range(n_chr):
    password.append(random.choice(alphabets))
for i in range(n_sym):
    password.append(random.choice(symbols))
for i in range(n_num):
    password.append(random.choice(numbers))
random.shuffle(password)
print("The password generated is :","".join(password))