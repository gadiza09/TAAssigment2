x = input("Please input names, separated by hyphens (ex. Gadiza-Pribadi): ")
y = x.replace("-", " ")
z = y.split()
def shortVar(z):
    for i in z:
        print(i[0].upper(), end = "")
shortVar(z)
