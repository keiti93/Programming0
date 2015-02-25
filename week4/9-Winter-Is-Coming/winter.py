def winter_is_coming(seasons):
    counter = 0
    for season in seasons:
        if season == "spring" or season == "summer":
            counter += 1

        else:
            counter = 0
            
    return counter >= 5
