layer = int(input("enter value: "))
row = int(input("enter value: "))

data_values = [] 

for i in range(layer):
    layer_value = []
    print(f"layers {i+1}")

    for j in range(row):
        row_value = []

        val_name = input("enter name: ")
        val_num = int(input("enter value number: "))
        val_grade = input("enter value grade:")

        row_value.append(val_name)
        row_value.append(val_num)
        row_value.append(val_grade)

        layer_value.append(row_value)

    data_values.append(layer_value)
    print(data_values)