def Fizzbuzz(number):
    
    Flag=False
    if 0 == number%3:
        Flag=True
        print("fizz", end="")
    if 0 == number%5:
        print("buzz")
        return
    else:
        if Flag==True:
            print()
            return
        print(number)
        
        
if __name__=="__main__":
    
    for i in range(1,100):
        Fizzbuzz(i)
        
    