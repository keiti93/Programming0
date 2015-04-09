def most_taken_row(cinema): # ред с най-малко свободни места
    taken = []
    
    for row in cinema:
        taken.append(sum(row))
        
    crowdest = min(taken)
    result = 0
    original = taken.index(crowdest)
    
    for index in range (0, len(taken)):
        if (taken[index]>crowdest):
            if (taken[index]!=len(cinema[0])):
                crowdest = taken[index]
                original = index
                result = index
            else:
                pass
        if taken[index]==crowdest:
            result = original
        
    return result
    
def free_seat(row): # първо свободно място на реда
    
    for index in range (0, len(row)):
        if row[index]==0:
            return index
        
    return False


def cinema_mutation(cinema): # МУТАЦИЯЯЯЯЯЯ!!!
    a = most_taken_row(cinema)
    b = free_seat(cinema[most_taken_row(cinema)])
    cinema[a][b]=1
    
    return (a+1, b+1)
        
def order_of_seats(cinema): # съществената част
    result = []
    
    for row in cinema:
        for seat in row:
            while sum(row)!= len(row):
                result.append(cinema_mutation(cinema))
                
    return result
        
cinema1 = [[1, 1, 1, 0], 
           [1, 0, 1, 0], 
           [0, 0, 0, 0]]

cinema2 = [[1, 1, 1],
           [1, 0, 0],
           [1, 0, 0],
           [1, 1, 0]]

cinema3 = [[0, 0],
           [0, 0],
           [0, 0]]

print(cinema1)
print(order_of_seats(cinema1))
print()
print(cinema2)
print(order_of_seats(cinema2))
print()
print(cinema3)
print(order_of_seats(cinema3))
