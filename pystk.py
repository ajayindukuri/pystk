#!/usr/bin/python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------
# Title : pystk.py 
# Description : Provides details of stock you are intersted in
#--------------------------------------------------------------------------------

import urllib2
import json
import sys

class pyStk:
  def __init__(self,stock_symbol):
    self.link1 = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20%28%22'
    self.link2 = '%22%29&format=json&diagnostics=false&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
    self.query_link = self.link1 + stock_symbol + self.link2
    stock_details = self.get_stock_data(self.query_link)
    #return stock_details
    print_data(stock_details)

  def get_stock_data(self, query_link):
    data = json.load(urllib2.urlopen(query_link))
    stock_data = data['query']['results']['quote']
    symbol = stock_data['Symbol']
    currentPrice = stock_data['LastTradePriceOnly']
    yearHigh = stock_data['YearHigh']
    yearLow = stock_data['YearLow']
    stock_details = [ symbol, currentPrice, yearHigh, yearLow ]
    return stock_details

def print_data(details):
    print('{0:10s} {1:10s} {2:15s} {3:15s}' .format(details[0],details[1],details[2],details[3]))

if __name__ == '__main__':
  details = [ 'Symbol', 'Price', '52week High', '52week Low' ]
  print_data(details)
  print ("-----------------------------------------------------")
  for stock_symbol in sys.argv[1:]:
    myStk = pyStk(stock_symbol)
