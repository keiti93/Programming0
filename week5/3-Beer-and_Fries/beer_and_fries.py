def max_score(beers, fries):

    beers = sorted(beers)
    fries = sorted(fries)
    score = 0
    
    for i in range (0, len(beers)):
        score = score + beers[i]*fries[i]
        
    return score
