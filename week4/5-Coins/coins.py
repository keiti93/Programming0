def calculate_coins(sum1):

    dictionary = {1 : 0,
                  2 : 0,
                  5 : 0,
                  10 : 0,
                  20 : 0,
                  50 : 0,
                  100 : int(sum1//1)}

    a = int(round((sum1*100)%100))
    
    list_coins = [50, 20, 20, 10, 5, 2, 2, 1]
    
    for coin in list_coins:
        if a >= coin:
            dictionary[coin] += 1
            a = a - coin
            
    return dictionary 

n = input("Enter sum: ")
n = float(n)

print (calculate_coins(n))
