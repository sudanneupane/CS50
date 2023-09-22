import random
def main():
    lvl = get_level()
    point = generate_integer(lvl)
    print(f"Score: {point}")


def get_level():
    while True:
        try:
            levl = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= levl <=3:
                return levl


def generate_integer(level):
    if level == 1:
        low = 0
        high = 9
    elif level == 2:
        low = 10
        high = 99
    else:
        low = 100
        high = 999
    score = 0
    for _ in range(10):
        mis = 0
        x = random.randint(low, high)
        y = random.randint(low, high)
        add = x+y
        while mis < 3:
            res = int(input(f"{x} + {y} = "))
            if res == add:
                score += 1
                break
            else:
                print("EEE")
                mis += 1
                if mis == 3:
                    print(f"{x} + {y} = {add}")
    return score




if __name__ == "__main__":
    main()