path = "../data/numbers.txt"

numbers = []

with open(path, "r") as file: 
    for line in file:
        numbers.append(int(line))

print(numbers)

out_path = "../data/numbers_decreased.txt"

with open(out_path, "w") as file:
    for number in numbers:
        line = str(number - 100) + "\n"
        file.write(line)


