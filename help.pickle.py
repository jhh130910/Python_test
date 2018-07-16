# dumps功能
import pickle
data = ['aa', 'bb', 'cc']  
# dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)            
#b'\x80\x03]q\x00(X\x02\x00\x00\x00aaq\x01X\x02\x00\x00\x00bbq\x02X\x02\x00\x00\x00ccq\x03e.

# loads功能
# loads  将pickle数据转换为python的数据结构
mes = pickle.loads(p_str)
print(mes)
['aa', 'bb', 'cc']

# dump功能
# dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('D:/tmp.pk', 'w') as f:
    pickle.dump(data, f)

# load功能
# load 从数据文件中读取数据，并转换为python的数据结构
with open('D:/tmp.pk', 'r') as f:
    data = pickle.load(f)

