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


class BikeShop(Bicycle):
    
    def __init__(self,name,Bikes=[],netprofit=0,margin=0.2):
        self.name=name
        self.margin=margin
        self.netprofit=netprofit
        self.inventory={}
        if isinstance (Bikes,list):
            for Bike in Bikes:
                    if isinstance(Bike,Bicycle):
                        if Bike in self.inventory:
                            self.inventory[Bike]+=1
                        else:
                            self.inventory[Bike]=1
                    else:
                        raise ValueError("Bikes not passed")
        else:
                raise ValueError("Bike out of stock")
                
    def __str__(self):
        print("Name of the BikeShop: {}".format(self.name))
        print("Inventory List")
        print("Name---Count")
        for cycle,stock in self.inventory.items():
            print(cycle.name,"---",stock)
            
    #To filter out affordable bicycles
    def searchBikes(self,Customers=[]):
        
        if isinstance(Customers,list):
            for customer in Customers:
                if isinstance(customer,Customer):
                    print("Affordable bikes by customer: {}".format(customer.name))
                    for bike in self.inventory:
                        if self.inventory[bike]>0:
                            if bike._cost * self.margin + bike._cost <= customer.fund:
                                print(bike.name,bike._cost)
                        else:
                            print("Out of stock")
                else:
                    raise ValueError("Inventory list only shown to Customers")
               
        
        
    #Sell Bikes based on First come first served
    def SellBicycles(self,Customers=[]):
         if isinstance(Customers,list):
             for customer in Customers:
                  if isinstance(customer,Customer):
                    for bike in self.inventory:
                        if customer.fund >= bike._cost and self.inventory[bike]>0:
                            print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(customer.name,bike.name,bike._cost,customer.fund-bike._cost))
                            self.netprofit=self.netprofit+bike._cost
                            if self.inventory[bike] <= 1: 
                                del self.inventory[bike]
                            else:
                                self.inventory[bike]-=1
                            break    

W1=Wheel(Wheeltypes.Road)
W2=Wheel(Wheeltypes.Road)
F1=Frame()
F2=Frame(Frametypes.Carbon)
WL=[W1,W2]
B1=Bicycle("Atlas",WL,F1)
B2=Bicycle("Venus",WL,F1)
B3=Bicycle("Atlas",WL,F2)
B1.__str__()
B2.__str__()
B3.__str__()

W1.__str__()
BS1=BikeShop("Monrovia",[B1,B2,B2,B3,B3,B3,B3])
BS1.__str__()
Customers=[Customer("Vigs",1000),Customer("Alex",400),Customer("James",500)]
BS1.searchBikes(Customers)
BS1.SellBicycles(Customers)
print("Net Profit afer Sale {}".format(BS1.netprofit))
print("Remaining inventory")
BS1.__str__()