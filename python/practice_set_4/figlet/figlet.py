import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    font =  figlet.getFonts()
    arg1 = ["-f", "-font"]
    if (len(sys.argv) == 1):
        f = random.choice(font)
    elif (len(sys.argv) == 3) and (sys.argv[1] in arg1) and (sys.argv[2] in font):
        f = sys.argv[2]
    else:
        print("Invalid usage")
        sys.exit(1)

    figlet.setFont(font=f)
    s = input("Input: ")
    print("Output: ")
    print(figlet.renderText(s))

main()