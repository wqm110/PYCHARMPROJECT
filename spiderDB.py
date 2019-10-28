from typing import Type

import sqlalchemy
from sqlalchemy import databases
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://spider:spider@localhost:3306/spider')
# 创建对象的基类:
Base = declarative_base()

DBSession = sessionmaker(bind=engine)


# 定义User对象:
class House(Base):
    # 表的名字:
    __tablename__ = 'house'

    # 表的结构:

    house_id = Column(String(120), primary_key=True)
    url = Column(String(120))
    city_name = Column(String(120))
    city_id = Column(String(120))
    house_type = Column(String(120))
    bildingname = Column(String(120))
    volume_ratio = Column(String(120))
    region = Column(String(120))
    greening_rate = Column(String(120))
    reference_price = Column(String(120))
    totle_house = Column(String(120))
    decoration_situation = Column(String(120))
    parking_place = Column(String(120))
    area = Column(String(120))
    property_company = Column(String(120))
    property_fee = Column(String(120))
    developers = Column(String(120))
    ts = Column(String(120))
    price_sum = Column(String(120))
    price_time = Column(String(120))
    use = Column(String(120))
    property_right = Column(String(120))
    opening_time = Column(String(120))
    delivery_time = Column(String(120))
    bh = Column(String(120))
    address = Column(String(120))
    types = Column(String(120))
    longitude = Column(String(20))  # 经度
    latitude = Column(String(20))  # 纬度

    # house_type_id = Column(String(120))
    # house_tp_title = Column(String(120))
    # house_tp_status = Column(String(120))
    # house_tp_sumprice = Column(String(120))
    # house_tp_firstpay = Column(String(120))
    # house_tp_monthpay = Column(String(120))
    # house_yp_area = Column(String(120))
    # house_tp_ts = Column(String(120))
    # house_imgs = Column(String(120))
    def __init__(self, city_name, city_id, house_id, house_type, bildingname, volume_ratio, region, greening_rate,
                 reference_price, totle_house, decoration_situation, parking_place, area, property_company,
                 property_fee, developers, ts, price_sum, price_time, use, property_right, opening_time, delivery_time,
                 bh, address, types,
                 # house_type_id, house_tp_title, house_tp_status, house_tp_sumprice,
                 # house_tp_firstpay, house_tp_monthpay, house_yp_area, house_tp_ts, house_imgs,
                 url, longitude, latitude
                 ):
        self.city_name = city_name
        self.city_id = city_id
        self.house_id = house_id
        self.house_type = house_type
        self.bildingname = bildingname
        self.volume_ratio = volume_ratio
        self.region = region
        self.greening_rate = greening_rate
        self.reference_price = reference_price
        self.totle_house = totle_house
        self.decoration_situation = decoration_situation
        self.parking_place = parking_place
        self.area = area
        self.property_company = property_company
        self.property_fee = property_fee
        self.developers = developers
        self.ts = ts
        self.price_sum = price_sum
        self.price_time = price_time
        self.use = use
        self.property_right = property_right
        self.opening_time = opening_time
        self.delivery_time = delivery_time
        self.bh = bh
        self.address = address
        self.types = types
        # self.house_type_id = house_type_id
        # self.house_tp_title = house_tp_title
        # self.house_tp_status = house_tp_status
        # self.house_tp_sumprice = house_tp_sumprice
        # self.house_tp_firstpay = house_tp_firstpay
        # self.house_tp_monthpay = house_tp_monthpay
        # self.house_yp_area = house_yp_area
        # self.house_tp_ts = house_tp_ts
        # self.house_imgs = house_imgs
        self.url = url
        self.longitude = longitude
        self.latitude = latitude

    def h_save(self):
        session = DBSession()
        session.merge(self)
        session.commit()
        session.close()


class Types(Base):
    __tablename__ = 'houseTypes'
    house_type_id = Column(String(120), primary_key=True)
    house_tp_title = Column(String(120))
    house_tp_status = Column(String(120))
    house_tp_sumprice = Column(String(120))
    house_tp_firstpay = Column(String(120))
    house_tp_monthpay = Column(String(120))
    house_yp_area = Column(String(120))
    house_tp_ts = Column(String(120))
    house_imgs = Column(String(120))
    gardenId = Column(String(120))
    url = Column(String(120))

    def __init__(self, house_type_id, house_tp_title, house_tp_status, house_tp_sumprice, house_tp_firstpay,
                 house_tp_monthpay, house_yp_area, house_tp_ts, house_imgs, gardenId, url):
        self.house_type_id = house_type_id
        self.house_tp_title = house_tp_title
        self.house_tp_status = house_tp_status
        self.house_tp_sumprice = house_tp_sumprice
        self.house_tp_firstpay = house_tp_firstpay
        self.house_tp_monthpay = house_tp_monthpay
        self.house_yp_area = house_yp_area
        self.house_tp_ts = house_tp_ts
        self.house_imgs = house_imgs
        self.gardenId = gardenId
        self.url = url

    def t_save(self):
        session = DBSession()
        session.merge(self)
        session.commit()
        session.close()


# 初始化数据库连接:
# 创建DBSession类型:

Base.metadata.create_all(engine)
