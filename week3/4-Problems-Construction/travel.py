def travel_costs(travels):
    price = 0
    for travel in travels:
        if travel >= 23:
            price += 23
        else:
            price += travel

        if price >= 50:
            price = 50
            
    return price

n = input("Enter number of lines: ")
n = int(n)

count = 1
travels = []

while count <= n:
    travel = input();
    travel = int(travel)
    travels = travels + [travel]
    count +=1
    
print ("The optimal price is:", travel_costs(travels))

