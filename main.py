from bicycles import Frame,Customer,Bicycle,BikeShop


Customers=[Customer("Vigs",1000),Customer("Alex",400),Customer("James",500)]


Bikes=[Bicycle("Atlas","Road","Carbon"),Bicycle("Neptune","bmx","Aluminium"),Bicycle("Pluto","track","steel"),Bicycle("Mars","road","carbon"),Bicycle("Earth","bmx","steel"),Bicycle("Venus","track","Aluminium")]

BS1=BikeShop("Mountaineers",Bikes)

print("Initial Inventory")
BS1.__str__()
print("-----------------")
BS1.filterBicycles(Customers)
BS1.SellBicycles(Customers)
print("-----------------")
print("After Sale, Inventory")
BS1.__str__()
print("Profit after selling three bikes {}".format(BS1.NetProfit))


        
