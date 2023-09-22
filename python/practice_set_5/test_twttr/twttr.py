def main():
    prompt = input("Input: ")
    print(f"Output: {shorten(prompt)}")


def shorten(word):
    out = ""
    for t in word:
        out = out + check_vowel(t)
    return out

def check_vowel(text):
    txt = text.lower()
    if txt=="a" or txt=="e" or txt=="i" or txt=="o" or txt=="u":
        return ""
    else:
        return text


if __name__ == "__main__":
    main()