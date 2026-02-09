id_card = ["Name","Fenil","Enrollment","235491105011","contact","9512074775","Location","Hirawadi"]

list_card = {}

for i in range(0, len(id_card), 2):
    list_card[id_card[i]] = id_card[i+1]

print(list_card)
