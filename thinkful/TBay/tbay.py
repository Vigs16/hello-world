from sqlalchemy import create_engine,Column, Integer, String, DateTime, Float,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "tUser"
    id = Column(Integer,primary_key=True)
    usrname= Column(String, nullable=False)
    usrpwd= Column(String, nullable=False)
    auction_items=relationship("Item",backref="user",secondary="userbid")
        
class Item(Base):
    __tablename__ = "item"
    id = Column(Integer,primary_key=True)
    name= Column(String, nullable=False)
    description=Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    auction_uid=Column(Integer,ForeignKey('tUser.id'),nullable=False)
    
    
class UserBid(Base):
    __tablename__="userbid"
    user_id=Column(Integer,ForeignKey('tUser.id'),primary_key=True)
    item_id=Column(Integer,ForeignKey('item.id'),primary_key=True)
    price= Column(Float, nullable=False)

    

Base.metadata.create_all(engine)
    
#Vigs=User(usrname='Vigs',usrpwd='123')
#Darcy=User(usrname='Darcy',usrpwd='123')
#TJ=User(usrname='TJ',usrpwd='123')

#session.add_all([Vigs,Darcy,TJ])
#session.commit()

#Item1=Item(name='BaseBall',description='PlayItem',auction_uid=session.query(User.id).filter(User.usrname=="Vigs").first())
#session.add(Item1)
#session.commit()

#Item2=Item(name='BaseBallCap',description='Apparel',auction_uid=session.query(User.id).filter(User.usrname=="Vigs").first())
#session.add(Item2)
#session.commit()


#UB1= UserBid(user_id=session.query(User.id).filter(User.usrname=="Darcy").first(),item_id=session.query(Item.id).filter(Item.name=="BaseBall").first(),price=10.00)
#UB2= UserBid(user_id=session.query(User.id).filter(User.usrname=="TJ").first(),item_id=session.query(Item.id).filter(Item.name=="BaseBall").first(),price=12.00)
#UB3= UserBid(user_id=session.query(User.id).filter(User.usrname=="TJ").first(),item_id=session.query(Item.id).filter(Item.name=="BaseBallCap").first(),price=12.00)
#session.add(UB3)
#session.commit()

#print("Items auctioned by Vigs")
#for item in Vigs.auction_items:
 #   print(item.name)
    
#print("Details of Auctioned users")
#Itemlist= session.query(Item).all()
#for item in Itemlist:
 #  print("Item: {}, AuctionedUser: {}".format(item.name,item.user.usrname))
    
    
print("MaxBid for BaseBall Item done by")
qry=session.query(func.max(UserBid.price).label("MaxBid"))
for res in qry.filter(UserBid.item_id==session.query(Item.id).filter(Item.name=="Baseball")).all():
    print(res)
#)




    