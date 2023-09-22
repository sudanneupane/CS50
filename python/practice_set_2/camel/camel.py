def snake_case_converter(text):
    res = ""
    for s in text:
        if "A" <= s <= "Z":
            res = res + "_" + s.lower()
        else:
            res = res + s
    return res

def main():
    camelCase = input("Enter camel cast text: ")
    print(snake_case_converter(camelCase))

main()