from sqlalchemy import insert
from database import engine, SessionLocal
from models import ShopHall0, ShopHall1, WareHouse0, WareHouse1, StopList1, StopList0
from random import randint


class Itemmanager():
    def __init__(self, num):
        self.num = num
    def check(self):
        session = SessionLocal()
        for i in range(1, 200):
            if self.num == 0:
                count = session.query(ShopHall0.count).filter(ShopHall0.item_id == i).all()[0][0]
                if count <= 1:
                    countware = session.query(WareHouse0.count).filter(WareHouse0.item_id == i).all()[0][0]
                    if countware == 0:
                        query = insert(StopList0).values(
                            item_id=i,
                            cause='end'
                        )
                        session.execute(query)
                    else:
                        c = randint(1, countware)
                        session.query(ShopHall0).filter(ShopHall0.item_id == i).update({ShopHall0.count: ShopHall0.count + c})
                        session.query(WareHouse0).filter(WareHouse0.item_id == i).update(
                            {WareHouse0.count: WareHouse0.count - c})
            else:
                count = session.query(ShopHall1.count).filter(ShopHall1.item_id == i).all()[0][0]
                if count <= 1:
                    countware = session.query(WareHouse1.count).filter(WareHouse1.item_id == i).all()[0][0]
                    if countware == 0:
                        query = insert(StopList1).values(
                            item_id=i,
                            cause='end'
                        )
                        session.execute(query)
                    else:
                        c = randint(1, countware)
                        session.query(ShopHall1).filter(ShopHall1.item_id == i).update(
                            {ShopHall1.count: ShopHall1.count + c})
                        session.query(WareHouse1).filter(WareHouse1.item_id == i).update(
                            {WareHouse1.count: WareHouse1.count - c})
        session.commit()