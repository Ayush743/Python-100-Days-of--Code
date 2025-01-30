#--------------Capstone Project---------------------------------------->
import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#----------My Solution------------------------->
# comp_card_01=random.choice(cards)
# comp_card_02=random.choice(cards)
# player_card_01=random.choice(cards)
# player_card_02=random.choice(cards)
# sum_score_player=0
# sum_score_comp=0
# player_list=[player_card_01,player_card_02]
# comp_list=[comp_card_01,comp_card_02]

# play=input("Do you wish to play the game of BlackJack? Type 'y' or 'n' : ")
# if play in "yY" :
#     while True:
#         for score in player_list:
#             sum_score_player+=score
#         print(f"Your Cards: {player_list}, current score :{sum_score_player}")
#         print(f"Computer first card :{comp_card_01}")
#         if(sum_score_player>21):
#                 print("You went over,You Lose...")
#                 break

#         ch=input("Type 'y' to get anohter card, type 'n' to pass :")
#         if(ch in "Yy"):
#             player_card_n=random.choice(cards)
#             player_list.append(player_card_n)
#             if(sum_score_player>21):
#                     print("You went over,You Lose...")
#                     print(player_list)
#                     print(comp_list)
#                     break
#             else:
                  
#                 if(sum(comp_list)<=21):
#                     comp_card_n=random.choice(cards)
#                     if(comp_card_n+sum(comp_list)<=21):
#                                comp_list.append(comp_card_n)
#                 if(sum_score_player>sum_score_comp):
#                   print("You Win .......")
#                   print(player_list)
#                   print(comp_list)
#                   break
#         else:
#               if(sum_score_player>sum_score_comp):
#                   print("You Win .......")
#                   print(player_list)
#                   print(comp_list)
#                   break
# else:
#     print("ok goodbye")
    
         
def  deal_card():
    return random.choice(cards)     
player_cards=[]
comp_cards=[]

for _ in range(0,2):
    player_cards.append(deal_card())
    comp_cards.append(deal_card())
def calculate_score(card_list):
    if(len(card_list)==2 and sum(card_list)==21):
        return 0
    else:
        for card in card_list:
            if card==11 and sum(card_list)>21:
                card_list.remove(11)
                card_list.append(1)
     
        return sum(card_list)
game_over=False
def compare_cards(player,comp):
    a=calculate_score(player)
    b=calculate_score(comp)
    if(a==0):
        print("Win, you have a blackjack")
        print(f"Computer Cards : {comp}, Current Score : {b}")
        print(f"Your Cards : {player}, Current Score : {a}")
    elif(b==0):
        print("Loose, opponent have a blackjack")
        print(f"Computer Cards : {comp}, Current Score : {b}")
        print(f"Your Cards : {player}, Current Score : {a}")
    elif(a>b):
        print("Congratulations you win....")
        print(f"Computer Cards : {comp}, Current Score : {b}")
        print(f"Your Cards : {player}, Current Score : {a}")
    elif(a==b):
        print("It's a draw")
        print(f"Computer Cards : {comp}, Current Score : {b}")
        print(f"Your Cards : {player}, Current Score : {a}")
    elif(a>21):
        print("Loose, You went over..")
        print(f"Computer Cards : {comp}, Current Score : {b}")
        print(f"Your Cards : {player}, Current Score : {a}")
    elif(b>21):
        print("Win, Opponent went over..")
        print(f"Computer Cards : {comp}, Current Score : {b}")
        print(f"Your Cards : {player}, Current Score : {a}")
        
    else :
        print("You Loose")
        print(f"Computer Cards : {comp}, Current Score : {b}")
        print(f"Your Cards : {player}, Current Score : {a}")

play=input("Do you want to play Blackjack type 'y' for yes and 'n' for no : ")
if(play in "Yy"):
        while not game_over:
            player_score=calculate_score(player_cards)
            comp_score=calculate_score(comp_cards)
            print(f" Your cards : {player_cards} , current score : {calculate_score(player_cards)}")
            print(f" Computer first card : {comp_cards[0]}")
            if(player_score>21 or player_score==0 or comp_score==0 ):
                compare_cards(player_cards,comp_cards)
                game_over=True
            else:
                user_should_deal=input("Type 'y' to draw another card,type 'n' to pass :")
                if(user_should_deal in "yY"):
                    player_cards.append(deal_card())
                else:
                    game_over=True
            while(comp_score!=0 and comp_score<17):
                comp_cards.append(deal_card())
                comp_score=calculate_score(comp_cards)
            compare_cards(player_cards,comp_cards)
           
else:
    print("Okay Goodbye")