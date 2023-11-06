from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table


class Place(base):
    __tablename__ = "Place"
    id = Column(Integer, primary_key=True)
    place_name = Column(String)
    country_name = Column(String)
    capital_city = Column(String)
    official_language = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Progammer table
lisbon = Place(
    place_name="Lisbon",
    country_name="Portugal",
    capital_city="Lisbon",
    official_language="Portuguese"
)

brighton = Place(
    place_name="Brighton",
    country_name="UK",
    capital_city="London",
    official_language="English"
)

taormina = Place(
    place_name="Taormina",
    country_name="Italy",
    capital_city="Rome",
    official_language="Italian"
)

# add each instance of our programmers to our session
# session.add(lisbon)
# session.add(brighton)
# session.add(taormina)

# updating a single record
# place = session.query(Place).filter_by(id=3).first()
# place.country_name = "World"


# commit our session to the database
# session.commit()

# updating multiple records
# locations = session.query(Place)
# for location in locations:
#     if location.official_language == "Italian":
#         location.official_language = "IT"
#     elif location.official_language == "English":
#         location.official_language = "EN"
#     elif location.official_language == "Portuguese":
#         location.official_language = "PT"
#     else:
#         print("Language not defined")
#     session.commit()

# deleting a single record
# pname = input("Enter a place name: ")
# cname = input("Enter a country name: ")
# place = session.query(Place).filter_by(place_name=pname, country_name=cname).first()
# defensive programming
# if place is not None:
#     print("Place Found: ", place.place_name + " " + place.country_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(place)
#         session.commit()
#         print("Place has been deleted")
#     else:
#         print("Place not deleted")
# else:
#     print("No records found")

# delete multiple/all records
# places = session.query(Place)
# for place in places:
#     session.delete(place)
#     session.commit()

# query the database to find all Programmers
places = session.query(Place)
for place in places:
    print(
        place.id,
        place.place_name + ", " + place.country_name,
        "Capital: " + place.capital_city,
        place.official_language + " language",
        sep=" | "
    )
