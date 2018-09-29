import matplotlib.pyplot as plt

u = 0
speed_limit = 60
t = int(input("Time: "))
a = int(input("Acceleration: "))
s = int(input("Distance: "))
v = u + a*t
d = u * t + ((0.5) * a * t**2)
distanceList = []
timeList = [i for i in range(t+1)]



def speed(u, a, t):
    return u + a*t

def distance(u, a, t):
    return u * t + ((0.5) * a * t**2)

print("* is equal to 10m\n")

duration = 0
dis = 0
while duration <= t:
    dis = distance(u, a, duration)
    i = " "
    distanceList.append(dis)
    while dis >= 10:
        i += "*"
        dis = dis - 10


    print("Duration: " + str(duration) + " / Distance: " + str(i))
    duration = duration + 1

if v >= speed_limit:
    print("\nThe person went over the speed limit." + "(Max speed was " + str(v) + "m/s)")

if v < speed_limit:
    print("\nThe person did not go over the speed limit." + "(Max speed was " + str(v) + "m/s)")

if s < d:
    print("\nThe person did not reach the destination." + "(Reached " + str(d) + "m)")

if s >= d:
    print ("\nThe person reached the destination.." + "(Reached " + str(d) + "m)")

# hello
plt.plot(timeList, distanceList)
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.show()
