from collections import OrderedDict
from operator import itemgetter
from enum import Enum


#Generic Parent class containing common attributes
class Parts(object):
    def __init__(self,weight,cost):
        self._weight=weight
        self._cost=cost


class Wheeltypes(Enum):
    BMX=(2,20)
    Road=(1,20)
    Track=(1,25)

class Frametypes(Enum):
    Aluminium= (110,120)
    Carbon = (115,200)
    Steel= (112.5,250)
    

#First part- Wheel        
class Wheel(Parts):
    def __init__(self,wheeltype=Wheeltypes.BMX):
        if isinstance(wheeltype,Wheeltypes):
            super().__init__(wheeltype.value[0],wheeltype.value[1])    
        else:
            raise ValueError("Invalid Wheel type")
            
    def __str__(self):
        print("Wheel details {} {}".format(self._cost,self._weight))
        
#Second Part- Frame
class Frame(Parts):
    def __init__(self,frametype=Frametypes.Aluminium):
        if isinstance(frametype,Frametypes):
            super().__init__(frametype.value[0],frametype.value[1])    
        else:
            raise ValueError("Invalid Frame type")
            
    def __str__(self):
        print("Frame details {} {}".format(self._cost,self._weight))

#Happy Customer
class Customer(object):
    def __init__(self,name,fund):
        self.name=name
        self.fund=fund
        
    def __str__(self):
        print("I am {} and I have {} funds".format(self.name,self.fund))
        
        
#Combination of Wheels and Frames- Logic here to get wheels of the same type   
#class BicycleParts(Wheel,Frame):
   #def __init__(self,wheeltype,count,frametype):
    #   BicycleCost=0
     #   F1=Frame(frametype)
     #  BicycleCost+=F1._cost
     #  BicycleWeight+=F1._weight
#    for i in range(0,count):
 #        W1=Wheel(wheeltype)
  #      BicycleCost+=W1._cost
   #    BicycleWeight+=W1._weight
    #    super().__init__(BicycleWeight,BicycleCost)
        
#Finished Product
class Bicycle(Parts):
    def __init__(self,name,Wheels,Frame):
        TotalCost=0
        TotalWeight=0
        TotalCost+=Frame._cost
        TotalWeight+=Frame._weight
        if isinstance (Wheels,list):
            for Wheel in Wheels:
                TotalCost+=Wheel._cost
                TotalWeight+=Wheel._weight
        super().__init__(TotalWeight,TotalCost)
        self.name=name
        
        
    def __str__(self):
        print("Name: {} Weight: {}lbs Price: ${}".format(self.name,self._weight,self._cost))



#Bikeshops selling Bikes---Add NetProfit as an Instance Variable
class BikeShop(Bicycle):
    self.NetProfit=0
    def __init__(self,name,Bikes,margin=0.2):
        self.name=name
        self.margin=margin
        self.inventory={}
        for Bicycle in Bikes:
            self.inventory[Bicycle.name]=self.margin*Bicycle._cost+Bicycle._cost
            
    def __str__(self):
        print("Name of the BikeShop: {}".format(self.name))
        print("Inventory List")
        for cycle,sp in self.inventory.items():
            print(cycle,sp)
            
    #To filter out affordable bicycles
    def filterBicycles(self,Customers):
     
        for Customer in Customers:
            print("Affordable Bicycles by {}".format(Customer.name))
            for key in self.inventory:
                    if Customer.fund >= self.inventory[key]:
                        print(key)
    
    #Sell Bikes based on First come first served
    def SellBicycles(self,Customers):
       for Customer in Customers:
            for key,value in self.inventory.items():
                    if Customer.fund >= value:
                        print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
                        BikeShop.NetProfit=BikeShop.NetProfit+value
                        del self.inventory[key]
                    break    
                
    #Sell Bikes based on the max amount affordable by the customer
    def SellBicyclesMaxProfit(self,Customers):
       for Customer in Customers:
            for key,value in sorted(self.inventory.items(),reverse=True):
                    if Customer.fund >= value:
                        print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
                        BikeShop.NetProfit=BikeShop.NetProfit+value
                        del self.inventory[key]
                    break    
                    
   
class BikeManufacturer(object):
    def __init__(self,name,profitpercent):
        self.name=name
        self.profitpercent=profitpercent
    
    def buildcycles(self):
        BikeList=[Bicycle("Atlas","Road","Carbon"),Bicycle("Neptune","bmx","Aluminium"),Bicycle("Pluto","track","steel")]
        return BikeList