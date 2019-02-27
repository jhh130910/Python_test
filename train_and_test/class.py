'''
class define 
'''

import os
import sys

class Name_About_Class () :
	def __init__ ( self , number , price , sell ) :
		self.number_alias = number
		self.price_alias  = price
		self.sell_alias   = sell 
	def simple_count (self) :
		report_number = self.number_alias ** 4 
		report_price = self.price_alias / 4 
		report_sell = self.sell_alias + self.number_alias + self.price_alias 
		return ( report_number , report_price , report_sell )

if __name__ == '__main__' :
	xxx = Name_About_Class(2,4,6)
	out = xxx.simple_count()
	print ( out )
	xxx_add = Name_About_Class(1,1,1)
	print ( xxx_add.simple_count() )
