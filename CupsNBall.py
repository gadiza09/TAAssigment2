options = str(input("Please enter the moves (a/b/c): "))
spaces = ["b", " ", " "]
for i in range(len(options)):
    if options[i] == "a":
        temporary = spaces[0]
        spaces[0] = spaces[1]
        spaces[1] = temporary
    elif options[i] == "b":
        temporary = spaces[1]
        spaces[1] = spaces[2]
        spaces[2] = temporary
    elif options[i] == "c":
        temporary = spaces[0]
        spaces[0] = spaces[2]
        spaces[2] = temporary
    else:
        print("Please choose only a/b/c.")
print(spaces)
for j in range(3):
    if spaces[j] == "b":
        print("The ball is in position", j+1)