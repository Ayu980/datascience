exp = [2340, 2500, 2100, 3100, 2980]
total = 0
for e in exp:
    total = total + e
print(total)
# prints Month with monthly expense
for i in range(len(exp)):
    print('Month: ', (i+1), 'Expense: ', exp[i])

# for loop using range
list = []
for i in range(1,11):
    list.append(i)
print(list)

# for loop using break
key_location = 'chair'
locations = ["garage", "living room", "chair", "closet"]

for i in locations:
    if i==key_location:
        print("Key is found in ", i)
        break
    else:
        print("Key is not found in ", i)

# for loop using continue which skips back to the forloop iteration
for j in range(1,6):
    if j %2 == 0:
        continue
    print(j**2)
# While loop
i = 1
while (i<=5):
    print(i)
    i = i + 1
