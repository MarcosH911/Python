class Years:
    def __init__(self):
        self.january = 31
        self.february = 28
        self.march = 31
        self.april = 30
        self.may = 31
        self.june = 30
        self.july = 31
        self.august = 31
        self.september = 30
        self.october = 31
        self.november = 30
        self.december = 31
        self.year = 1901
        self.sunday_count = 0
        self.days_sum = 2

    def check_february(self):
        if self.year % 100 == 0:
            if self.year % 400 == 0:
                self.february = 29
        elif self.year % 4 == 0:
            self.february = 29
        else:
            self.february = 28

    def is_sunday(self):
        if self.days_sum % 7 == 0:
            self.sunday_count += 1

    def add_month(self, month):
        self.days_sum += month


def main():
    years = Years()
    months = [years.january, years.february, years.march, years.april, years.may, years.june,
              years.july, years.august, years.september, years.october, years.november, years.december]
    while years.year <= 2000:
        years.check_february()

        for month in months:
            years.add_month(month)
            years.is_sunday()
        years.year += 1

    return years.sunday_count


print(main())
