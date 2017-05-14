from collections import OrderedDict
from operator import itemgetter

class Bicycle(object):
    def __init__(self,name,BicycleParts):
        self.name=name
        self.weight=BicycleParts.BicycleWeight
        self.cost=BicycleParts.BicycleCost
        
        
    def __str__(self):
        print("Name: {} Weight: {} Price: {}".format(self.name,self.weight,self.cost))
        
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
    
class Parts(object):
    def __init__(self,weight,cost):
        self.weight=weight
        self.cost=cost
        
class Wheel(Parts):
    def __init__(self,modelname,weight=0,cost=0):
         self.__modelname=modelname
         self.cost=cost
         self.weight=cost
         
    @property
    def modelname(self):
        return self.__modelname
        
    @modelname.setter
    def modelname(self,modelname):
        wheeltype={'bmx':(2,20),'road':(1,20),'track':(2.5,20)}
        if(self.__modelname in wheeltype):
            super(Wheel,self).__init__(wheeltype[self.modelname][0],wheeltype[self.modelname][1])
        
            
            
    def __str__(self):
        print("Wheel details {} {}".format(self.cost,self.weight))

class Frame(Parts):
    def __init__(self,weight,cost,type):
        super(Frame,self).__init__(weight,cost)
        self.type=type 
        
    @property   
    def type(self):
        return self.__type
    @type.setter
    def type(self,type):
        if type.lower() in ["aluminium","carbon","steel"]:
            self.__type=type
        else:
           raise ValueError("Invalid Frame type")
            
    def __str__(self):
        print("Frame details {} {} {}".format(self.weight,self.cost,self.type))
   
class BicycleParts(object):
    BicycleCost=0
    BicycleWeight=0
    
    def __init__(self,wheels,frame):
        BicycleParts.BicycleCost+=frame.cost
        BicycleParts.BicycleWeight+=frame.weight
        for Wheel in wheels:
            BicycleParts.BicycleCost+=Wheel.cost
            BicycleParts.BicycleWeight+=Wheel.weight
       
        
        
    def __str__(self):
        print("Total Cost {} and Total Weight {}".format(BicycleParts.BicycleCost,BicycleParts.BicycleWeight))
        
F1 = Frame(10,30,"Aluminium")
F1.type="CArbon"
F1.__str__()
#WL=[Wheel(10,10.2,"Aluminium"),Wheel(10,10.2,"Aluminium")]
W1=Wheel("road")
W1.modelname="road"
W1.__str__()
#BP1= BicycleParts(WL,F1)
#BP1.__str__()


#B1= Bicycle("Atlas",BP1)


