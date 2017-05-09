import random
#global variables
custorder={}
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
def makedrink(preferences,cname):
    drink=[]
    for key in preferences:
        if preferences[key] == True:
            drink.append(random.choice(ingredients[key]))
   
    if len(drink)>0:
        drinkname=random.choice(cocktailnames)
        drink.append(drinkname+" "+"Containing")
        custorder[cname]=drink
        return custorder
    else:
        print("Umm, you didnt choose from any of the choices")

#function to ask customer preference
def TakeOrder(questions):
    preferences={}
    for key,value in questions.items():
        print(value)
        my_input = input()
        if my_input.lower() in ['yes','y','yeah','yup']:
            preferences[key]=True
        else:
           preferences[key]= False
    ServeDrink(cname,makedrink(preferences,cname))      

#function to Welcome Customer
def Welcome(cname):
    print("How would you like your drink to be? Enter y or yes for selection")
    TakeOrder(questions)
    ReOrder(cname)

#function to provide another drink
def ReOrder(cname):
    customer_choice= input("Would you like another drink?\nHit TIP if you want to leave\n")
    if customer_choice.lower() in ['tip','n','no']:
        print("Thanks for coming {}. Hope you enjoyed your time".format(cname))
        del(custorder[cname])
    return

#function to serve drink
def ServeDrink(cname,custorder):
    for item in reversed(custorder[cname]):
       print (item)
    
if __name__=="__main__":
        while True:
            cname=input("Show us your ID\n")
            if cname in custorder:
                c_choice1=input("Would you like same drink?\nHit Y, else Hit N\n")
                if c_choice1.lower() in ['yes','y','yeah','yup']:
                    print("Here is your next round of")
                    ServeDrink(cname,custorder)
                    ReOrder(cname)
                else:
                    Welcome(cname)
            else:
                if len(cname)> 0:
                    print("Welcome to our bar")
                    Welcome(cname)
                else:
                    break
     
