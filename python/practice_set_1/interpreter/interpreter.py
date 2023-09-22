inp = input("Expression:")
calc = inp.split()
a = float(calc[0])
b = float(calc[2])
res = 0
match calc[1]:
    case "+":
        res = a+b
    case "-":
        res = a-b
    case "*":
        res = a*b
    case "/":
        res = a/b

print(res)