def check(greet):
    text = greet.lower().strip().split()
    if text[0].replace(",", "") == "hello":
        print("$0")
    elif text[0][0] ==  "h":
        print("$20")
    else:
        print("$100")

def main():
    check(input("Greeting:"))

main()