def loss_or_profit(income, outcome):
    a = sum(income)-sum(outcome)
    if a > 0:
        return "+" + str(a)
    elif a == 0:
        return "=" + str(a)
    else:
        return str(a)
