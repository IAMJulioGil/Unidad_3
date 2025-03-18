palabra_1= input("Ingresa la primera palabra:")
palabra_2= input("Ingresa la segunda palabra:")
if sorted(palabra_1.lower()) == sorted(palabra_2.lower()):
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")