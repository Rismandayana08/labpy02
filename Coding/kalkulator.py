def kalkulator(angka1,angka2,operator) :
    if operator == '+':
        return angka1 + angka2
    elif operator == '-':
        return angka1 - angka2 
    elif operator == '*':
        return angka1 * angka2
    elif operator == '/':
        return angka1 / angka2
    else:
        print("Input tidak valid")
        exit()

angka1 = int(input('masukan angka pertama :'))
angka2 = int(input('masukan angka kedua :'))
operator = input("masukan operator ('+','-','*','/')")

hasil = kalkulator(angka1, angka2, operator)
print(f"Hasilnya Adalah : {hasil}")