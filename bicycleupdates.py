 from collections import OrderedDict
  from operator import itemgetter
 +from enum import Enum
  
 -class Bicycle(object):
 -    def __init__(self,name,BicycleParts):
 -        self.name=name
 -        self.weight=BicycleParts.BicycleWeight
 -        self.cost=BicycleParts.BicycleCost
 -        
 -        
 +
 +#Generic Parent class containing common attributes
 +class Parts(object):
 +    def __init__(self,weight,cost):
 +        self._weight=weight
 +        self._cost=cost
 +
 +
 +class Wheeltypes(Enum):
 +    BMX=(2,20)
 +    Road=(1,20)
 +    Track=(1,25)
 +
 +class Frametypes(Enum):
 +    Aluminium= (110,120)
 +    Carbon = (115,200)
 +    Steel= (112.5,250)
 +    
 +
 +#First part- Wheel        
 +class Wheel(Parts):
 +    def __init__(self,wheeltype=Wheeltypes.BMX):
 +        if isinstance(wheeltype,Wheeltypes):
 +            super().__init__(wheeltype.value[0],wheeltype.value[1])    
 +        else:
 +            raise ValueError("Invalid Wheel type")
 +            
      def __str__(self):
 -        print("Name: {} Weight: {} Price: {}".format(self.name,self.weight,self.cost))
 +        print("Wheel details {} {}".format(self._cost,self._weight))
          
 +#Second Part- Frame
 +class Frame(Parts):
 +    def __init__(self,frametype=Frametypes.Aluminium):
 +        if isinstance(frametype,Frametypes):
 +            super().__init__(frametype.value[0],frametype.value[1])    
 +        else:
 +            raise ValueError("Invalid Frame type")
 +            
 +    def __str__(self):
 +        print("Frame details {} {}".format(self._cost,self._weight))
 +
 +#Happy Customer
  class Customer(object):
      def __init__(self,name,fund):
          self.name=name
          self.fund=fund
          
      def __str__(self):
          print("I am {} and I have {} funds".format(self.name,self.fund))
 -
          
 -class BikeShop(object):
 -  
 -    NetProfit=0;
 -    
 -    def __init__(self,name,Bikes):
 +        
 +#Combination of Wheels and Frames- Logic here to get wheels of the same type   
 +#class BicycleParts(Wheel,Frame):
 +   #def __init__(self,wheeltype,count,frametype):
 +    #   BicycleCost=0
 +     #   F1=Frame(frametype)
 +     #  BicycleCost+=F1._cost
 +     #  BicycleWeight+=F1._weight
 +#    for i in range(0,count):
 + #        W1=Wheel(wheeltype)
 +  #      BicycleCost+=W1._cost
 +   #    BicycleWeight+=W1._weight
 +    #    super().__init__(BicycleWeight,BicycleCost)
 +        
 +#Finished Product
 +class Bicycle(Parts):
 +    def __init__(self,name,Wheels,Frame):
 +        TotalCost=0
 +        TotalWeight=0
 +        TotalCost+=Frame._cost
 +        TotalWeight+=Frame._weight
 +        if isinstance (Wheels,list):
 +            for Wheel in Wheels:
 +                TotalCost+=Wheel._cost
 +                TotalWeight+=Wheel._weight
 +        super().__init__(TotalWeight,TotalCost)
          self.name=name
 -        self.inventory={}
 -       
 -        for Bicycle in Bikes:
 -            self.inventory[Bicycle.name]=0.2*Bicycle.cost+Bicycle.cost
          
          
      def __str__(self):
 +        print("Name: {} Weight: {}lbs Price: ${}".format(self.name,self._weight,self._cost))
 +
 +
 +
 +#Bikeshops selling Bikes---Add NetProfit as an Instance Variable
 +class BikeShop(Bicycle):
 +    self.NetProfit=0
 +    def __init__(self,name,Bikes,margin=0.2):
 +        self.name=name
 +        self.margin=margin
 +        self.inventory={}
 +        for Bicycle in Bikes:
 +            self.inventory[Bicycle.name]=self.margin*Bicycle._cost+Bicycle._cost
 +            
 +    def __str__(self):
          print("Name of the BikeShop: {}".format(self.name))
          print("Inventory List")
          for cycle,sp in self.inventory.items():
              print(cycle,sp)
              
 -  
 +    #To filter out affordable bicycles
      def filterBicycles(self,Customers):
 -        print("Affordable Bicycles")
 +     
          for Customer in Customers:
 +            print("Affordable Bicycles by {}".format(Customer.name))
              for key in self.inventory:
                      if Customer.fund >= self.inventory[key]:
 -                        print("Bicycle {} affordable by {} for amount {}".format(key,Customer.name,self.inventory[key]))
 +                        print(key)
      
 -    
 -    def SellBicyclesMaxProfit(self,Customers):
 +    #Sell Bikes based on First come first served
 +    def SellBicycles(self,Customers):
         for Customer in Customers:
 -            for key,value in sorted(self.inventory.items(),reverse=True):
 +            for key,value in self.inventory.items():
                      if Customer.fund >= value:
                          print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
                          BikeShop.NetProfit=BikeShop.NetProfit+value
                          del self.inventory[key]
                      break    
 -                    
 -    def SellBicycles(self,Customers):
 +                
 +    #Sell Bikes based on the max amount affordable by the customer
 +    def SellBicyclesMaxProfit(self,Customers):
         for Customer in Customers:
 -            for key,value in self.inventory.items():
 +            for key,value in sorted(self.inventory.items(),reverse=True):
                      if Customer.fund >= value:
                          print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
                          BikeShop.NetProfit=BikeShop.NetProfit+value
                          del self.inventory[key]
                      break    
 -    
 -class Parts(object):
 -    def __init__(self,weight,cost):
 -        self.weight=weight
 -        self.cost=cost
 -        
 -class Wheel(Parts):
 -    def __init__(self,modelname,weight=0,cost=0):
 -         self.__modelname=modelname
 -         self.cost=cost
 -         self.weight=cost
 -         
 -    @property
 -    def modelname(self):
 -        return self.__modelname
 -        
 -    @modelname.setter
 -    def modelname(self,modelname):
 -        wheeltype={'bmx':(2,20),'road':(1,20),'track':(2.5,20)}
 -        if(self.__modelname in wheeltype):
 -            super(Wheel,self).__init__(wheeltype[self.modelname][0],wheeltype[self.modelname][1])
 -        
 -            
 -            
 -    def __str__(self):
 -        print("Wheel details {} {}".format(self.cost,self.weight))
 -
 -class Frame(Parts):
 -    def __init__(self,weight,cost,type):
 -        super(Frame,self).__init__(weight,cost)
 -        self.type=type 
 -        
 -    @property   
 -    def type(self):
 -        return self.__type
 -    @type.setter
 -    def type(self,type):
 -        if type.lower() in ["aluminium","carbon","steel"]:
 -            self.__type=type
 -        else:
 -           raise ValueError("Invalid Frame type")
 -            
 -    def __str__(self):
 -        print("Frame details {} {} {}".format(self.weight,self.cost,self.type))
 +                    
     
 -class BicycleParts(object):
 -    BicycleCost=0
 -    BicycleWeight=0
 +class BikeManufacturer(object):
 +    def __init__(self,name,profitpercent):
 +        self.name=name
 +        self.profitpercent=profitpercent
      
 -    def __init__(self,wheels,frame):
 -        BicycleParts.BicycleCost+=frame.cost
 -        BicycleParts.BicycleWeight+=frame.weight
 -        for Wheel in wheels:
 -            BicycleParts.BicycleCost+=Wheel.cost
 -            BicycleParts.BicycleWeight+=Wheel.weight
 -       
 -        
 -        
 -    def __str__(self):
 -        print("Total Cost {} and Total Weight {}".format(BicycleParts.BicycleCost,BicycleParts.BicycleWeight))
 -        
 -F1 = Frame(10,30,"Aluminium")
 -F1.type="CArbon"
 -F1.__str__()
 -#WL=[Wheel(10,10.2,"Aluminium"),Wheel(10,10.2,"Aluminium")]
 -W1=Wheel("road")
 -W1.modelname="road"
 -W1.__str__()
 -#BP1= BicycleParts(WL,F1)
 -#BP1.__str__()
 -
 -
 -#B1= Bicycle("Atlas",BP1)
 -
 -
 +    def buildcycles(self):
 +        BikeList=[Bicycle("Atlas","Road","Carbon"),Bicycle("Neptune","bmx","Aluminium"),Bicycle("Pluto","track","steel")]
 +        return BikeList 
