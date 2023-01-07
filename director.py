from sqlalchemy import insert, and_
from database import SessionLocal
from models import Items, PriceList, WareHouse0, WareHouse1, StopList0, StopList1


class Director():
    def __init__(self, number_supermarket):
        self.number_supermarket = number_supermarket
        self.dangerouslist = range(10, 100)
        self.badlist = range(150, 170)
        self.badmap = dict()
        for i in range(150, 170):
            self.badmap[i] = 0


    def UpdatePrice(self):
        session = SessionLocal()
        for i in range(200):
            if len(list(session.query(PriceList).filter(and_(PriceList.item_id == i, PriceList.place_keeping_id == self.number_supermarket)))) == 0:
                query = insert(PriceList).values(
                    id = int(str(i)+str(self.number_supermarket)),
                    item_id=i,
                    type_price_id=1,
                    place_keeping_id=self.number_supermarket,
                    price=session.query(Items.inner_price).filter(Items.id == i)[0][0] * 1.05
                 )
                session.execute(query)
                session.commit()
            else:
                query = session.query(PriceList.price, PriceList.type_price_id, PriceList.place_keeping_id)\
                    .filter(PriceList.item_id == i).all()
                m = query[0][0]
                for j in query:
                    if m < j[0]:
                        m = j[0]
                session.query(PriceList).filter(and_(PriceList.id == i, PriceList.place_keeping_id == self.number_supermarket)).\
                update({PriceList.price: m}, synchronize_session=False)
                session.commit()
            days = session.query(Items.date_of_end).filter(Items.id == i).all()[0][0]
            if self.number_supermarket == 0:
                count = session.query(WareHouse0.count).filter(WareHouse0.item_id == i + 1).all()[0][0]
            else:
                count = session.query(WareHouse1.count).filter(WareHouse1.item_id == i + 1).all()[0][0]
            print(days)
            if days < 5 and days > 3 and count <= 10:
                session.query(PriceList).filter(
                    and_(PriceList.id == i, PriceList.place_keeping_id == self.number_supermarket)). \
                    update({PriceList.price: (PriceList.price * 0.95), PriceList.type_price_id : 2}, synchronize_session=False)
                session.commit()
            if days <= 3 and count <= 4:
                session.query(PriceList).filter(
                    and_(PriceList.id == i, PriceList.place_keeping_id == self.number_supermarket)). \
                    update({PriceList.price: (PriceList.price * 0.5), PriceList.type_price_id: 3},
                           synchronize_session=False)
                session.commit()
    def gkmarkup(self, markup):
        session = SessionLocal()
        for i in markup:
            if (markup[i] > 15 and i in self.dangerouslist):
                if self.number_supermarket == 0:
                    query = insert(StopList0).values(
                        item_id = i,
                        cause='big markup'
                    )
                    session.execute(query)
                else:
                    query = insert(StopList1).values(
                        item_id=i,
                        cause='big markup'
                    )
                    session.execute(query)
            elif markup[i] > 5 and i in self.badlist:
                if markup[i] // 5 > 1:
                    self.badmap[i] += markup[i]


            else:
                session.query(PriceList).filter(
                    and_(PriceList.id == i, PriceList.place_keeping_id == self.number_supermarket)). \
                    update({PriceList.price: ((PriceList.price * float(1 + markup[i] / 100)))},
                           synchronize_session=False)
            session.commit()
    def updateday(self):
        session = SessionLocal()
        for i in self.badmap:
            if self.badmap[i] > 5:
                self.badmap[i] -= 5
            else:
                self.badmap[i] = 0
        session.query(PriceList).filter(
            and_(PriceList.id == i, PriceList.place_keeping_id == self.number_supermarket)). \
            update({PriceList.price: ((PriceList.price * float(1 + 5 / 100)))},
                   synchronize_session=False)
        session.commit()


