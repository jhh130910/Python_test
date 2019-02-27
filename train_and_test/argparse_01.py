import argparse 

'''
write user-friendly command-line interfaces. what arguments requires, parse out sys.argv

automatically generate help and usage messages , issue error when user give invaild arguments 

'''

parser = argparse.ArgumentParser(description= ' Start ... ')
#parser.add_argument()
parser.add_argument('-parameter1',metavar='P1', help='this is p1')
parser.add_argument('-parameter2',type=int,metavar='P2',help=' this is p2' )

args = parser.parse_args()

#print (args.accumulate(args.integers))

if __name__ == '__main__' :
	import os 
	print ( os.path )
	print ( os.path.basename('argparse_01.py') )
	print ( os.path.abspath('argparse_01.py') )
	import sys
	print ( sys.version )
