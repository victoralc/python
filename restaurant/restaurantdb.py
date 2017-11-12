from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)


def save(restaurant):
    session = DBSession()
    session.add(restaurant)
    session.commit()
    session.close()


def find_all():
    session = DBSession()
    restaurants = session.query(Restaurant).all()
    return restaurants


def find_by(restaurant_id):
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    session.close()
    return restaurant


def delete(restaurant_id):
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    session.delete(restaurant)
    session.commit()
    session.close()

