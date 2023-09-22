def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    l = len(s)
    check = 0
    i = 2
    if 2 <= l <=6:
        if "A" <= (s[0] and s[1]) <= "Z":
            for i in range(l):
                if ("A" <= s[i] <= "Z") and check == 0 :
                    check = 0
                elif "0" == s[i] and check == 0:
                    return False
                elif "0" <= s[i] <= "9":
                    check = 1
                else:
                    return False
            return True
    return False
main()