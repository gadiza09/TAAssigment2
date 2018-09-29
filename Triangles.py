sym = ("*")
mult = 1
count = 6
while mult <= count:
    print sym*mult
    mult = mult+1

x = 1
while x <= count:
    print (" " * (count - x) + "*" * x)
    x = x + 1

y = 1
while y <= count:
    print (" " * (count - y) + "*" * (y*2-1))
    y = y + 1

p = 1
while p <= count:
    print (" " * (count - p) + "*" * (p*2-1))
    p = p + 1
z=1
s= 10
while z <= s:
    print (" " * z + "*" * (s - (z*2-1)) + " " * z)
    z = z + 1
