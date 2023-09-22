import sys
import csv
table = []
def scourgify(readingFile, writingFile):
    try:
        with open(readingFile) as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                table.append(row)

        with open(writingFile, "w") as writefile:
            headername = ["first", "last", "house"]
            writer = csv.DictWriter(writefile, fieldnames = headername )
            writer.writeheader()
            for addrow in table:
                last_name, first_name = addrow["name"].split(", ")
                writer.writerow({"first" : first_name, "last" : last_name, "house" : addrow["house"] })

    except FileNotFoundError:
        sys.exit(f"Could not read {readingFile}")



def main():
    leng = len(sys.argv[1:])
    if (leng < 2):
        sys.exit("Too few command-line arguments")
    elif (leng > 2):
        sys.exit("Too many command-line arguments")
    else:
        scourgify(sys.argv[1], sys.argv[2])



if __name__ == "__main__":
    main()
    sys.exit()