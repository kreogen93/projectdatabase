from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Float, insert
from database import engine, SessionLocal
from models import PlaceOfKeeping, TypeOfPrices, Items
from random import randint


class MainCompany():
    def CreateSuperMarket(self, number_supermarket):
        metadata = MetaData()
        Warehouse = Table(f'Warehouse {number_supermarket}', metadata,
                          Column('id', Integer(), primary_key=True),
                          Column('count', Integer()))
        #Здесь нужно добавить сотрудников,поставщиков и тд

        metadata.create_all(engine)