View  
194  bicycles.py
@@ -1,18 +1,31 @@
  from collections import OrderedDict
  from operator import itemgetter
 +from enum import Enum
 +
  
  #Generic Parent class containing common attributes
  class Parts(object):
      def __init__(self,weight,cost):
          self._weight=weight
          self._cost=cost
 -        
 +
 +
 +class Wheeltypes(Enum):
 +    BMX=(2,20)
 +    Road=(1,20)
 +    Track=(1,25)
 +
 +class Frametypes(Enum):
 +    Aluminium= (110,120)
 +    Carbon = (115,200)
 +    Steel= (112.5,250)
 +    
 +
  #First part- Wheel        
  class Wheel(Parts):
 -    def __init__(self,wheeltype):
 -        wheeltypes={'bmx':(2,20),'road':(1,20),'track':(2.5,20)}
 -        if(wheeltype.lower() in wheeltypes):
 -            super().__init__(wheeltypes[wheeltype.lower()][0],wheeltypes[wheeltype.lower()][1])    
 +    def __init__(self,wheeltype=Wheeltypes.BMX):
 +        if isinstance(wheeltype,Wheeltypes):
 +            super().__init__(wheeltype.value[0],wheeltype.value[1])    
          else:
              raise ValueError("Invalid Wheel type")
              
 @@ -21,47 +34,14 @@ def __str__(self):
          
  #Second Part- Frame
  class Frame(Parts):
 -    def __init__(self,Frametype):
 -        Frametypes={'aluminium':(10,120),'carbon':(15,200),'steel':(112.5,250)}
 -        if(Frametype.lower() in Frametypes):
 -            super().__init__(Frametypes[Frametype.lower()][0],Frametypes[Frametype.lower()][1])    
 +    def __init__(self,frametype=Frametypes.Aluminium):
 +        if isinstance(frametype,Frametypes):
 +            super().__init__(frametype.value[0],frametype.value[1])    
          else:
              raise ValueError("Invalid Frame type")
 -     
 -    def __str__(self):
 -        print("Frame details {} {}".format(self._weight,self._cost))
 -        
 -#Combination of Wheels and Frames- Logic here to get wheels of the same type   
 -#class BicycleParts(Wheel,Frame):
 -   #def __init__(self,wheeltype,count,frametype):
 -    #   BicycleCost=0
 -     #   F1=Frame(frametype)
 -     #  BicycleCost+=F1._cost
 -     #  BicycleWeight+=F1._weight
 -#    for i in range(0,count):
 - #        W1=Wheel(wheeltype)
 -  #      BicycleCost+=W1._cost
 -   #    BicycleWeight+=W1._weight
 -    #    super().__init__(BicycleWeight,BicycleCost)
 -        
 -#Finished Product
 -class Bicycle(Parts):
 -    def __init__(self,name,wheeltype,frametype):
 -        BicycleCost=0
 -        BicycleWeight=0
 -        F1=Frame(frametype)
 -        BicycleCost+=F1._cost
 -        BicycleWeight+=F1._weight
 -        for i in range(0,2):
 -            W1=Wheel(wheeltype)
 -            BicycleCost+=W1._cost
 -            BicycleWeight+=W1._weight
 -        super().__init__(BicycleWeight,BicycleCost)
 -        self.name=name
 -        
 -        
 +            
      def __str__(self):
 -        print("Name: {} Weight: {}lbs Price: ${}".format(self.name,self._weight,self._cost))
 +        print("Frame details {} {}".format(self._cost,self._weight))
  
  #Happy Customer
  class Customer(object):
 @@ -71,57 +51,97 @@ def __init__(self,name,fund):
          
      def __str__(self):
          print("I am {} and I have {} funds".format(self.name,self.fund))
 +        
 +class Bicycle(Parts):
 +    def __init__(self,name,Wheels,Frame):
 +        TotalCost=0
 +        TotalWeight=0
 +        TotalCost+=Frame._cost
 +        TotalWeight+=Frame._weight
 +        if isinstance (Wheels,list):
 +            for Wheel in Wheels:
 +                TotalCost+=Wheel._cost
 +                TotalWeight+=Wheel._weight
 +        super().__init__(TotalWeight,TotalCost)
 +        self.name=name
 +        
 +        
 +    def __str__(self):
 +        print("Name: {} Weight: {}lbs Price: ${}".format(self.name,self._weight,self._cost))
 +
  
 -#Bikeshops selling Bikes
  class BikeShop(Bicycle):
 -    NetProfit=0;
 -    def __init__(self,name,Bikes):
 +    
 +    def __init__(self,name,Bikes=[],netprofit=0,margin=0.2):
          self.name=name
 +        self.margin=margin
 +        self.netprofit=netprofit
          self.inventory={}
 -        for Bicycle in Bikes:
 -            self.inventory[Bicycle.name]=0.2*Bicycle._cost+Bicycle._cost
 -            
 +        if isinstance (Bikes,list):
 +            for Bike in Bikes:
 +                    if isinstance(Bike,Bicycle):
 +                        if Bike in self.inventory:
 +                            self.inventory[Bike]+=1
 +                        else:
 +                            self.inventory[Bike]=1
 +                    else:
 +                        raise ValueError("Bikes not passed")
 +        else:
 +                raise ValueError("Bike out of stock")
 +                
      def __str__(self):
          print("Name of the BikeShop: {}".format(self.name))
          print("Inventory List")
 -        for cycle,sp in self.inventory.items():
 -            print(cycle,sp)
 +        print("Name---Count")
 +        for cycle,stock in self.inventory.items():
 +            print(cycle.name,"---",stock)
              
      #To filter out affordable bicycles
 -    def filterBicycles(self,Customers):
 -     
 -        for Customer in Customers:
 -            print("Affordable Bicycles by {}".format(Customer.name))
 -            for key in self.inventory:
 -                    if Customer.fund >= self.inventory[key]:
 -                        print(key)
 -    
 -    #Sell Bikes based on First come first served
 -    def SellBicycles(self,Customers):
 -       for Customer in Customers:
 -            for key,value in self.inventory.items():
 -                    if Customer.fund >= value:
 -                        print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
 -                        BikeShop.NetProfit=BikeShop.NetProfit+value
 -                        del self.inventory[key]
 -                    break    
 -                
 -    #Sell Bikes based on the max amount affordable by the customer
 -    def SellBicyclesMaxProfit(self,Customers):
 -       for Customer in Customers:
 -            for key,value in sorted(self.inventory.items(),reverse=True):
 -                    if Customer.fund >= value:
 -                        print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
 -                        BikeShop.NetProfit=BikeShop.NetProfit+value
 -                        del self.inventory[key]
 -                    break    
 -                    
 -   
 -class BikeManufacturer(object):
 -    def __init__(self,name,profitpercent):
 -        self.name=name
 -        self.profitpercent=profitpercent
 +    def searchBikes(self,Customers=[]):
 +        
 +        if isinstance(Customers,list):
 +            for customer in Customers:
 +                if isinstance(customer,Customer):
 +                    print("Affordable bikes by customer: {}".format(customer.name))
 +                    for bike in self.inventory:
 +                        if self.inventory[bike]>0:
 +                            if bike._cost * self.margin + bike._cost <= customer.fund:
 +                                print(bike.name,bike._cost)
 +                        else:
 +                            print("Out of stock")
 +                else:
 +                    raise ValueError("Inventory list only shown to Customers")
 +               
 +        
 +        
      
 -    def buildcycles(self):
 -        BikeList=[Bicycle("Atlas","Road","Carbon"),Bicycle("Neptune","bmx","Aluminium"),Bicycle("Pluto","track","steel")]
 -        return BikeList 
 +    def SellBicycles(self,Customers=[]):
 +         if isinstance(Customers,list):
 +             for customer in Customers:
 +                  if isinstance(customer,Customer):
 +                    for bike in self.inventory:
 +                        if customer.fund >= bike._cost and self.inventory[bike]>0:
 +                            print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(customer.name,bike.name,bike._cost,customer.fund-bike._cost))
 +                            self.netprofit=self.netprofit+bike._cost
 +                            if self.inventory[bike] <= 1: 
 +                                del self.inventory[bike]
 +                            else:
 +                                self.inventory[bike]-=1
 +                            break    
 +
 +W1=Wheel(Wheeltypes.Road)
 +W2=Wheel(Wheeltypes.Road)
 +F1=Frame()
 +F2=Frame(Frametypes.Carbon)
 +WL=[W1,W2]
 +B1=Bicycle("Atlas",WL,F1)
 +B2=Bicycle("Venus",WL,F1)
 +B3=Bicycle("Atlas",WL,F2)
 +BS1=BikeShop("Monrovia",[B1,B2,B2,B3,B3,B3,B3])
 +BS1.__str__()
 +Customers=[Customer("Vigs",1000),Customer("Alex",400),Customer("James",500)]
 +BS1.searchBikes(Customers)
 +BS1.SellBicycles(Customers)
 +print("Net Profit afer Sale {}".format(BS1.netprofit))
 +print("Remaining inventory")
 +BS1.__str__() 
