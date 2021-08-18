import os
def main():
    #escribe tu código abajo de esta línea
    os.system("clear")
    a = float(input("Dame el valor de a: "))
    b = float(input("Dame el valor de b: "))
    c = float(input("Dame el valor de c: "))
    
    d = float(input("Dame el valor de d: "))
    e = float(input("Dame el valor de e: "))
    f = float(input("Dame el valor de f: "))
    
    determinante = a*e - b*d

    if determinante == 0:
        print("El sistema no tiene solución.")
    else:
        x = (c*e - b*f)/determinante
        y = (a*f - c*d)/determinante
        print("La solución al sistema de ecuaciones es:")
        print(f"x={x}")
        print(f"y={y}")
    
if __name__=='__main__':
    main()
