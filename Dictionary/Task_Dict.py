data = [['mountainA',10,5,'ahd'],['mountainA',10,5,'ahd'],['mountainA',10,5,'ahd']]
data2 = [['mountainA','mountainB','mountainC'],[10,12,15],[4,3,12],['ahd','ahd','ahd']]

dictionary = {}

for elemnt in data:
   repet_dict = elemnt[0]

   if repet_dict not in dictionary:
      dictionary[repet_dict] = []

   dictionary[repet_dict].append ({
      "height": elemnt[1],
      "weidth": elemnt[2],
      "location" : elemnt[3]
   })


vari_key = (data2[0])
values = list(zip(*data2[1:]))

dictionary2 = {}

for key,value in zip(vari_key,values):
   dictionary2[key] = {
      "height": value[0],
      "weidth": value[1],
      "location": value[2]
   }
   print("Data List 1\n")
   print(dictionary)
   print("data list 2\n")
   print(dictionary2)