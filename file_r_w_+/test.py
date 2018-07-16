

with open ( "file.txt" ,'r' ) as f:
        for line in f.readlines():
                print ( line )

with open ( "file.txt" ,'r+' ) as f:
        #for line in f.readlines():
        f.write('r+ ...')


# w+ : 如果文件不存在，则建立
with open ( "file.write2.txt" , 'w+' ) as f: 
        for line in f.read():
            print (line)
        f.write('w+ ...2 ')
