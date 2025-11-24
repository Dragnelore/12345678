month = int(input("Сколько месяцев (n)? "))
kids = int(input("Сколько детей (k)? "))

def rabbits(month):
    if month == 1:
        return 1

    if month == 2:
        return 1

    return rabbits(month - 1) + kids * rabbits(month - 2)
print(rabbits(month))
