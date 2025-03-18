numero = int(input("Ingresa un número: "))

if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            es_primo = False
            break
        i += 1
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")