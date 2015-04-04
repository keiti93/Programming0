surname_husband = input("Husband's name: ")
surname_wife = input("Wife's name: ")

def taken_name(surname_husband, surname_wife):
    if surname_husband in surname_wife:
        return True
    else:
        return False
    
print(taken_name(surname_husband, surname_wife))