View  
214  function.py
@@ -1,122 +1,152 @@
  from collections import OrderedDict
  from operator import itemgetter
 +from enum import Enum
  
 +
 +#Generic Parent class containing common attributes
  class Parts(object):
      def __init__(self,weight,cost):
          self._weight=weight
          self._cost=cost
  
  
 -class Bicycle(Parts):
 -    def __init__(self,name,BicycleParts):
 -        super().__init__(BicycleParts.BicycleWeight,BicycleParts.BicycleCost)
 -        self.name=name
 -        self.__str__()
 -        
 -        
 +class Wheeltypes(Enum):
 +    BMX=(2,20)
 +    Road=(1,20)
 +    Track=(1,25)
 +
 +class Frametypes(Enum):
 +    Aluminium= (110,120)
 +    Carbon = (115,200)
 +    Steel= (112.5,250)
 +    
 +
 +#First part- Wheel        
 +class Wheel(Parts):
 +    def __init__(self,wheeltype=Wheeltypes.BMX):
 +        if isinstance(wheeltype,Wheeltypes):
 +            super().__init__(wheeltype.value[0],wheeltype.value[1])    
 +        else:
 +            raise ValueError("Invalid Wheel type")
 +            
      def __str__(self):
 -        print("Name: {} Weight: {}lbs Price: ${}".format(self.name,self._weight,self._cost))
 +        print("Wheel details {} {}".format(self._cost,self._weight))
          
 +#Second Part- Frame
 +class Frame(Parts):
 +    def __init__(self,frametype=Frametypes.Aluminium):
 +        if isinstance(frametype,Frametypes):
 +            super().__init__(frametype.value[0],frametype.value[1])    
 +        else:
 +            raise ValueError("Invalid Frame type")
 +            
 +    def __str__(self):
 +        print("Frame details {} {}".format(self._cost,self._weight))
 +
 +#Happy Customer
  class Customer(object):
      def __init__(self,name,fund):
          self.name=name
          self.fund=fund
          
      def __str__(self):
          print("I am {} and I have {} funds".format(self.name,self.fund))
 +        
 +class Bicycle(Parts):
 +    def __init__(self,name,Wheels,Frame):
 +        TotalCost=0
 +        TotalWeight=0
 +        TotalCost+=Frame._cost
 +        TotalWeight+=Frame._weight
 +        if isinstance (Wheels,list):
 +            for Wheel in Wheels:
 +                TotalCost+=Wheel._cost
 +                TotalWeight+=Wheel._weight
 +        super().__init__(TotalWeight,TotalCost)
 +        self.name=name
 +        
 +        
 +    def __str__(self):
 +        print("Name: {} Weight: {}lbs Price: ${}".format(self.name,self._weight,self._cost))
 +
  
 -class BikeShop(object):
 -  
 -    NetProfit=0;
 +class BikeShop(Bicycle):
      
 -    def __init__(self,name,Bikes):
 +    def __init__(self,name,Bikes=[],netprofit=0,margin=0.2):
          self.name=name
 +        self.margin=margin
 +        self.netprofit=netprofit
          self.inventory={}
 -       
 -        for Bicycle in Bikes:
 -            self.inventory[Bicycle.name]=0.2*Bicycle.cost+Bicycle.cost
 -        
 -        
 +        if isinstance (Bikes,list):
 +            for Bike in Bikes:
 +                    if isinstance(Bike,Bicycle):
 +                        if Bike in self.inventory:
 +                            self.inventory[Bike]+=1
 +                        else:
 +                            self.inventory[Bike]=1
 +                    else:
 +                        raise ValueError("Bikes not passed")
 +        else:
 +                raise ValueError("Bike out of stock")
 +                
      def __str__(self):
          print("Name of the BikeShop: {}".format(self.name))
          print("Inventory List")
 -        for cycle,sp in self.inventory.items():
 -            print(cycle,sp)
 +        print("Name---Count")
 +        for cycle,stock in self.inventory.items():
 +            print(cycle.name,"---",stock)
              
 -  
 -    def filterBicycles(self,Customers):
 -        print("Affordable Bicycles")
 -        for Customer in Customers:
 -            for key in self.inventory:
 -                    if Customer.fund >= self.inventory[key]:
 -                        print("Bicycle {} affordable by {} for amount {}".format(key,Customer.name,self.inventory[key]))
 -    
 -    
 -    def SellBicyclesMaxProfit(self,Customers):
 -       for Customer in Customers:
 -            for key,value in sorted(self.inventory.items(),reverse=True):
 -                    if Customer.fund >= value:
 -                        print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
 -                        BikeShop.NetProfit=BikeShop.NetProfit+value
 -                        del self.inventory[key]
 -                    break    
 -                    
 -    def SellBicycles(self,Customers):
 -       for Customer in Customers:
 -            for key,value in self.inventory.items():
 -                    if Customer.fund >= value:
 -                        print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(Customer.name,key,value,Customer.fund-value))
 -                        BikeShop.NetProfit=BikeShop.NetProfit+value
 -                        del self.inventory[key]
 -                    break    
 -    
 -
 +    #To filter out affordable bicycles
 +    def searchBikes(self,Customers=[]):
          
 -class Wheel(Parts):
 -    def __init__(self,wheeltype):
 -        wheeltypes={'bmx':(2,20),'road':(1,20),'track':(2.5,20)}
 -        if(wheeltype.lower() in wheeltypes):
 -            super().__init__(wheeltypes[wheeltype.lower()][0],wheeltypes[wheeltype.lower()][1])    
 -        else:
 -            raise ValueError("Invalid Wheel type")
 -            
 -    def __str__(self):
 -        print("Wheel details {} {}".format(self._cost,self._weight))
 -
 -class Frame(Parts):
 -    def __init__(self,Frametype):
 -        Frametypes={'aluminium':(10,120),'carbon':(15,200),'steel':(112.5,250)}
 -        if(Frametype.lower() in Frametypes):
 -            super().__init__(Frametypes[Frametype.lower()][0],Frametypes[Frametype.lower()][1])    
 -        else:
 -            raise ValueError("Invalid Frame type")
 -     
 -    def __str__(self):
 -        print("Frame details {} {}".format(self._weight,self._cost))
 -   
 -class BicycleParts(Wheel,Frame):
 -    BicycleCost=0
 -    BicycleWeight=0
 -    
 -    def __init__(self,wheeltype,count,frame):
 -        BicycleParts.BicycleCost+=frame._cost
 -        BicycleParts.BicycleWeight+=frame._weight
 -        for i in range(0,count):
 -            W1=Wheel(wheeltype)
 -            BicycleParts.BicycleCost+=W1._cost
 -            BicycleParts.BicycleWeight+=W1._weight
 -       
 -    def __str__(self):
 -        print("Total Cost $ {}  and Total Weight {} lbs".format(BicycleParts.BicycleCost,BicycleParts.BicycleWeight))
 +        if isinstance(Customers,list):
 +            for customer in Customers:
 +                if isinstance(customer,Customer):
 +                    print("Affordable bikes by customer: {}".format(customer.name))
 +                    for bike in self.inventory:
 +                        if self.inventory[bike]>0:
 +                            if bike._cost * self.margin + bike._cost <= customer.fund:
 +                                print(bike.name,bike._cost)
 +                        else:
 +                            print("Out of stock")
 +                else:
 +                    raise ValueError("Inventory list only shown to Customers")
 +               
          
 +        
 +    #Sell Bikes based on First come first served
 +    def SellBicycles(self,Customers=[]):
 +         if isinstance(Customers,list):
 +             for customer in Customers:
 +                  if isinstance(customer,Customer):
 +                    for bike in self.inventory:
 +                        if customer.fund >= bike._cost and self.inventory[bike]>0:
 +                            print("{} bought Bicycle {} for the amount {}. Remaining Funds {}".format(customer.name,bike.name,bike._cost,customer.fund-bike._cost))
 +                            self.netprofit=self.netprofit+bike._cost
 +                            if self.inventory[bike] <= 1: 
 +                                del self.inventory[bike]
 +                            else:
 +                                self.inventory[bike]-=1
 +                            break    
  
 -WL=[Wheel("road"),Wheel("road")]
 -W1=Wheel("road")
 -F1=Frame("Carbon")
 -BP1= BicycleParts("road",2,F1)
 -BP1.__str__()
 -
 -
 -B1= Bicycle("Atlas",BP1)
 -
 +W1=Wheel(Wheeltypes.Road)
 +W2=Wheel(Wheeltypes.Road)
 +F1=Frame()
 +F2=Frame(Frametypes.Carbon)
 +WL=[W1,W2]
 +B1=Bicycle("Atlas",WL,F1)
 +B2=Bicycle("Venus",WL,F1)
 +B3=Bicycle("Atlas",WL,F2)
 +B1.__str__()
 +B2.__str__()
 +B3.__str__()
  
 +W1.__str__()
 +BS1=BikeShop("Monrovia",[B1,B2,B2,B3,B3,B3,B3])
 +BS1.__str__()
 +Customers=[Customer("Vigs",1000),Customer("Alex",400),Customer("James",500)]
 +BS1.searchBikes(Customers)
 +BS1.SellBicycles(Customers)
 +print("Net Profit afer Sale {}".format(BS1.netprofit))
 +print("Remaining inventory")
 +BS1.__str__() 
