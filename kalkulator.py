def kalkulator(angka1,angka2,operator) :
    if operator == '+':
        return angka1 + angka2
    elif operator == '-':
        return angka1 - angka2 
    elif operator == '*':
        return angka1 * angka2
    elif operator == '/':
        return angka1 / angka2
    

angka1 = int(input('masukan angka1 :'))
angka2 = int(input('masukan angka2 :'))
operator = input("masukan operator ('+','-','*','/')")

hasil = kalkulator(angka1, angka2, operator)
print(f"Hasilnya Adalah : {hasil}")