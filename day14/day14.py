print("------------------------------𝓭𝓪𝔂 14---------------------------------------------->")

from game_data import data
from random import choice
print("""

 __    __   __    _______  __    __   _______ .______                          
|  |  |  | |  |  /  _____||  |  |  | |   ____||   _  \                         
|  |__|  | |  | |  |  __  |  |__|  | |  |__   |  |_)  |                        
|   __   | |  | |  | |_ | |   __   | |   __|  |      /                         
|  |  |  | |  | |  |__| | |  |  |  | |  |____ |  |\  \----.                    
|__|  |__| |__|  \______| |__|  |__| |_______|| _| `._____|                    
                                                                               
                   __        ______   ____    __    ____  _______ .______      
                  |  |      /  __  \  \   \  /  \  /   / |   ____||   _  \     
                  |  |     |  |  |  |  \   \/    \/   /  |  |__   |  |_)  |    
                  |  |     |  |  |  |   \            /   |   __|  |      /     
                  |  `----.|  `--'  |    \    /\    /    |  |____ |  |\  \----.
                  |_______| \______/      \__/  \__/     |_______|| _| `._____|
                                                                               

""")

score=0
gameover=0
def followers_count(n):
    return n["followers"]
def compare_score(guess,a,b):
    if(a>b):
        return guess in "Aa"
    else:
        return guess in "Bb"
    

    

random_celeb_a=choice(data)
while (not gameover):
    random_celeb_b=choice(data)
    if(random_celeb_a["name"]==random_celeb_b["name"]):
        random_index_n=choice(data)
    print(f"Compare A : {random_celeb_a["name"]}, a {random_celeb_a["description"]} from {random_celeb_a["country"]}")
    print('''
   
 _  _  ____ 
/ )( \/ ___)
\ \/ /\___ |
 \__/ (____/
                                 
                                 
''')
    print(f"Compare B : {random_celeb_b["name"]},{random_celeb_b["description"]} from {random_celeb_b["country"]}")
    A=followers_count(random_celeb_a)
    B=followers_count(random_celeb_b)
    ans=input("Who has more followers? Type 'A' or 'B' :")
    result=compare_score(ans,A,B)
    if(result):
        random_celeb_a=random_celeb_b
        random_celeb_b=choice(data)
        score+=1
        print(f"You are right , you current score : {score}")
    else:
        print(f"Sorry you were wrong, your final score : {score}")
        gameover=1






