
count = 1
while count :
    with open ( 'chg' + '_' + str(count) + '_' + '.bcl', 'w' ) as f :
        f.write('just test ... ')
        count += 1
        if count > 10 :
            break 

# END 
