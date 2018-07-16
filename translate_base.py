ss = 'AGCT'
trans_pattern = str.maketrans('AG','tc')
print ( ss.translate(trans_pattern) )

a = 'xxxxxxxpppp'.translate(str.maketrans('x','A'))
print (a)