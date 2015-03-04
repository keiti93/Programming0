def on_budget(books, budget):
    books = sorted(books)
    price = 0
    new_books = {"books_on_budget": 0, "loan": 0}
    for book in books:
        if book < budget:
            budget = budget - book
            price += book
            new_books["books_on_budget"] += 1
            if budget <0:   
                new_books["loan"] = sum(books) - price - budget
        else:
            new_books["loan"] = sum(books) - budget
    return new_books
