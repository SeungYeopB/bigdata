def create_expense(date, coffee, traffic, bab):
    return {
        "date": date,
        "coffee": coffee,
        "traffic": traffic,
        "bab": bab
    }

def expense_get_sum(expense) :
    return expense["coffee"] + expense["traffic"] + expense["bab"]

def expense_to_string(expense) :
    return "{}\t {} \t {} \t {} \t {}".format(
        expense["date"],
        expense["coffee"],
        expense["traffic"],
        expense["bab"],
        expense_get_sum(expense))


expenses = [
    create_expense("3/1", 8700, 9800, 8800),
    create_expense("3/2", 5700, 9700, 6700),
    create_expense("3/3", 8700, 9800, 9800),
    create_expense("3/4", 5700, 9500, 6700),
    create_expense("3/5", 8700, 6800, 8800),
    create_expense("3/6", 5700, 9700, 6700),
    create_expense("3/7", 8300, 9800, 9800),
    create_expense("3/8", 5700, 9500, 9700)
]
print("일자 ", "음료    ", "교통   ", "식비   ", " 합계")
print("=====================================")
for expense in expenses:
    print(expense_to_string(expense))
print("=====================================")