import json

with open('output.json') as f:
    data = json.load(f)

print(type(data), data[0], len(data))

dic = {
    'name': 'John',
    'age': 30,  
    'city': 'New York'}
def greet(**kwargs):
    for k in kwargs.items():
        print(k)

greet(**dic)