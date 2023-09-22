def main():
    val = value(input("Greeting:"))
    print(f"${val}")

def value(greeting):
    text = greeting.lower().strip().split()
    if text[0].replace(",", "") == "hello":
        return 0
    elif text[0][0] ==  "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()