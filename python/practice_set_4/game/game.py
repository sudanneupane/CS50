import random
def get_level():
    while True:
        try:
            lvl= int(input("Level: ").strip())
            win = random.randint(1, lvl)
        except ValueError:
            pass
        else:
             guess(win)
def guess(guess_me):
    while True:
        try:
            gus = int(input("Guess: ").strip())
        except ValueError:
            pass
        else:
            if 0 < gus:
                if gus == guess_me:
                    print("Just right!")
                    exit()
                elif gus < guess_me:
                    print("Too small!")
                elif gus > guess_me:
                    print("Too Large!")

def main():
    get_level()

main()