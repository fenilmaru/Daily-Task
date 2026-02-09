hills = ['mountainA','mountainB','mountainC','maountainD','mountainE']
hills_str = [[54,45,457,25,84,34,354],[4,46,58],['Raj','ahd','Delhi']]

dictnary_main = {}

for i in range(len(hills_str[0])):
    if i < len(hills):
        key = hills[i]
    else:
        key = f"Not Available {i - len(hills) + 1}"

    # height 
    height = hills_str[0][i]

    # width
    if i < len(hills_str[1]):
        width = hills_str[1][i]
    else:
        width = "0"  
        
    # location
    if i < len(hills_str[2]):
        location = hills_str[2][i]
    else:
        location = "Not Avilable"

    dictnary_main[key] = {
        "height": height,
        "width": width,
        "location": location
    }

print(dictnary_main)
