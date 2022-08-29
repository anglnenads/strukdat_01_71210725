while True:
    n = input("Masukkan perhitungan : ")
        
    n = n.split()
    if n[0] == "Q":
        break
    elif n[1] == "+":
        print(int(n[0]) + int(n[2]))
    elif n[1] == "-":
        print(int(n[0]) - int(n[2]))
    elif n[1] == "/":
        print(int(n[0]) / int(n[2]))
    elif n[1] == "*":
        print(int(n[0]) * int(n[2]))