# example 1 for nested-if-else
target_Score = "192/6"
win_Score = "193"

if win_Score > target_Score:
    if win_Score:
        print("Team is Winner for target score")
    else:
        print("Team not complete target")
else:
    print("Rain delay")

# example 2 for nested-if-else
stu_age = 18
age = 20

if stu_age >= 20:
    if age:
        print("improved age")
    else:
        print("maintain age")
else:
    print("Not Eligible ")

# example 3 for nested-if-else
max_atten = "280 Days"
min_atten = "200 Days"

if max_atten > min_atten:
    if min_atten:
        print("minimum attendence is required")
    else:
        print("attendence not not required")
else:
    print("Complesary Attendence for all students")

# example 4 for nested-if-else
dl_age = 25
license = True

if dl_age >= 20:
    if license:
        print("you can drive on vehical")
    else:
        print("you will need leaning license")
else:
    print("Your age is not eligible for drive")

# example 5 for nested-if-else
kabbadi_member = 9
student = True

if kabbadi_member >= 5:
    if student:
        print("Minimum 7 member required in Kabbadi")
    else:
        print("Maximum 9 student required")
else:
    print("student will not participate in kabbadi")

# example 6 for nested-if-else
Grade = "AA"
rank = True

if Grade >= "AA":
    if rank:
        print("AA grade is topper in the gtu")
    else:
        print("BB grade is topper in the class")
else:
    print("Grade is not impotant as ranking")

# example 7 for nested-is-else
charger_amount = 120
price = True

if charger_amount <= 100:
    if price:
        print("Amount is very high")
    else:
        print("Best Quality of charger case")
else:
    print("Delivery charges apply")

# example 7 for nested-is-else
gov_exam_result = "3 days"
gov_result = True

if gov_exam_result <= "4 days":
    if gov_result:
        print("Result view only 3 day")
    else:
        print("after 3 days site closed")
else:
    print("site reopen next month")

# example 9 for nested-is-else
account_amount = "Rs.200"
amount = True

if account_amount >= "Rs.8000":
    if price:
        print("Account is oprative")
    else:
        print("Account is in-operative")
else:
    print("Please fill oprative banck account form")

# example 10 for nested-is-else
Temp = 29
temp_code = True

if Temp <= 35:
    if price:
        print("summer weather is coming")
    else:
        print("winnter season")
else:
    print("multi weather season")

# example 11 for nested-is-else
racing_track = "1 km"
track_score = True

if racing_track <= "500 meter":
    if track_score:
        print("racing track is not valid for fast car")
    else:
        print("racing tra is 800 meter")
else:
    print("Racing track is 1.2 km valid for fastest car")

# example 12 for nested-is-else
dob_tob = "date 13/09/2005 and time 5 pm"
dot = True

if dob_tob == "date 13/09/2005 and time 5 pm":
    if dot:
        print("original birth date and time")
    else:
        print("date and time is wrong")
else:
    print("please fill original date and itme")


# example 13 for nested-is-else
festival = "Diwali"
amount = 500

if festival == "Diwali":
    if amount >= 600:
        print("shoes 30% Diwali Discount")
    elif amount >= 250:
        print("shoes 20% Diwali Discount")
    else:
        print("10% Diwali Discount")
else:
    print("No festival discount")


# example 13 for nested-is-else
movie = "dhurandhar"
ticket = 100

if movie == "dhurandhar":
    if ticket >= 200:
        print("Monday")
    elif ticket == 100:
        print("Tuesday")
    else:
        print("No discount at that day")
else:
    print("discount only tuesday")


# example 14 for nested-is-else
today = 10
Agrim = 12

if today < Agrim:
    print("Event is in", Agrim - today, "days")
elif today == Agrim:
    print("Today is the Event Day!")
else:
    print("Event is over")


# example 15 for nested-is-else
sender = "friend"
recive = True

if sender == "other":
    if recive:
        print("Reply immediately")
    else:
        print("Reply later")
else:
    print("Ignore or check later")


# example 16 for nested-is-else
img_recyle = 10
reclye_done = True

if img_recyle <= 15:
    if reclye_done:
        print("images are recycle in file manage/application")
    else:
        print("images are not recycle in file manage/application")
else:
    print("data is not recycling")


# example 17 for nested-is-else
population = 1200000

if population >= 1000000:
    if population >= 1500000:
        print("population is very high in india colony")
    else:
        print("population is medium in india colony")
else:
    print("population count after 5 years")


# example 18 for nested-is-else
money = 150
food = True

if food:
    if food >= 200:
        print("Buy a burger ")
    elif food >= 100:
        print("Buy snacks")
    else:
        print("Not enough money Eat at home")
else:
    print("No need to buy food")
