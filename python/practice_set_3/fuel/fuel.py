def main():

    fuel_level = int(round(check_fuel("Fraction: "), 0))
    if fuel_level <= 1:
        print("E")
    elif fuel_level >= 99:
        print("F")
    else:
        print(f"{fuel_level}%")

def check_fuel(prompt):
    while True:
        fraction = input(prompt)
        try:
            x,y = fraction.split("/")
            x , y = int(x) , int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x <= y:
                return x/y*100

main()