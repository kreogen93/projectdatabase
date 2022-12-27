from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, SessionLocal, engine


class PlaceOfKeeping(Base):
    __tablename__ = "PlaceOfKeeping"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Items(Base):
    __tablename__ = "Items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    name_of_company = Column(String)
    country_of_company = Column(String)
    id_company = Column(Integer, primary_key=True)
    date_of_end = Column(Integer)
    inner_price = Column(Float)


class TypeOfPrices(Base):
    __tablename__ = "TypeOfPrices"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class PriceList(Base):
    __tablename__ = "PriceList"

    id = Column(Integer, primary_key=True)
    item_id = Column(
        Integer, ForeignKey("Items.id"), primary_key=True
    )
    item = relationship("Items")
    price_id = Column(
        Integer, ForeignKey("TypeOfPrices.id"), primary_key=True, name='type_price_id'
    )
    type = relationship("TypeOfPrices")
    price = Column(Float)


if not __name__ == "__main__":
    session = SessionLocal()
    results = (
        session.query(PriceList)
        .all()
    )
    print(results)
