# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item


class SpiderpItem(Item):
     
    city_name = scrapy.Field()
    url = scrapy.Field()
    city_id = scrapy.Field()
    gardenId = scrapy.Field()
    gardenName = scrapy.Field()
    roomId = scrapy.Field()
    house_id = scrapy.Field()
    house_type = scrapy.Field()
    bildingname = scrapy.Field()
    volume_ratio = scrapy.Field()
    region = scrapy.Field()
    greening_rate = scrapy.Field()
    reference_price = scrapy.Field()
    totle_house = scrapy.Field()
    decoration_situation = scrapy.Field()
    parking_place = scrapy.Field()
    area = scrapy.Field()
    property_company = scrapy.Field()
    property_fee = scrapy.Field()
    developers = scrapy.Field()
    ts = scrapy.Field()
    price_sum = scrapy.Field()
    price_time = scrapy.Field()
    use = scrapy.Field()
    property_right = scrapy.Field()
    opening_time = scrapy.Field()
    delivery_time = scrapy.Field()
    bh = scrapy.Field()
    address = scrapy.Field()
    types = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    
    pass
class TpyeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_type_id = scrapy.Field()
    house_tp_title = scrapy.Field()
    house_tp_status = scrapy.Field()
    house_tp_sumprice = scrapy.Field()
    house_tp_firstpay = scrapy.Field()
    house_tp_monthpay = scrapy.Field()
    house_yp_area = scrapy.Field()
    house_tp_ts = scrapy.Field()
    house_imgs = scrapy.Field()
    gardenId = scrapy.Field()
    url = scrapy.Field()

    pass
