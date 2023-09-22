def check_coin(c):
    if c == 5 or c == 10 or c == 25:
        return c
    else:
        return 0

def main():
    due = 50
    coin = 0
    owed = 0
    while True:
        if due <= 0:
            owed = - due
            break
        coin = check_coin(int(input(f"Amount Due: {due}\nInsert Coin: ")))
        due = due - coin

    print(f"Change Owed: {owed}")

main()

