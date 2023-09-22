def main():
    dic = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        else:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
    mylist = list(dic.keys())
    mylist.sort()
    sorted_dictionary = {i: dic[i] for i in mylist}
    for j in sorted_dictionary:
        print(f"{sorted_dictionary[j]} {j}")

main()