from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Float, insert
from database import engine, SessionLocal
from models import PlaceOfKeeping, TypeOfPrices, Items, WareHouse
from random import randint


class MainCompany():
    def CreateSuperMarket(self, number_supermarket):
        metadata = MetaData()
        warehouse = Table(f'Warehouse {number_supermarket}', metadata,
                          Column('item_id', Integer(), primary_key=True),
                          Column('count', Integer()))
        #Здесь нужно добавить сотрудников,поставщиков и тд

        metadata.create_all(engine)
        session = SessionLocal()
        for i in range(200):
            query = insert(WareHouse).values(
                item_id=i,
                count=randint(1, 30)
            )
            session.execute(query)
        session.commit()
