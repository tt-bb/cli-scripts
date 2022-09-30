import calendar


def validation_year():
    year = input("Enter the desired year > ")
    while not year.isdigit():
        print("Enter a number!")
        year = input("> ")
    return int(year)


def validation_month():
    month = input("Enter the desired month > ")
    while (not month.isdigit()) or not (1 <= int(month) <= 12):
        print("Enter a number between 1 and 12")
        month = input("> ")
    return int(month)


if __name__ == "__main__":
    user_year = validation_year()
    user_month = validation_month()
    print(calendar.month(user_year, user_month))
