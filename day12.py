print("------------------------------𝓭𝓪𝔂 12---------------------------------------------->")
#--------------------------------Scope--------------------------------->
enemies=1
def inc_enemies():
    enemies=2
    print(f"No of enemies inside the function is : {enemies}")
inc_enemies()
print(f"No of enemies outside the function is : {enemies}")

#---------------Local Scope---------------------------------->
def desc(name,age):
    description={
        "name": name,   # description is only valid inside the body of the function
        "Age" : age
    }
    description["hobbies"]=["watching anime","coding in python"]
    print("desc is defined inside the function", description)
# print(description)
desc("Ayush",21)


#--------------------------Global Scope--------------------------->
animes=["Naruto","one Peice","Bleach","DBZ","Demon Slayer"]
def anime_list():
    print(animes)               #animes is globally available to insdie  function body as well as outside it


anime_list()

def game():
    def navigate():
        print("Move left,right,top,bottom")
    navigate()


#navigate function is not available outside the body of game function

#----------------------modifying the global variable---------------------------------------->
enemies_list=["aliens","Zombies","phirahnas"]
a=2
def enemies():
    global a
    a+=123
    enemies_list.append("sharks")
    print(f"enemies inside the function is : {enemies_list} and a={a}")
enemies()
print(f"enemies outside the function is : {enemies_list} and a={a}")

#--------------------Guess the number---------------------------------->
def random_game_logic(attempt):
    attempts=attempt
    while attempts!=0:
            print(f"You have {attempts} attempts remaining to guess the number")
            guess_number=int(input("Make a guess : "))
            if(guess_number!=random_number):
                if(guess_number>random_number):
                      print("Too High")
                      if(attempts!=1):
                          print("Make a guess again")
                else:
                     print("Too Low")
                     if(attempts!=1):
                          print("Make a guess again")
                     
                attempts-=1
    
            else:
                print(f"That's a correct guess!!. You win, the answer is {guess_number}")
                break
            if(attempts==0):
                 print("You run out of guesses.You loose 😔")


print('''
                                        __  .__                                 ___.                 
   ____  __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
  / ___\|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
 / /_/  >  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \___  /|____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
/_____/             \/     \/     \/             \/     \/       \/            \/    \/     \/       
''')

print("welcome to the number guessing game!")
print("I am thinking of a number between 0 and 1")
diff=input("Choose the level of difficulty type'easy' or 'hard' : ")
import random

random_number=random.randint(1,100)
print(random_number)
if(diff=="easy"):
     random_game_logic(10)
elif(diff=="hard"):
     random_game_logic(5)
else:
     print("Invalid text")
     
   
           
                    

