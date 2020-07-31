import serial
import threading
import time

conectado = False
desligarArduino = False
contador = 0

# posso criar inputs para esses parâmetros
portaCOM = 'COM5'
velocidadeBaud = 115200

# Se isso for válido, entra aqui
try:
    # Comunicação com a serial
    serialArduino = serial.Serial(portaCOM, velocidadeBaud, timeout=0.2)
    print('Conectado!')

# Se não for válido, entra aqui
except:
    print('Verifique a porta serial do seu Arduino ou reconecte seu Arduino!')


# É necessario criar uma função pro Thread
def leitura_porta(serialArduino, conectado=None, desligarArduino=None):
    while not conectado:
        #global conectado

        conectado = True #False

        while True:
            reading = serialArduino.readLine().decode()

            if reading != "":  # Leitura diferente de vazio
                enviar(reading)

            if desligarArduino:
                print('Desligando Arduino')
                break


def enviar(reading):
    global contador
    print(f'Recebi {reading}')
    contador += 1


lerSerialThread = threading.Thread(target=leitura_porta, args=(serialArduino,))
lerSerialThread.start()

print('Preparando o Arduino')
time.sleep(2)
print('Arduino pronto!')

#Programa principal
while (True):
    try:
        print('Enviando')
        serialArduino.write('ligar lampada\n'.encode())
        time.sleep(2)

        print('Enviando')
        serialArduino.write('desligar lampada\n'.encode())
        time.sleep(2)

    except KeyboardInterrupt:
        # comando interrupção de teclado
        print('Apertou ctrl + C')
        desligarArduino = True
        serialArduino.close()
        lerSerialThread.join()
        conectado = False
        break
