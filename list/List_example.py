# List example common
Bike_part = ['Engine', 'cluth', 'Dashboard', 'gear', 'lever']
Bike_part[2] = "meter"
extra_items = ['greas', 'oil']
print(Bike_part)
print(Bike_part[2])
print(Bike_part[1:4])
print(Bike_part.append('break pads'))
print(Bike_part.insert(5,'tyres'))
Bike_part.extend(extra_items)
print(Bike_part)
Bike_part.pop()
Bike_part.pop(5)
Bike_part.remove("greas")
print(Bike_part)


for a in range(len(Bike_part)):
    print(Bike_part[3])

a = 1
while a < len(Bike_part):
    print(Bike_part[a])
    a = a + 1


# example 2
cake_machine = ["Mixing Bowls","whisks","heating elements"]
print(len(cake_machine))
cake_machine.remove("whisks")
print(cake_machine[0:2])
print(cake_machine.append('whisks'))
print(cake_machine.insert(3,'bitter'))
print(cake_machine)
for c in range(len(cake_machine)):
    print(c)

cake_machine.pop()
print(cake_machine)


#examples 3 
Banner_machine = ['print head','ink pump', 'moter', 'carrige belt', 'encode sensor']
laminate_machine = ['lamination paper', 'plastic paper', 'glue']
laminate_paper = Banner_machine + laminate_machine
print(laminate_paper)

b = 1
while b < len(Banner_machine):
    print(Banner_machine[b])
    b = b + 1

print(len(laminate_paper))

#example 4
water_pump = ['volute', 'shaft', 'impeller', 'bearings']
add_extra = water_pump * 2
print(add_extra)
water_pump2 = ['volute', 'shaft', 'impeller', 'bearings']
print(water_pump == water_pump2)
water_pump.pop(1)

for i in range(5):
    water_pump.append("shaft")


#example 5 
toy_train = ['chasis', 'moter', 'drive', 'body shell']
print("Toy Train Coaches:")
print(toy_train)

toy_train.append("Coach3")
print(toy_train)

toy_train.pop()

toy_train.insert(2, "Coach2")
print(toy_train)

print(len(toy_train))

