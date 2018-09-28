def stones(n):
    if n%2 == 0:
        print("Bob")
    else:
        print ("Alice")
while True:
    n = int(input("Please input a number: "))
    stones(n)