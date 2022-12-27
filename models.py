from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, SessionLocal, engine


class PlaceOfKeeping(Base):
    __tablename__ = "PlaceOfKeeping"
    __table_args__ = {"schema": "cd"}

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Items(Base):
    __tablename__ = "Items"
    __table_args__ = {"schema": "cd"}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    name_of_company = Column(String)
    country_of_company = Column(String)
    id_company = Column(Integer, primary_key=True)
    date_of_end = Column(Integer)
    inner_price = Column('inner_price', Float)


class TypeOfPrices(Base):
    __tablename__ = "TypeOfPrices"
    __table_args__ = {"schema": "cd"}

    id = Column(Integer, primary_key=True)
    name = Column(String)


class PriceList(Base):
    __tablename__ = "PriceList"
    __table_args__ = {"schema": "cd"}

    id = Column(Integer, primary_key=True)
    item_id = Column(
        Integer, ForeignKey("cd.Items.id"), primary_key=True
    )
    item = relationship("Items")
    price_id = Column(
        Integer, ForeignKey("cd.TypeOfPrices.id"), primary_key=True
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
