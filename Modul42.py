num = []
x = []
for i in range(1, 11):
    num.append(int(input("Enter a number: ")))
for i in num:
    x.append(int(i) % 42)
z = (dict((y,x.count(y)) for y in set(x)))
print(len(z.keys()))