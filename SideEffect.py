def side_effect(value):
    #List Changes.
    #Number does not change
    #Boolean does not change
    #string does not change
    #tuple does not change
    #Dictonary changes
    
    #Dictionaries and Lists are Mutable?
    
    #value[1]="orange"
    #value=value+1
    #value=False
    #value="newstring"
    #value=(3,4)
    value["test"]="second"
    print("Inside the function, value is {}".format(value))
    

if __name__=="__main__":
   # value=["red","green","blue"]
   #value=1
   #value=True
   #value="oldstring"
   #value=(1,2)
   value={"test":"First","Hello":"World"}
print("Outside the function, the value starts as {}".format(value))

side_effect(value)

print("Outside the function, the value is now {}".format(value))