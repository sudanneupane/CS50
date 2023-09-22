def check(ch):
    res = "No"
    if(ch.strip()=="42" or ch.lower()== "forty two" or ch.lower() == "forty-two"):
        res = "Yes"
        return res
    else:
        res = "No"
        return res

def main():
    question = input("What is the answer to the Great Question of Life, the Universe and Everything?" )
    print(check(question))

main()