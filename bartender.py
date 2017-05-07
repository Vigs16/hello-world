import random
#global variables
customerhistory={}
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
cocktailnames= ["SakeBomb","Zombie","Tom and Jerry","Black and Tan","Black Velvet",]

#function to make the drink
def contents(preferences,cname):
    drink=[]
    for key,value in preferences.items():
        if value == True:
            drink.append(random.choice(ingredients[key]))
   
    if len(drink)>0:
        drinkname=random.choice(cocktailnames)
        customerhistory[cname]=drink
        print("YO! Your drink is {}.".format(drinkname)+" " + "It contains")
        for item in drink:
            print(item)
        drink.append(drinkname+" "+"Containing")
    else:
        print("Umm, you didnt choose from any of the choices")

#function to ask customer preference
def ask(questions):
    preferences={}
    for key,value in questions.items():
        print(value)
        my_input = raw_input()
        if my_input=="y" or my_input=="yes":
            preferences[key]=True
        else:
           preferences[key]= False
    contents(preferences,cname)      

#function to Welcome Customer
def Welcome(cname):
   
    print("How would you like your drink to be? Enter y or yes for selection")
    ask(questions)
    Reorder(cname)

#function to provide another drink
def Reorder(cname):
    customer_choice= raw_input("Would you like another drink? \n Hit TIP if you want to leave\n")
    if customer_choice=="TIP":
        print("Thanks for coming {}. Hope you enjoyed your time".format(cname))
        del(customerhistory[cname])
    return
    
if __name__=="__main__":
        while True:
            cname=raw_input("Show us your ID\n")
            if cname in customerhistory:
                c_choice1=raw_input("Would you like same drink?\n Hit Y, else Hit N\n")
                if c_choice1=="Y":
                    print("Here is your next round of")
                    for item in reversed(customerhistory[cname]):
                        print item
                        
                    Reorder(cname)
                else:
                    Welcome(cname)
            else:
                print("Welcome to our bar")
                Welcome(cname)
               
     
