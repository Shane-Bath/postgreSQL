from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()


class Clients(base):
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(Integer)
    email_address = Column(String)


Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)


# client_one = Clients(
#     first_name="Shane",
#     last_name="Bath",
#     phone_number=86339933,
#     email_address="s.bath@gmail.com"
# )


# session.add(client_one)


# session.commit()

# add a new record with user inputs
fname = input("Enter first name: ")
lname = input("Enter last name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

new_record = Clients(first_name=fname, last_name=lname,
                     phone_number=phone, email_address=email)

session.add(new_record)
session.commit()

clients = session.query(Clients)
for client in clients:
    print(
        client.id,
        client.first_name + " " + client.last_name,
        client.phone_number,
        client.email_address,
        sep=" | "
    )
