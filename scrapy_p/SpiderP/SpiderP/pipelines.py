# -*- coding: utf-8 -*-
import scrapyd
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys

from scrapy.exporters import JsonLinesItemExporter

fpath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ffpath = os.path.abspath(os.path.join(fpath, ".."))
print(ffpath)
sys.path.append(ffpath)
from SpiderP.items import SpiderpItem
from SpiderP.items import TpyeItem

sys.path.append(r'D:\Anaconda3\Scripts\myModel\\')
from spiderDB import House, Types


class SpiderpPipeline(object):
    def __init__(self) -> None:
        self.fp = open('weixin.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def process_item(self, item, spider):
        # print('xxxx')

        self.exporter.export_item(item)
        if isinstance(item, SpiderpItem):
            city_name = item.get("city_name")
            city_id = item.get("city_id")
            house_id = item.get("house_id")
            gardenName = item.get("gardenName")
            house_type = item.get("house_type")
            bildingname = item.get("gardenName")
            volume_ratio = item.get("volume_ratio")
            region = item.get("region")
            greening_rate = item.get("greening_rate")
            reference_price = item.get("reference_price")
            totle_house = item.get("totle_house")
            decoration_situation = item.get("decoration_situation")
            parking_place = item.get("parking_place")
            area = item.get("area")
            property_company = item.get("property_company")
            property_fee = item.get("property_fee")
            developers = item.get("developers")
            ts = item.get("ts")
            price_sum = item.get("price_sum")
            price_time = item.get("price_time")
            use = item.get("use")
            property_right = item.get("property_right")
            opening_time = item.get("opening_time")
            delivery_time = item.get("delivery_time")
            bh = item.get("bh")
            address = item.get("address")
            types = item.get("types")
            # house_type_id = item.get("house_type_id")
            # house_tp_title = item.get("house_tp_title")
            # house_tp_status = item.get("house_tp_status")
            # house_tp_sumprice = item.get("house_tp_sumprice")
            # house_tp_firstpay = item.get("house_tp_firstpay")
            # house_tp_monthpay = item.get("house_tp_monthpay")
            # house_yp_area = item.get("house_yp_area")
            # house_tp_ts = item.get("house_tp_ts")
            # house_imgs = item.get("house_imgs")
            url = item.get("url")
            longitude = item.get("longitude")
            latitude = item.get("latitude")
            house = House(city_name=city_name, city_id=city_id, house_id=house_id, house_type=house_type,
                          bildingname=bildingname, volume_ratio=volume_ratio, region=region,
                          greening_rate=greening_rate,
                          reference_price=reference_price, totle_house=totle_house,
                          decoration_situation=decoration_situation, parking_place=parking_place, area=area,
                          property_company=property_company, property_fee=property_fee, developers=developers, ts=ts,
                          price_sum=price_sum, price_time=price_time, use=use, property_right=property_right,
                          opening_time=opening_time, delivery_time=delivery_time, bh=bh, address=address, types=types,
                          # house_type_id=house_type_id, house_tp_title=house_tp_title, house_tp_status=house_tp_status,
                          # house_tp_sumprice=house_tp_sumprice, house_tp_firstpay=house_tp_firstpay,
                          # house_tp_monthpay=house_tp_monthpay, house_yp_area=house_yp_area, house_tp_ts=house_tp_ts,
                          # house_imgs=house_imgs,
                          url=url, latitude=latitude, longitude=longitude
                          )
            house.h_save()
            return item
        elif isinstance(item, TpyeItem):
            house_type_id = item.get("house_type_id")
            house_tp_title = item.get("house_tp_title")
            house_tp_status = item.get("house_tp_status")
            house_tp_sumprice = item.get("house_tp_sumprice")
            house_tp_firstpay = item.get("house_tp_firstpay")
            house_tp_monthpay = item.get("house_tp_monthpay")
            house_yp_area = item.get("house_yp_area")
            house_tp_ts = item.get("house_tp_ts")
            house_imgs = item.get("house_imgs")
            gardenId = item.get("gardenId")
            url = item.get("url")

            t = Types(house_type_id=house_type_id, house_tp_title=house_tp_title, house_tp_status=house_tp_status,
                      house_tp_sumprice=house_tp_sumprice, house_tp_firstpay=house_tp_firstpay,
                      house_tp_monthpay=house_tp_monthpay, house_yp_area=house_yp_area, house_tp_ts=house_tp_ts,
                      house_imgs=house_imgs, gardenId=gardenId, url=url
                      )
            t.t_save()

            return item

    def close_spider(self, spider):
        self.fp.close()
