limite= int(input("Ingresa un número limite para tu serie de fibonacci: "))
a, b= 0, 1

print("Serie de Fibonacci hasta" , limite, ":")
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b