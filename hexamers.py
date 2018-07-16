
import itertools

for x in itertools.product('ACGT',repeat=11):
    print ( "'{0}'".format( ''.join(x) ) )
