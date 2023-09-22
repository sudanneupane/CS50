def main():
    text = input()
    print(convert(text))

def convert(message):
    message = message.replace(":)", "🙂")
    result_message = message.replace(":(", "🙁")
    return result_message

main()

