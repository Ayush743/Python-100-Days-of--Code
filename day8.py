# #--------------function basics-------------------------->
# def greet(name):
#     print("Hii there",name)
#     print("Python is fun!!")
#     print("let's Code 😎")

# def new_greet(name,location):
#     print(f"hello {name}")
#     print(f"what is it like to live in {location} ?")
# #positional argument  
# greet("Ayush")
# new_greet("Ayush","India")
# #keyword argument
# new_greet(location="India",name="ayush")

# from math import ceil
# # no of paint can calculator based on random height and width as well as cover of each can
# def paint_can(height,width,cover):
#     area=height*width
#     num_cans=ceil(area/cover)
#     print(f"The number of cans required are {num_cans} ")
# t_height=int(input("Enter the height of the wall (m) : "))
# t_width=int(input("Enter the width of the wall (m)  : "))
# cover=5
# paint_can(height=t_height,width=t_width,cover=cover)

#------------prime number checker------------------------>
# def is_prime(n):
#     f=0
#     for i in range(1,n+1):
#         if(n%i==0):
#             f+=1
#     if(f==2):
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} is not a prime number")
# is_prime(73)
# is_prime(75)

#-------------------encode decode text------------------->
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt_decrypt(text,shift,type):
    if(type=="decode"):
        shift*=-1
    end_word=""
    for ch in text:
        if(ch in alphabets): 
            pos=alphabets.index(ch)
            new_pos=pos+shift
            ch=alphabets[new_pos]
            end_word+=ch
        else:
             end_word+=ch
    if(type.lower()=="encode"):
        print(f"The encoded text is {end_word}")
    elif(type.lower()=="decode"):
        print(f"The decoded text is {end_word}")


while True:
    direction=input("Type 'encode' to encrypt and Type 'decode' to 'decrypt : ")
    if(direction.lower()=="encode" or direction.lower()=="decode"):
  
            text=input("Enter the message : \n")
            shift=int(input("Type the shift number : "))
            shift%=26
            encrypt_decrypt(text,shift,direction)
            ch=input("do you want to continue (y/n) ?")
            if(ch in "Nn"):
                    print("Goodbye")
                    break
    else:
      print('Invalid word')
   
# i applied ord() and chr() function for encoding but it is not accurate for last characters alphabests
# def encrypt(text,shift):
#     encrypt_text=""
#     for ch in text:
#         asci=ord(ch)
#         encrypt_chr=chr(asci+shift)
#         encrypt_text+=encrypt_chr
#     print(f"The encoded text is {encrypt_text}")
# if(direction=="encode"):
#     encrypt(text,shift)
    
    


    

    