print("------------------------------𝓭𝓪𝔂 7---------------------------------------------->")
import random
words_list=[
    'fennel', 'vinegar', 'strawberry', 'quinoa', 'zucchini', 'kiwi', 
    'honeydew', 'garlic', 'eggplant', 'coconut', 'raspberry', 'fennel', 
    'honeydew', 'xigua', 'mint', 'raspberry', 'banana', 'zucchini', 
    'papaya', 'elderberry', 'vinegar', 'strawberry', 'jalapeno', 
    'date', 'garlic', 'watermelon', 'mango', 'almond', 'apple', 
    'vanilla', 'hazelnut', 'basil', 'cherry', 'wasabi', 'xanthan', 
    'nutmeg', 'mint', 'xanthan', 'oregano', 'radish', 'mango', 
    'lentil', 'kiwi', 'parsley', 'iceberg', 'ugli', 'quince', 
    'almond', 'oregano', 'papaya'
]
states= [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

 
word=random.choice(words_list)
i=0
s=0
print('''█▀▀ █░█ █▀▀ █▀ █▀  ▀█▀ █░█ █▀▀  █░█░█ █▀█ █▀█ █▀▄''')
print('''█▄█ █▄█ ██▄ ▄█ ▄█  ░█░ █▀█ ██▄  ▀▄▀▄▀ █▄█ █▀▄ █▄▀ ''')
print(states[0])
l1=[]
for _ in word:
    l1.append("_")
print(" ".join(l1))
print()
print()
while(i<len(word)+6):
    letter=input("Enter a letter : ").lower()
    if(letter not in word):
     
        print("You chose the wrong letter,you loose one life")
        s+=1
    print(states[s])
   
    for chr in range(len(word)):
        if(word[chr]==letter):
            l1[chr]=word[chr]
       
    print(" ".join(l1))
        
    if(l1.count("_")==0 or s==6):
        print()
        break
     
    i+=1
    print()
    

if(l1.count("_")==0):
    print(f"You Win !! , the word is {word}")
else:
    print(f"OOps ! You Lose and the word is {word}")