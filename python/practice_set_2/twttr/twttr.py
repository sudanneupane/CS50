def check_vowel(text):
    txt = text.lower()
    if txt=="a" or txt=="e" or txt=="i" or txt=="o" or txt=="u":
        return ""
    else:
        return text
def main():
    prompt = input("Input: ")
    out = ""
    for t in prompt:
        out = out + check_vowel(t)
    print(f"Output: {out}")

main()