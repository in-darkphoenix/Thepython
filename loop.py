emails = ['me@gmail.com','you@hotmail.com','they@gmail.com']
for item in emails :
    if 'gmail' in item :
        print(item)


def inrtousd(rate,inr) :
    return float(rate) * float(inr)

r  = input("Enter the rate - ")
i  = input("Enter the amount - ")
print(inrtousd(r,i))


password = ''
while password != 'python123' :
    password  = input("Enter the password  - ")
    if password == 'python123' :
        print("You are logged in!")
    else :
        print("Sorry, try again!!!")


name = ['John','Danaerys','Tyrion']
house = ['Snow','Targeryan','Lannister']
for i,j in zip(name,house) :
    print(i,j)
