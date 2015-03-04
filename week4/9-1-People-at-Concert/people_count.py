def get_people_count(activity):
    people = len(activity)
    count = 0
    new = [activity[0]]
    for person in activity:
        if person not in new:
            new = new + [person]
    return len(new)
