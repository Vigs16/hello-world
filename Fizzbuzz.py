def Fizzbuzz(number):
    
    if 0 == number%3:
        print("fizz", end="")
    if number%5==0:
        print("buzz")
        return
    else:
        print(number)   
        
if __name__=="__main__":
    
    for i in range(1,17):
        Fizzbuzz(i)
        
    