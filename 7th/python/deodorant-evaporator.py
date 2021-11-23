def evaporator(content, evap_per_day, threshold):
    days = 0
    i = 100
    while i > threshold:
        i = i - i * evap_per_day/100
        days += 1
    return days
