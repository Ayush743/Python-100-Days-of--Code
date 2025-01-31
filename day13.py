print("------------------------------𝓭𝓪𝔂 13---------------------------------------------->")


# tips to finds bugs and solve them

'''
 1) Describe the problem

 Analyse each step in code and then figure out the problem
 Eg :

 for i in range(1,20):
      if(i==20):     # Here the value of i runs from 1 to 19 and hence it will never be 20 and we get no output
          print("i got it")
Solution : run the loop from i=1 to i=21
'''



 #2)  Reproduce the error i.e find how occasionaly the error occurs in what particular case and then solve it.


'''
from random import randint
bugs=["1🐞","2🐞","3🐞","4🐞","5🐞","6🐞"]
random_index=randint(1,6) 

#since randint include both the endpoints when the value of random_index is 6 it will throw list index out of range error
Solution : change the endpoints of randint function from 0 to 5 i.e randint(0,5)

print(bugs[random_index])
'''


#3) Play the computer and think how computer would interpret each line of code and identify the bug 
'''

year=int(input("Enter your birth year :" ))
if(year>1980 and year<1994):
       print('Melinial generation')
# if the user input 1994 as a birth year it will not give any output
elif( year>1994):
      print("GenZ")
        

'''


#4) Fix the error ,check for the console and identify which  error is shown and then fixed it
# You  can use stackoverflow for reference
"""
age=input("Enter your age : ")
if(age>=18): # here the age is treated as a string rather than integer which cannot be compare with the integer
    print("You are eligible for vote")
else:
    print("you are not eligible")
Solution : convert the input into integer using int() function
    """

#5) print is your friend,if you are getting errors make use of print() to identify the problems
'''

pages=0
words_per_page=0
pages==int(input("Enter the number of pages : ")) #here it returns True or False
words_per_page=int(input("Enter the number of words per page :"))
total_words=pages*words_per_page
print(pages) # returns 0 
print(words_per_page) # returns the user input
print(total_words)


'''
#6)  Debugger use debugger like pyhontutor.com or thonny editor
"""
def mutate(l1):
    l2=[]
    for item in l1:
        new_item=item*2
        l2.append(new_item)
    print(l2)
mutate([45,5,678,43,56,2])
    """

#7) Take a break :) and run your code often and ask stackoverflow