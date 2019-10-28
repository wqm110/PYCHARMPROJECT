# -*- coding: utf-8 -*-
import os
import sys

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver

fpath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ffpath = os.path.abspath(os.path.join(fpath, ".."))
print(ffpath)
sys.path.append(ffpath)
#
#
# from SpiderP.items import SpiderpItem
# from SpiderP.items import TpyeItem#

from SpiderP.items import SpiderpItem
from SpiderP.items import TpyeItem


def x_path(re, url):
    try:
        if len(re.xpath(url)) > 0:
            return re.xpath(url)[0].get().strip().replace('"', '')
        else:
            return ''
    except:

        return ''


class HousespiderSpider(CrawlSpider):
    name = 'houseSpider'
    # allowed_domains = ['www.*.qfang.com']
    start_urls = ['https://www.qfang.com/index.html#BDPZ?utm_source=baidu&utm_medium=PZ&utm_term=PC-zhubiaoti']

    rules = (
        # 城市链接
        Rule(LinkExtractor(allow=r'https://.*.qfang.com', deny=r'.com/.*'), callback='parse_item', follow=True),
        # 新房列表
        Rule(LinkExtractor(allow=r'/newhouse/\d?insource=new_list&top=\d'), callback='parse_list_item', follow=False),

    )

    # 城市
    def parse_item(self, response):
        # 二手房  /sale/list
        # 新房 /newhouse/list
        # 租房  /rent/list
        # 小区 /garden/
        # print(response.url)
        yield scrapy.Request(response.url + '/newhouse/list', callback=self.parse_list_item)

    # 城市房屋列表
    def parse_list_item(self, response):
        # print('parse_list_item --> ', response.url)
        # 新房 单条
        list_item_urls = LinkExtractor(allow=r'/newhouse/.*?insource=new_list&top=.*').extract_links(response)
        for list_item_url in list_item_urls:
            # print('list_item_url', list_item_url.url)
            yield scrapy.Request(list_item_url.url, callback=self.parse_detail_new)
        # 下一页
        next_page = LinkExtractor(allow=r'/newhouse/list/n\d+').extract_links(response)
        for n in next_page:
            yield scrapy.Request(n.url, callback=self.parse_list_item)

    def parse_detail_new(self, response):
        gr = ''
        item = SpiderpItem()
        head = response.xpath('/html/head/script').xpath('text()')  # /html/body/div[6]/script[4]
        maps = response.xpath('/html/body/div[6]/script').xpath('text()')  # /html/body/div[6]/script[4]
        for m in maps:
            lines = m.get()
            # print('lines',lines)
            for text in lines.strip().split(';'):
                if 'longitude' in text:
                    longitude = text.replace('var longitude=', '').strip()
                    item['longitude'] = longitude.replace('"', '')
                    # print(longitude)
                if 'latitude' in text:
                    latitude = text.replace('var latitude=', '').strip()
                    item['latitude'] = latitude.replace('"', '')
                    # print(latitude)
                if 'city' in text:
                    city_name = text.replace('var city=', '').strip().replace('"', '')
                    item['city_name'] = city_name
                    # print(city_name)

        for id in head:
            textlines = id.get()
            # print(textlines)
            for text in textlines.split(';'):
                # print(text)
                text = text.strip()
                if 'gardenId' in text:
                    if 'var pageStyle="new"' not in text:
                        gardenId = text.replace('var gardenId =', '').strip()
                        # print('gardenId=',gardenId)
                        item['gardenId'] = gardenId
                        # gr = gardenId
                if 'newhouseID' in text:
                    newhouseID = text.replace('var newhouseID=', '').strip()
                    # print('newhouseID=',newhouseID)
                    item['house_id'] = newhouseID
                    gr = newhouseID
                if 'roomId' in text:
                    roomId = text.replace('var roomId =', '').strip()
                    # print('roomId= ',roomId)
                    item['roomId'] = roomId
                if 'roomCity' in text:
                    roomCity = text.replace('var roomCity =', '').strip()
                    # print('roomcity =',roomCity)
                    # item['city_name'] = roomCity
                    item['city_id'] = roomCity.replace('"', '')
                if 'gardenName' in text:
                    gardenName = text.replace('var gardenName=', '').strip()
                    # print('roomcity =',roomCity)
                    item['gardenName'] = gardenName.replace('"', '')

        item['volume_ratio'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[2]/p/text()')
        item['region'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[3]/p/text()')
        item['greening_rate'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[4]/p/text()')
        item['reference_price'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[5]/p/text()')
        item['totle_house'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[6]/p/text()')
        item['decoration_situation'] = x_path(response,
                                              '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[7]/p/text()')
        item['parking_place'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[8]/p/text()')
        item['area'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[10]/p/text()')
        item['property_company'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[12]/p/text()')
        item['property_fee'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[14]/p/text()')
        item['developers'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[18]/p/text()')
        item['ts'] = x_path(response, '/html/body/div[2]/div/div[1]/div/text()')
        item['price_sum'] = ''
        item['price_time'] = x_path(response, '/html/body/div[4]/div/div[2]/div[1]/div[1]/p[2]/text()')
        item['use'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[9]/p/text()')
        item['property_right'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[11]/p/text()')
        item['opening_time'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[13]/p/text()')
        item['delivery_time'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[15]/p/text()')
        item['bh'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[16]/div/text()')
        item['address'] = x_path(response, '/html/body/div[6]/div[1]/div[1]/div[3]/div[2]/ul/li[17]/p/text()')

        item['url'] = response.url
        item['house_type'] = 'newhouse'
        yield item

        op = webdriver.FirefoxOptions()
        op.add_argument('--headless')
        dr = webdriver.Firefox(executable_path='D:\Chrome_x64\\geckodriver.exe', options=op)
        dr.get(response.url)

        dr.implicitly_wait(10)

        # map = dr.find_elements_by_xpath('/html/body/div[6]/script')#/html/body/div[6]/script[4]
        # print('map=========',map)
        # for m in map:
        #     print('m.text =',m)
        # 户型部分
        list = dr.find_elements_by_xpath('//*[@id="newhsDMF"]/ul/li')

        print(list)
        try:
            for k, l in enumerate(list):
                house_tp_title = ''
                house_tp_ts = ''
                house_tp_sumprice = ''
                house_tp_firstpay = ''
                house_tp_monthpay = ''
                house_yp_area = ''
                house_imgs = ''
                try:
                    house_tp_title = l.find_element_by_xpath('div[2]/div[1]/p[1]').text
                except Exception as e:
                    print(e)
                    pass
                try:
                    house_tp_sumprice = l.find_element_by_xpath('div[2]/div[1]/p[2]').text
                except Exception as e:
                    print(e)
                    pass
                try:
                    house_tp_firstpay = l.find_element_by_xpath('div[2]/div[2]/div[1]/p[1]').text
                except Exception as e:
                    print(e)
                    pass
                try:
                    house_tp_monthpay = l.find_element_by_xpath('div[2]/div[2]/div[2]/p/em').text
                except Exception as e:
                    pass
                    print(e)
                try:
                    house_yp_area = l.find_element_by_xpath('div[2]/div[2]/div[1]/p[2]/em').text
                except Exception as e:
                    print(e)
                    pass
                try:
                    seletor = l.find_element_by_xpath('div[2]/div[3]')
                    house_tp_ts = seletor.text
                except Exception as e:
                    print(e)

                try:
                    house_imgs = l.find_element_by_xpath('div[1]/a/img').get_attribute('src')
                except:
                    pass
                house_tp_status = ''
                house_type_id = k

                item = TpyeItem()
                item["house_type_id"] = gr + '_' + str(house_type_id)
                item["house_tp_title"] = house_tp_title
                item["house_tp_status"] = house_tp_status
                item["house_tp_sumprice"] = house_tp_sumprice
                item["house_tp_firstpay"] = house_tp_firstpay
                item["house_tp_monthpay"] = house_tp_monthpay
                item["house_yp_area"] = house_yp_area
                item["house_tp_ts"] = house_tp_ts
                item["house_imgs"] = house_imgs
                item["gardenId"] = gr
                item["url"] = response.url
                yield item
        except Exception as e:
            print(e)
            dr.close()
            dr.__exit__()
        dr.close()
        dr.__exit__()
