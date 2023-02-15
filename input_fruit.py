in_file = open("input_data.txt", "r")
fruits = in_file.readlines()
print(fruits)
in_file.close()


in_file = open("input_data.txt", "r")
for line in in_file:
    print(line)


first_fruit = in_file.readline()
second_fruit = in_file.readline()
