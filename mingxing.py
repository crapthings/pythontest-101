# -*- coding: utf-8 -*-

import re
import scrapy
from bs4 import BeautifulSoup

mingxinglist = open('mingxinglist.txt', 'r').read().split()

base_url = 'https://baike.baidu.com/item/'
mingxing_urls = ['https://baike.baidu.com/item/刘德华']

for mingxing in mingxinglist:
  mingxing_urls.append(base_url + mingxing)

class mingxinglistSpider(scrapy.Spider):
  name = 'mingxinglist'
  start_urls = mingxing_urls

  def parse(self, response):
    for el in response.css('div.poster'):
      item = {
        'name': el.css('.lemmaWgt-lemmaTitle-title').xpath('//h1/text()').extract_first(),
        'summary': el.css('.lemma-summary .para').extract(),
        'works': el.css('#slider_works .maqueeCanvas li').extract(),
        'relations': el.css('#slider_relations .maqueeCanvas li').extract(),
      }

      item['summary'] = re.sub('\\n+', '\n', BeautifulSoup(''.join(item['summary']), 'lxml').get_text())
      item['works'] = re.sub('\\n+', '\n', BeautifulSoup(''.join(item['works']), 'lxml').get_text())
      item['relations'] = re.sub('\\n+', '\n', BeautifulSoup(''.join(item['relations']), 'lxml').get_text())

      yield item
