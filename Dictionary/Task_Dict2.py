hills = ['mountainA','mountainB','mountainC','maountainD','mountainE']
hills_str = [[10,12,15,25],[4,3,12],['ahd','ahd','ahd']]

dict_merge = {}

for i in range(len(hills)):
    key = hills[i]

    height = "0"
    width = "0"
    location = "not found"

    # height 
    if i < len(hills_str[0]):
        height = hills_str[0][i]

    # width
    if i < len(hills_str[0]) and i < len(hills_str[1]):
        width = hills_str[1][i]
    elif i < len(hills_str[0]):
        width = "0"
    else:
        width = "0"  
        
    # mountainE
    if i < len(hills_str[2]):
        location = hills_str[2][i]

    dict_merge[key] = {
        "height": height,
        "width": width,
        "location": location
    }

print(dict_merge)
