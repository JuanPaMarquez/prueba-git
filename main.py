import threading
import time

lista = [1, 2, 3]
continuar = True

def hilo1():
    print("\nEjecucion del hilo 1")
    time.sleep(1)
    lista.append(-1)
    print("impresion 1: ",lista)
    print("\nFinalizacion del hilo 1")

def hilo2():
    i = 0
    print("\nEjecucion del hilo 2")
    lista.append(-2)
    for num in lista:
        time.sleep(0.5)
        print("Hilo 2: Lista: ", num)
    while continuar:
        time.sleep(0.5)
        print(i)
        i += 1
    print("\nFinalizacion del hilo 2")

def hilo3():
    global continuar
    print("\nEjecucion del hilo 3")
    fin = int(input("\nHilo 3: (1) para True: \n"))
    if fin==1:
        continuar = False
    print("\nFinalizacion del hilo 3")

hilo1 = threading.Thread(target=hilo1)
hilo2 = threading.Thread(target=hilo2)
hilo3 = threading.Thread(target=hilo3)

hilo1.start()
hilo2.start()
hilo3.start()