import random
#global variables
drink=[]
preferences={}
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
#Change in GIT
#function to make the drink
def contents(preferences):

    for key,value in preferences.items():
        if value:
            drink.append(random.choice(ingredients[key]))
    print("YO! Your drink is {}.".format(random.choice(cocktailnames))+" " + "It contains")
    for item in drink:
        print(item)

#function to ask customer preference
def ask(questions):
    print("Hi there")
    print("How would you like your drink to be? Enter y or yes for selection")
    
    for key,value in questions.items():
        print(value)
        my_input = raw_input()
        if my_input=="y" or my_input=="yes":
            preferences[key]=True
        else:
           preferences[key]= False
    contents(preferences)      
   # return preferences

if __name__=="__main__":
        ask(questions)
       
