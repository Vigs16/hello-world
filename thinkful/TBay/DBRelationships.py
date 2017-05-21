from sqlalchemy import Column, Integer, String, Date, ForeignKey,create_engine
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine=create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()


class Manufacturer(Base):
    __tablename__="manufacturer"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    guitars=relationship("Guitar",backref="manufacturer")


class Guitar(Base):
    __tablename__="guitar"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    manufacturer_id=Column(Integer,ForeignKey('manufacturer.id'),nullable=False)
    
class Pizza(Base):
    __tablename__="pizza"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    toppings=relationship("Topping", secondary="pizzatoppingtable",backref="pizzas")

class Topping(Base):
    __tablename__="topping"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    
    
class PizzaToppingTable(Base):
    __tablename__="pizzatoppingtable"
    
    pizza_id= Column(Integer,ForeignKey('pizza.id'),primary_key=True)
    topping_id=Column(Integer,ForeignKey('topping.id'),primary_key=True)
    
    
peppers = Topping(name="Peppers")
garlic = Topping(name="Garlic")
chilli = Topping(name="Chilli")

spicy_pepper = Pizza(name="Spicy Pepper")
spicy_pepper.toppings = [peppers, chilli]

vampire_weekend = Pizza(name="Vampire Weekend")
vampire_weekend.toppings = [garlic, chilli]


session.add_all([garlic, peppers, chilli, spicy_pepper, vampire_weekend])
session.commit()

for topping in vampire_weekend.toppings:
    print(topping.name)

for pizza in chilli.pizzas:
    print(pizza.name)
    
    
    
    
