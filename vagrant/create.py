from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurant_menu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
MyFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(MyFirstRestaurant)
session.commit()
print(session.query(Restaurant).all())