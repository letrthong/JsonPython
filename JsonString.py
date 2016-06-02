import json
from types import *

#Declare String
json_data ="{ \"key\": 1 ,\"key2\": \"value2\"}"

#Convert String to Dictionary
Dictionary = json.loads(json_data)


for key, value in Dictionary.items():
	print key
	print value
	print  type(value) 

#Declare Dictionary
Dict_data ={ "key": 1 ,"key2": "value2"}

#Convert dictionary to string
string = json.JSONEncoder().encode(Dict_data)

print string
print  type(string)  

