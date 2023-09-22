def name():
    nam = []
    while True:
        try:
            ad = input("Nane: ")
            nam.append(ad)
        except EOFError:
            return nam
def main():
    out = name()
    print(f"Adieu, adieu, to ", end = "")
    ln = len(out)
    if ln == 1:
        print(f"{out[0]}")
    elif ln == 2:
        print(f"{out[0]} and {out[1]}")
    else:
        for i  in range(ln):
            if (i+1) == ln:
                print(f"and {out[i]}")
            else:
                print(f"{out[i]}, ", end = "")
main()