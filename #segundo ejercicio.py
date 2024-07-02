#segundo ejercicio
import time
import os
import csv

time.sleep(1)
os.system("cls")
contador = True
bl = ("─" * 32)
error = "no es una opcion o error en su seleccion"
es_rutas_prede = "rutas predeterminadas"
es_rutas = (f"{es_rutas_prede} \n{bl}")
while contador == True:
    while contador == True:
        try:
            print(f"bienbenido al menu de rutas seleccione la opcion (0 para salir) \n{bl}")
            print("1) rutas predeterminadas \n2) rutas guardadas")
            eleguir = int(input("coloque la opcion aqui: "))
        except ValueError:
            print(error)
            time.sleep(1)
            os.system("cls")
            continue
        break
    print("espere...")
    time.sleep(1)
    os.system("cls")
    if eleguir == 1:
        while contador == True:
            try:
                print(es_rutas)
                print(f"0) salir \n1) parque acuatico OASIS \n2) fantasilandia \n3) DUOC san bernardo")
                eleguir = int(input("selecione la ruta aqui: "))
            except ValueError:
                print(error)
                time.sleep(1)
                os.system("cls")
                continue
            
            if eleguir == 1:
                parque_acuatico = ["a 100 metros gire a la derecha ╔═»", "luego siga recto por unos 1.5 kilometros ║", "tome la carretera central en la siguiente curva"]
                for i in parque_acuatico:
                    palabras = i.split()
                    mensaje = " ".join(palabras)
                    print(mensaje)
                    time.sleep(0.5)