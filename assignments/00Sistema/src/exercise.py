import os
def main():
    #escribe tu código abajo de esta línea
    os.system("clear")
    angulo = int(input("Dame el ángulo en grados: "))
    if angulo > 360:
        print("Error, el ángulo debe estar entre 0 y 360 grados")
    elif angulo > 180:
        print("Cóncavo")
    elif angulo == 180:
        print("Llano")
    elif angulo > 90:
        print("Obtuso")
    elif angulo == 90:
        print("Recto")
    elif angulo >= 0:
        print("Agudo")
    else:
        print("Error, el ángulo debe estar entre 0 y 360 grados")
    
if __name__=='__main__':
    main()
