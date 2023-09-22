import sys
from tabulate import tabulate
import csv




def Tabulater(data):
    table = []
    try:
        with open(data) as inp:
            reader = csv.reader(inp)
            for row in reader:
                table.append(row)
            """
            # Just printing the result stored in table
            for count in table:
                print(count)

            # Directly reading the rows from the csv file often creates the problem where it does not
            # gives all the content as expected

            print(tabulate(reader, headers = "firstrow", tablefmt = "grid"))

            print(tabulate(table, headers="keys", tablefmt="grid"))     #using DictReader sometimes gave problem

            """
            print(tabulate(table[1:], headers = table[0], tablefmt = "grid"))


    except FileNotFoundError:
        sys.exit("File does not exist")




def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        print(Tabulater(sys.argv[1]))


if __name__ == "__main__":
    main()
    sys.exit()
