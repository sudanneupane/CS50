import re
def date_formatter(prompt):
    while True:
        old_date = input(prompt).strip()
        month = ["January","February","March","April","May","June","July",
                 "August","September","October","November", "December"]
        try:
            mon, day, year = re.split(" |/", old_date)
            mon = mon.strip()
            day = int(day.strip().replace(",", ""))
            year= year.strip()
        except ValueError:
            pass
        else:
            check_for = mon+" "+str(day)+", "+year
            if (mon.title() in month) and (old_date.title()==check_for ):
                mon = month.index(mon.title()) + 1
            try:
                if day < 31 and int(mon) <= 12:
                    return (f"{year}-{int(mon):02d}-{int(day):02d}")
            except:
                pass
def main():
    print(date_formatter("Date: "))

main()

