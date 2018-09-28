moves = str(input("Please enter the moves (a/b/c): "))
list = ["b", " ", " "]
for i in range(len(moves)):
    if moves[i] == "a":
        temporary = list[0]
        list[0] = list[1]
        list[1] = temporary
    elif moves[i] == "b":
        temporary = list[1]
        list[1] = list[2]
        list[2] = temporary
    elif moves[i] == "c":
        temporary = list[0]
        list[0] = list[2]
        list[2] = temporary
    else:
        print("Please choose only a/b/c.")
print(list)
for j in range(3):
    if list[j] == "b":
        print("The ball is in position", j+1)