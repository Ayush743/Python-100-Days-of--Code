#-------------------- dictionary and nesting------------------------------------------------->
dict={
    1:"sunday",
    2:"monday",
    3:"tuesday",
    4:"wednesday",
    6:"friday",
}
# retreiving an element from dictionary
print(dict[2])

#adding an element to the dictionary
dict[5]="thursday"
# print(dict)
#----------------grading system------------------->
students_score={
     "Ayush" : 86,
     "Optimus Prime":94,
     "Po": 76,
     "Cosmos" : 90,
     "Shisui" : 95,
     "Hinata" :93,
     "Luffy":56,
     "Naruto": 60
}
student_grade={}
for student in students_score:
    if(students_score[student]>=91 and students_score[student]<=100):
        student_grade[student]="Outstanding"
    elif(students_score[student]>=81 and students_score[student]<=90):
        student_grade[student]="Exceed Exceptions"
    elif(students_score[student]>=71 and students_score[student]<=80):
        student_grade[student]="Acceptable"
    else:
               student_grade[student]="Fail"
# print(student_grade)
# print(students_score)
#----------------Nesting a dictionary inside a dictionary------------------------->
travel_catalogue={
     "France":{
          "city_visited" : ["Paris","Lille","Dijon"],
          "Total_visits": 6
     },
     "India":{
          "city_visited" : ["Meerut","Delhi","Mumbai"],
          "Total_visits": 5
     },
     "Austrailia":{
          "city_visited" : ["Sydney", "Melbourne", "Brisbane", "Perth"],
          "Total_visits": 4
     }
     
}
#--------------------Nesting dictionary inside a list--------------------------------------->
travel_list=[
     {
          "country":"France",
          "city_visited" : ["Paris","Lille","Dijon"],
          "Total_visits": 6
     }
     ,
     {
          "country":"India",
          "city_visited" : ["Meerut","Delhi","Mumbai"],
          "Total_visits": 5
     }
     ,
     {
          "country": "Austrailia",
          "city_visited" : ["Sydney", "Melbourne", "Brisbane", "Perth"],
          "Total_visits": 4
     }    
     
]

def add_new_country(country,visits,city):
     country_dict={
          "country" : country,
          "city_visited" : city,
          "Total_visits" : visits
     }
     travel_list.append(country_dict)
add_new_country("Finland",5,["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"])
# print(travel_list)



#------------------Blind Auction------------------------------------------------->
auction_dict={}
while True:
     name=input("Enter your name : ")
     bid=int(input("What's your bid : $"))
     ch=input("Do you want to continue ? (Y/N)")
     auction_dict[name]=bid
     if(ch in "Nn"):
          break
maximu_bid=max(auction_dict.values())
for winner in auction_dict:
     if(auction_dict[winner]==maximu_bid):
          print(f"The winner of the auction is {winner} with ${maximu_bid} bid")
     
