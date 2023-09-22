def main():
    while True:
        inp = input("Fraction: ")
        fuel_level = convert(inp)
        if fuel_level != None:
            break
    print(f"{gauge(fuel_level)}")


def convert(fraction):
    try:
        x,y = fraction.split("/")
        x , y = int(x) , int(y)
        fra = x/y
    except (ValueError, ZeroDivisionError):
        raise
    else:
        if x <= y:
            return int(round(fra*100, 0))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
