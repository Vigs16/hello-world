from tbay import User,Item,Bid,session

from DBRelationships import Manufacturer,Guitar

#Vigs=User(usrname="Vigs",usrpwd="1234")    
#Teejay=User(usrname="TJ",usrpwd="12345")

#Item1=Item(name="Gloves",description="Powerlifting")
#Item2=Item(name="QuestBars",description="Protein Bars")


#session.add(Vigs)
#session.add(Teejay)

#session.add(Item1)
#session.add(Item2)
#session.commit()
#Userlist=session.query(User).filter(User.usrname=="Vigs").all()
#for user in Userlist:
 #   session.delete(user)
#session.commit()

#Userlist=session.query(User).filter(User.usrname=="TJ").all()
#for user in Userlist:
 #   session.delete(user)
#session.commit()

fender = Manufacturer(name="Fender")
strat = Guitar(name="Stratocaster", manufacturer=fender)
tele = Guitar(name="Telecaster")
fender.guitars.append(tele)

session.add_all([fender, strat, tele])
session.commit()


for guitar in fender.guitars:
    print(guitar.name)
print(tele.manufacturer.name)