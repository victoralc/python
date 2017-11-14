from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


def save(restaurant):
    session.add(restaurant)
    session.commit()
    session.close()


def find_all():
    restaurants = session.query(Restaurant).all()
    return restaurants

def find_first_restaurant():
    first = session.query(Restaurant).first()
    session.close()
    return first


def find_by(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    session.close()
    return restaurant


def delete(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    session.delete(restaurant)
    session.commit()
    session.close()

def find_menu_items_by_restaurant_id(id):
    items = session.query(MenuItem).filter_by(restaurant_id = id)
    return items

def find_menu_item_by_id(menuitem_id):
    item = session.query(MenuItem).filter_by(id = menuitem_id).one()
    session.close()
    return item

def saveMenuItem(menuItem):
    session.add(menuItem)
    session.commit()
    session.close()

def deleteItem(menuItem):
    session.delete(menuItem)
    session.commit()
    session.close()