import requests
import json
BASE = "http://127.0.0.1:5000/"



books = [
        {'id': 2,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'published': '1992'},
        {'id': 3,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
        'published': '1973'},
        {'id': 4,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'}
]


#response = requests.get(BASE + "getid/0")
#print(response.json())
#
# response = requests.get(BASE + "getid/2")
# print(response.json())

# #already exists
# response = requests.post(BASE + "getid/3", {"id":3,"title":"Report Card","published":2020,"author":"Dinkar jani"})
# print(response.json())

# response = requests.post(BASE + "getid/3", {"id":3,"title":"Report Card","published":2020,"author":"Dinkar jani"})
# print(response.json())


# response = requests.delete(BASE + "getid/2")
# print(response.content)

#with DB
response = requests.post(BASE + "getid/1", {"id":1,"title":"Report Card","published":2020,"author":"Dinkar jani"})
print(response.json())

response = requests.get(BASE + "getid/0")
print(response.json())

'''

print("POST")

try:
    for i in books:
        response = requests.post(BASE + "getid/" + str(i['id']), i)
        print(response.json())
except:
    print("API is not accesible")
    exit()
    
print("POST")

input()
response = requests.get(BASE + "getid/2")


print(response.json())

print("PATCH")

input()
response = requests.patch(BASE + "getid/2", {"published":2022,"author":"Bhaskar Mandiya"})
print(response.json())

print("GET")

input()
response = requests.get(BASE + "getid/2")
print(response.json())

print("DELETE")

input()
response = requests.delete(BASE + "getid/2")
print(response.json())

print("GET")

input()
response = requests.get(BASE + "getid/2")
print(response.json())
'''