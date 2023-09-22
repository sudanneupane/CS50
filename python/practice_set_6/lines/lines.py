import sys


def CountLinesInProgram(name):
    countLine = 0
    try:
        with open(f"{name}") as readFile:
            for line in readFile:
                if( line.strip() == "" or line.strip()[0] == "#" ):
                    countLine
                else:
                    countLine = countLine + 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return countLine

def main():
    if(len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")
    elif(sys.argv[1][-3:] != ".py"):
        sys.exit("Not a Python file")
    else:
        print(CountLinesInProgram(sys.argv[1]))

if __name__ == "__main__":
    main()