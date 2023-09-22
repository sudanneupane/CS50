def main():
    in_time = input("Enter time:")
    out = convert(in_time)
    if 7.0 <= out <= 8.0:
        print("breakfast time")
    elif 12.0<= out <= 13.0:
        print("lunch time")
    elif 18.0 <= out <=19.0:
        print("dinner time")

def convert(time):
    hrs, minute = time.split(":")
    res = 0
    res = float(hrs)+float(minute)/60
    return res

if __name__ == "__main__":
    main()