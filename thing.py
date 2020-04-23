
num1 = float(input("Vul calorieen in"))
plusmin = input("plus of min?")
num2 = float(input("Vul tweede calorieen in"))

if plusmin == "+":
    print(num1 + num2)
elif plusmin == "-":
    print(num1 - num2)
else:
    print("error")