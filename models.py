from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base, SessionLocal


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


class StopList0(Base):
    __tablename__ = "StopList 0"

    item_id = Column(Integer, primary_key=True)
    cause = Column(String)


class StopList1(Base):
    __tablename__ = "StopList 1"

    item_id = Column(Integer, primary_key=True)
    cause = Column(String)


class WareHouse0(Base):
    __tablename__ = "Warehouse 0"

    item_id = Column(Integer, primary_key=True)
    count = Column(String)


class WareHouse1(Base):
    __tablename__ = "Warehouse 1"

    item_id = Column(Integer, primary_key=True)
    count = Column(String)


class ShopHall0(Base):
    __tablename__ = "ShopHall 0"

    item_id = Column(Integer, primary_key=True)
    count = Column(String)


class ShopHall1(Base):
    __tablename__ = "ShopHall 1"

    item_id = Column(Integer, primary_key=True)
    count = Column(String)


class PriceList(Base):
    __tablename__ = "PriceList"

    id = Column(Integer, primary_key=True)
    item_id = Column(
        Integer, ForeignKey("Items.id"), primary_key=True
    )
    item = relationship("Items")
    type_price_id = Column(
        Integer, ForeignKey("TypeOfPrices.id"), primary_key=True, name='type_price_id'
    )
    type = relationship("TypeOfPrices")
    place_keeping_id = Column(
        Integer, ForeignKey("PlaceOfKeeping.id"), primary_key=True
    )
    price = Column(Float)



