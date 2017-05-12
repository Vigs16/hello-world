from collections import OrderedDict
from operator import itemgetter

class Bicycle(object):
    def __init__(self,name,BicycleParts):
        self.name=name
        self.weight=BicycleParts.BicycleWeight
        self.cost=BicycleParts.BicycleCost
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
    
class Parts(object):
    def __init__(self,weight,cost):
        self.weight=weight
        self.cost=cost
        
class Wheel(Parts):
    def __init__(self,weight,cost,name,):
        super(Wheel,self).__init__(weight,cost)
        self.name=name
        

class Frame(Parts):
    def __init__(self,weight,cost,name):
        super(Frame,self).__init__(weight,cost)
        self.name=name
        
   
class BicycleParts(object):
    BicycleCost=0
    BicycleWeight=0
    
    def __init__(self,wheels,frame):
        BicycleParts.BicycleCost+=frame.cost
        BicycleParts.BicycleWeight+=frame.weight
        for Wheel in wheels:
            BicycleParts.BicycleCost+=Wheel.cost
            BicycleParts.BicycleWeight+=Wheel.weight
       
        
        
    def display(self):
        print("Total Cost {} and Total Weight {}".format(BicycleParts.BicycleCost,BicycleParts.BicycleWeight))
        
F1 = Frame(10,30,"Aluminium")
WL=[Wheel(10,10.2,"Aluminium"),Wheel(10,10.2,"Aluminium")]

BP1= BicycleParts(WL,F1)
BP1.display()


B1= Bicycle("Atlas",BP1)


