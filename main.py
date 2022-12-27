from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Float, insert
from database import engine, SessionLocal
from models import PlaceOfKeeping, TypeOfPrices, Items
from random import randint

def CreateTables():
    metadata = MetaData()


    PlaceOfKeeping = Table('PlaceOfKeeping', metadata,
                           Column('id', Integer(), primary_key=True),
                           Column('name', String()))
    Items = Table('Items', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('name', String()),
                  Column('name_of_company', String()),
                  Column('country_of_company', String()),
                  Column('id_company', Integer(), primary_key=True),
                  Column('date_of_end', Integer()),
                  Column('inner_price', Float()))
    TypeOfPrices = Table('TypeOfPrices', metadata,
                         Column('id', Integer(), primary_key=True),
                         Column('name', String()))
    PriceList = Table('PriceList', metadata,
                      Column('id', Integer(), primary_key=True),
                      Column('item_id', ForeignKey("Items.id"), primary_key=True),
                      Column('type_price_id', ForeignKey("TypeOfPrices.id"), primary_key=True),
                      Column('price', Float()))


    metadata.create_all(engine)
def InnerTypes():
    session = SessionLocal()
    query = insert(TypeOfPrices).values(
        name='regular'
    )
    session.execute(query)
    query = insert(TypeOfPrices).values(
        name='markdown'
    )
    session.execute(query)
    query = insert(TypeOfPrices).values(
        name='action'
    )
    session.execute(query)
    session.commit()


def InnerPlaces():
    session = SessionLocal()
    for i in range(20):
        query = insert(PlaceOfKeeping).values(
            name='supermarket ' + str(i)
        )
        session.execute(query)
    session.commit()


def InnerItems():
    session = SessionLocal()
    for i in range(200):
        rand = randint(1, 50)
        query = insert(Items).values(
            id = i,
            name='item ' + str(i),
            name_of_company='company ' + str(rand),
            country_of_company='country ' + str(randint(1, 50)),
            id_company = rand,
            date_of_end=randint(1, 100),
            inner_price=randint(100, 2000) / 2
        )
        session.execute(query)
    session.commit()

