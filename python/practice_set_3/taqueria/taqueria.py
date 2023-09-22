def main():
    bill_amt = 0
    while True:
        menu = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }
        try:
            prompt = menu[input("Item: ").title()]
        except KeyError:
            pass
        except EOFError:
            break
        else:
                sum = round(float(prompt), 2)
                bill_amt +=  sum
                print("Total: $%.2f" %(bill_amt))
    print()

main()

