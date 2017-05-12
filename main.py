import bicycles


Customers=[bicycles.Customer("Vigs",1000),bicycles.Customer("Alex",200),bicycles.Customer("James",500)]


Bikes=[bicycles.Bicycle("Atlas","50lbs",1050),bicycles.Bicycle("Neptune","50lbs",110), bicycles.Bicycle("Pluto","50lbs",150),bicycles.Bicycle("Mars","50lbs",400),bicycles.Bicycle("Earth","40lbs",1510),bicycles.Bicycle("Venus","60lbs",500)]

BS1= bicycles.BikeShop("Mountaineers",Bikes)

print("Initial Inventory")
BS1.displayBikeShop()
print("-----------------")
BS1.filterBicycles(Customers)
BS1.SellBicycles(Customers)
print("-----------------")
print("After Sale, Inventory")
BS1.displayBikeShop()
print("Profit after selling three bikes {}".format(BS1.NetProfit))
