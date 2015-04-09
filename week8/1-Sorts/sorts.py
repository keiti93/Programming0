def min_index(arr): #Намира ИНДЕКСА, на който се намиранай-малкият елемент
    result = 0
    index = 0
    for x in arr:
        if x < arr[result]:
            result = index
        index += 1
    return result
 
def selection_sort_that_destroys(numbers): #Създава нов списък и изтрива стария
    result = []
    n = len(numbers)
    while len(result) != n:
        current_min_index = min_index(numbers)
        result.append(numbers[current_min_index])
        del numbers[current_min_index] #Изтрива всеки добавен елемент от стария списък
    return result
 
 
 
def swap(i, j, items): # Разменя местата на две стойности според индексите им
    temp = items[i]
    items[i] = items[j]
    items[j] = temp
     
def min_index_from(start_index, items): # Намира индекса на най-малкото число
    result = start_index                # от подаден индекс нататък
    n = len(items)
    for index in range(start_index, n):
        if items[index] < items[result]:
            result = index
        index += 1
    return result
 
def selection_sort_that_mutates(numbers): # пренаписва стария списък - мутира го
    n = len(numbers)
    for i in range(0, n):
        index_of_min_from_i = min_index_from(i, numbers)
        swap(i, index_of_min_from_i, numbers)
 

a = [100, 0, -10, 5]
 
print (a, selection_sort(a))
