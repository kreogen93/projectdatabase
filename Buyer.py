from database import engine, SessionLocal
from models import ShopHall0, ShopHall1
from random import randint


class Buyer():
    def __init__(self, num):
        self.num = num
    def buy(self):
        session = SessionLocal()
        for i in range(randint(1, 10)):
            tovar = randint(1, 199)
            if self.num == 0:
                count = session.query(ShopHall0.count).filter(ShopHall0.item_id == tovar).all()[0][0]
                session.query(ShopHall0).filter(ShopHall0.item_id == tovar). \
                    update({ShopHall0.count: count - randint(0, count)}, synchronize_session=False)
            else:
                count = session.query(ShopHall1.count).filter(ShopHall0.item_id == tovar).all()[0][0]
                session.query(ShopHall1).filter(ShopHall0.item_id == tovar). \
                    update({ShopHall1.count: count - randint(0, count)}, synchronize_session=False)
        session.commit()

