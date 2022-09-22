# FLOW
# x >> integer
# y >> +, -, *, or /
# z >> integer


txt = input("write: ")

x, y, z = txt.split(" ")
x = float(x)
z = float(z)
match y :
    case "*":
        print(round(x*z,1))
    case "+":
        print(round(x+z,1))
    case "-":
        print(round(x-z,1))
    case "/":
        print(round(x/z,1))
    case _ :
        print("error404")