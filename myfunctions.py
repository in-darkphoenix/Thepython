def mth(minutes) :
    hour = minutes / 60
    print(hour)

def sth(minutes, seconds = 18000) :
    hour = seconds / 3600 + minutes  / 60
    return hour

def age_foo(age) :
    new_age = float(age) + 50
    return new_age

mth(90)
print(sth(90))
print(sth(90,7200))
age = input("Enter your age - ")
print(age_foo(age))
