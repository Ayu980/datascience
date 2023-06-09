d = {"tom": 206778, "rob": 734730}
print(d)
d["sam"] = 23456
print(d)

del d["sam"]
print(d)
# printing
for key in d:
    print("key:", key, "value:", d[key])

for k,v in d.items():
    print("key: ", k, "value: ", v)
# to check if a specific value is in the dictionary
var = 'tom' in d
print(var)
# to clear the dictionary
d.clear()
print(d)