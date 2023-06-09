# JSON is java script object notation
# JSON is a data exchange format similar to XML
book ={}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 9898000
}
book['bob']={
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 23433636
}
import json
s=json.dumps(book)
with open("C://data//book.txt","w") as f:
    f.write(s)
f=open("C://data//book.txt", "r")
s=f.read()
print("Json: ",s)

book = json.loads(s) # dictionary
print(book)

bBook = book['bob']
print(bBook)

#print Bob's phone
bphone = bBook['phone']
print("Bob phone: ", bphone)

for person in book:
    print(book[person])
