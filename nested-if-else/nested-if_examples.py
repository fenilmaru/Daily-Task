# Example 1
target_score = int(input("Enter target score: "))
win_score = int(input("Enter win score: "))

if win_score > target_score:
    print("Team is Winner for target score")
else:
    print("Team not complete target")


# Example 2
stu_age = int(input("\nEnter student age: "))

if stu_age >= 20:
    print("Improved age")
else:
    print("Not Eligible")


# Example 3
max_atten = int(input("\nEnter maximum attendance days: "))
min_atten = int(input("Enter minimum attendance days: "))

if max_atten > min_atten:
    print("Minimum attendance is required")
else:
    print("Compulsory Attendance for all students")


# Example 4
dl_age = int(input("\nEnter your age: "))
license = input("Do you have license? (yes/no): ")

if dl_age >= 20:
    if license == "yes":
        print("You can drive vehicle")
    else:
        print("You need learning license")
else:
    print("Age not eligible for driving")


# Example 5
kabbadi_member = int(input("\nEnter number of players: "))
student = input("Are you student? (yes/no): ")

if kabbadi_member >= 5:
    if student == "yes":
        print("Minimum 7 members required")
    else:
        print("Maximum 9 members allowed")
else:
    print("Cannot participate in Kabaddi")


# Example 6
grade = input("\nEnter your grade: ")
rank = input("Do you have rank? (yes/no): ")

if grade == "AA":
    if rank == "yes":
        print("AA grade is topper")
    else:
        print("AA grade without rank")
else:
    print("Grade is not important")


# Example 7
charger_amount = int(input("\nEnter charger price: "))

if charger_amount <= 100:
    print("Best Quality charger")
else:
    print("Delivery charges apply")


# Example 8
gov_exam_days = int(input("\nEnter result available days: "))

if gov_exam_days <= 4:
    print("Result available")
else:
    print("Site reopen next month")


# Example 9
account_amount = int(input("\nEnter account balance: "))

if account_amount >= 8000:
    print("Account is operative")
else:
    print("Please fill operative bank form")


# Example 10
temp = int(input("\nEnter temperature: "))

if temp <= 35:
    print("Summer weather")
else:
    print("Multi weather season")


# Example 11
racing_track = int(input("\nEnter track length (meters): "))

if racing_track <= 500:
    print("Track not valid for fast car")
else:
    print("Track valid for racing")


# Example 12
dob = input("\nEnter DOB (dd/mm/yyyy): ")

if dob == "13/09/2005":
    print("Original birth date")
else:
    print("Wrong birth date")


# Example 13
festival = input("\nEnter festival name: ")
amount = int(input("Enter purchase amount: "))

if festival == "Diwali":
    if amount >= 600:
        print("30% Discount")
    elif amount >= 250:
        print("20% Discount")
    else:
        print("10% Discount")
else:
    print("No festival discount")


# Example 14
movie = input("\nEnter movie name: ")
ticket = int(input("Enter ticket price: "))

if movie == "dhurandhar":
    if ticket == 100:
        print("Tuesday Discount")
    else:
        print("No discount")
else:
    print("Discount only on Tuesday")


# Example 15
today = int(input("\nEnter today date: "))
event = int(input("Enter event date: "))

if today < event:
    print("Event in", event - today, "days")
elif today == event:
    print("Today is Event Day")
else:
    print("Event is over")


# Example 16
sender = input("\nEnter sender type (friend/other): ")

if sender == "other":
    print("Reply immediately")
else:
    print("Ignore or reply later")


# Example 17
img_recycle = int(input("\nEnter recycle count: "))

if img_recycle <= 15:
    print("Images recycled")
else:
    print("Data not recycling")


# Example 18
population = int(input("\nEnter population count: "))

if population >= 1000000:
    if population >= 1500000:
        print("Very high population")
    else:
        print("Medium population")
else:
    print("Low population")


# Example 19
money = int(input("\nEnter money amount: "))

if money >= 200:
    print("Buy Burger")
elif money >= 100:
    print("Buy Snacks")
else:
    print("Eat at home")
