results = input("Which list do you want?\n1D List\n2D List\n3D List: ")

# 1D LIST
if(results == "1" or results == "1D"):
    size = int(input("How many elements do you want? "))
    one_d = []

    for i in range(size):
        val = int(input(f"Enter element {i+1}: "))
        one_d.append(val)
    print("1D List:", one_d)


# 2D LIST
elif(results == "2" or results == "2D"):
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    two_d = []

    for i in range(rows):
        row = []
        for j in range(cols):
            val = input(f"Enter element [{i}][{j}]: ")
            row.append(val)
        two_d.append(row)
    print(two_d)


# 3D LIST 
elif(results == "3" or results == "3D"):
    layers = int(input("Enter number of layers: "))
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    three_d = []

    for l in range(layers):
        layer = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = input(f"Enter element [{l}][{i}][{j}]: ")
                row.append(val)
            layer.append(row)
        three_d.append(layer)
    print(three_d)


else:
    print("Invalid choice!")
