def count_item(x, a):
    counter = 0
    for element in a:
        if element == x:
            counter += 1
    return counter

def forecast(days):
    sunshine = count_item ("sunshine", days)
    rain = count_item ("rain", days)
    snow = count_item ("snow", days)

    if (sunshine > rain + snow):
        return "sunshine"
    if (rain == snow) and (snow > sunshine):
        return "sunshine"
    if (rain > sunshine + snow):
        return "rain"
    if (sunshine == snow) and (snow > rain):
        return "rain"
    if (snow > sunshine + rain):
        return "snow"
    if (sunshine == rain) and (rain > snow):
        return "snow"
    
    return days[len(days) - 1]
    
