rows = int(input("Please input the number of rows: "))
def pascalsTriangle(rows):
    numbers = []
    for i in range(rows):
        row = [1]
        if numbers:
            bottom = numbers[-1]
            row.extend([sum(num) for num in zip(bottom, bottom[1:])])
            row.append(1)
        numbers.append(row)
    return numbers

for i in pascalsTriangle(rows):
    print(i)
