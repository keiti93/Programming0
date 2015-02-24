def hash_them(keys, values):
    hash_them = {}
    i = 0
    a = 1
    while a < len(keys):
        if len(values)<len(keys):
            values += ["None"]
        a += 1
            
    for key in keys:
        hash_them[key] = values[i]
        i += 1
    return hash_them

print (hash_them)
