from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Float, insert
from database import engine, SessionLocal
from random import randint
import pandas as pd


class MainCompany():
    def CreateSuperMarket(self, number_supermarket):
        metadata = MetaData()
        warehouse = Table(f'Warehouse {number_supermarket}', metadata,
                          Column('item_id', Integer(), primary_key=True),
                          Column('count', Integer()))


        stop_list = Table(f'StopList {number_supermarket}', metadata,
                          Column('item_id', Integer(), primary_key=True),
                          Column('cause', String()))


        shop_hall = Table(f'ShopHall {number_supermarket}', metadata,
                          Column('item_id', Integer(), primary_key=True),
                          Column('count', Integer()))
        #Здесь нужно добавить сотрудников,поставщиков и тд

        metadata.create_all(engine)
        session = SessionLocal()
        for i in range(200):
            count = randint(1, 30)
            query = insert(warehouse).values(
                count=count
            )
            session.execute(query)
            query = insert(shop_hall).values(
                count=count - randint(1, count)
            )
            session.execute(query)
        session.commit()


    def createexcel(self):
        markup = dict()
        for i in range(randint(0, 200)):
            markup[randint(0, 200)] = randint(1, 30)
        return markup
        #markup = pd.DataFrame(markup)
        #markup.to_excel('Markup.xlsx')
