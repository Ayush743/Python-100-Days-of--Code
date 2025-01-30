print("Day 1- Python Print Function \nThe function is declared like this:\nprint('what to print)")
print("hello "+input("what is your name?")+"!")

#---------------Swapping two variable----------------->
a=int(input("a:"))
b=int(input("b:"))
print("before swapping a :",a,"and b :",b)
a=a+b
b=a-b
a=a-b
print("after swapping a :",a,"and b :",b)
#-----------------Band Name Generator----------------->
print("Welcome to the Band Name Generator")
while True:
    city=input("What's the name of the city you grew up in ?\n")
    pet=input("What's your pet name ?\n")
    print("Your band name might be "+city+" "+pet)
    ch=input("do you want to continue (y/n):")
    if(ch in "Nn"):
        break
    else:
        continue

num_chr=len(input("Enter your Name?"))
print("your name has "+str(num_chr)+" characters")

#----------------Sum of digits---------------------->

num=input("Enter the number : ")
s=0
for i in num:
    s+=int(i)
print(s)
# print(int(num[0])+int(num[1]))
 #-----------------factorial---------------------->
x= int(input("Enter a number : "))
f=1
for i in range(1,x+1):
    f*=i
print(f)
