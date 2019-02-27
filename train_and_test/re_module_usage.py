import re

temp_pattern = re.compile('([0-9]+)')
list_set = []
dict_set = {}

result = re.findall(temp_pattern, '0900000')

print (result)
