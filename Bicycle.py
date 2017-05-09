from collections import OrderedDict
from operator import itemgetter

class Bicycle(object):
    def __init__(self,name,weight,cost):
        self.name=name
        self.weight=weight
        self.cost=cost
        self.displayBicycle()
        
    def displayBicycle(self):
        print("Name: {} Weight: {} Price: {}".format(self.name,self.weight,self.cost))
        
class Customer(object):
    def __init__(self,name,fund):
        self.name=name
        self.fund=fund
        self.displayCustomer()
        
    def displayCustomer(self):
        print("I am {} and I have {} funds".format(self.name,self.fund))
        
    #def checkBicycle(self,BikeShop):
     #   print("The affordable bikes are")
      #  for key in BikeShop.inventory:
       #     if self.fund >= BikeShop.inventory.get(key,0):
        #        print key
            
        
class BikeShop(object):
  
    NetProfit=0;
    
    def __init__(self,name,Bikes):
        self.name=name
        self.inventory={}
       
        for Bicycle in Bikes:
            self.inventory[Bicycle.name]=0.2*Bicycle.cost+Bicycle.cost
        
        
    def displayBikeShop(self):
        print("Name of the BikeShop: {}".format(self.name))
        print("Inventory List")
        for cycle,sp in self.inventory.items():
            print(cycle,sp)
            
    def sellBicycles(self,Bicycle):
        BikeShop.NetProfit=BikeShop.NetProfit+self.inventory[Bicycle.name]
        self.inventory.pop(Bicycle.name)
        pass
  
    def filterBicycles(self,Customers):
        print("Affordable Bicycles")
        for Customer in Customers:
            for key in self.inventory:
                    if Customer.fund >= self.inventory[key]:
                        print("Bicycle {} affordable by {} for amount {}".format(key,Customer.name,self.inventory[key]))
    
    
    def SellBicyclesMaxProfit(self,Customers):
       for Customer in Customers:
            for key,value in sorted(self.inventory.items(),reverse=True):
                    if Customer.fund >= value:
                        print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
                        BikeShop.NetProfit=BikeShop.NetProfit+value
                        del self.inventory[key]
                    break    
                    
    def SellBicycles(self,Customers):
       for Customer in Customers:
            for key,value in self.inventory.items():
                    if Customer.fund >= value:
                        print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
                        BikeShop.NetProfit=BikeShop.NetProfit+value
                        del self.inventory[key]
                    break    
    

Customers=[Customer("Vigs",1000),Customer("Alex",200),Customer("James",500)]

Bikes=[Bicycle("Atlas","50lbs",1050),Bicycle("Neptune","50lbs",110), Bicycle("Pluto","50lbs",150),Bicycle("Mars","50lbs",400),Bicycle("Earth","40lbs",1510),Bicycle("Venus","60lbs",500)]

BS1= BikeShop("Mountaineers",Bikes)

print("Initial Inventory")
BS1.displayBikeShop()
print("-----------------")
BS1.filterBicycles(Customers)
BS1.SellBicycles(Customers)
print("-----------------")
print("After Sale, Inventory")
BS1.displayBikeShop()
print("Profit after selling three bikes {}".format(BS1.NetProfit))