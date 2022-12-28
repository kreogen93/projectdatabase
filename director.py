from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Float, insert, and_
from database import engine, SessionLocal
from models import PlaceOfKeeping, TypeOfPrices, Items, PriceList


class Director():
    def __init__(self, number_supermarket):
        self.number_supermarket = number_supermarket


    def UpdatePrice(self):
        session = SessionLocal()
        for i in range(200):
            if len(list(session.query(PriceList).filter(PriceList.item_id == i))) == 0:
                query = insert(PriceList).values(
                    id = i,
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
                for i in query:
                    if m < i[0]:
                        m = i[0]
                session.query(PriceList).filter(and_(PriceList.id == i, PriceList.place_keeping_id == self.number_supermarket)).\
                update({PriceList.price: m}, synchronize_session=False)
                session.commit()
            days = session.query(Items.date_of_end).filter(Items.id == i).all()[0][0]
            if days < 5 and days > 3:
                session.query(PriceList).filter(
                    and_(PriceList.id == i, PriceList.place_keeping_id == self.number_supermarket)). \
                    update({PriceList.price: PriceList.price * 0.95, PriceList.type_price_id : 2}, synchronize_session=False)
                session.commit()
            if days <= 3:
                session.query(PriceList).filter(
                    and_(PriceList.id == i, PriceList.place_keeping_id == self.number_supermarket)). \
                    update({PriceList.price: PriceList.price * 0.5, PriceList.type_price_id: 3},
                           synchronize_session=False)
                session.commit()

