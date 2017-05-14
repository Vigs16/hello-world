from collections import OrderedDict
from operator import itemgetter

class Parts(object):
    def __init__(self,weight,cost):
        self._weight=weight
        self._cost=cost


class Bicycle(Parts):
    def __init__(self,name,BicycleParts):
        super().__init__(BicycleParts.BicycleWeight,BicycleParts.BicycleCost)
        self.name=name
        self.__str__()
        
        
    def __str__(self):
        print("Name: {} Weight: {}lbs Price: ${}".format(self.name,self._weight,self._cost))
        
class Customer(object):
    def __init__(self,name,fund):
        self.name=name
        self.fund=fund
        
    def __str__(self):
        print("I am {} and I have {} funds".format(self.name,self.fund))

class BikeShop(object):
  
    NetProfit=0;
    
    def __init__(self,name,Bikes):
        self.name=name
        self.inventory={}
       
        for Bicycle in Bikes:
            self.inventory[Bicycle.name]=0.2*Bicycle.cost+Bicycle.cost
        
        
    def __str__(self):
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
    

        
class Wheel(Parts):
    def __init__(self,wheeltype):
        wheeltypes={'bmx':(2,20),'road':(1,20),'track':(2.5,20)}
        if(wheeltype.lower() in wheeltypes):
            super().__init__(wheeltypes[wheeltype.lower()][0],wheeltypes[wheeltype.lower()][1])    
        else:
            raise ValueError("Invalid Wheel type")
            
    def __str__(self):
        print("Wheel details {} {}".format(self._cost,self._weight))

class Frame(Parts):
    def __init__(self,Frametype):
        Frametypes={'aluminium':(10,120),'carbon':(15,200),'steel':(112.5,250)}
        if(Frametype.lower() in Frametypes):
            super().__init__(Frametypes[Frametype.lower()][0],Frametypes[Frametype.lower()][1])    
        else:
            raise ValueError("Invalid Frame type")
     
    def __str__(self):
        print("Frame details {} {}".format(self._weight,self._cost))
   
class BicycleParts(Wheel,Frame):
    BicycleCost=0
    BicycleWeight=0
    
    def __init__(self,wheeltype,count,frame):
        BicycleParts.BicycleCost+=frame._cost
        BicycleParts.BicycleWeight+=frame._weight
        for i in range(0,count):
            W1=Wheel(wheeltype)
            BicycleParts.BicycleCost+=W1._cost
            BicycleParts.BicycleWeight+=W1._weight
       
    def __str__(self):
        print("Total Cost $ {}  and Total Weight {} lbs".format(BicycleParts.BicycleCost,BicycleParts.BicycleWeight))
        

WL=[Wheel("road"),Wheel("road")]
W1=Wheel("road")
F1=Frame("Carbon")
BP1= BicycleParts("road",2,F1)
BP1.__str__()


B1= Bicycle("Atlas",BP1)


