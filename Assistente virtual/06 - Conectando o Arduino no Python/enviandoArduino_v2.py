import serial
import threading
import time

conectado = False
desligarArduinoThread = False
mensagensRecebidas = 1
serialArduino = 0

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


def handle_data(data):
    global mensagensRecebidas

    print('Recebi ' + str(mensagensRecebidas) + ': ' + data)
    mensagensRecebidas += 1


# É necessario criar uma função pro Thread
def read_from_port(ser):
    global conectado, desligarArduinoThread

    while not conectado:
        conectado = True

        while True:
            reading = ser.readLine().decode()

            if reading != "":  # Leitura diferente de vazio
                handle_data(reading)

            if desligarArduinoThread:
                print('Desligando Arduino')
                break


lerSerialThread = threading.Thread(target=read_from_port, args=(serialArduino,))
lerSerialThread.start()

print('Preparando o Arduino')
time.sleep(2)
print('Arduino pronto!')

# Programa principal
while True:
    try:
        print('Enviando - Comandos de acionamento')
        serialArduino.write('ligar\n'.encode())
        time.sleep(2)

        print('Enviando - Comandos de desacionamento')
        serialArduino.write('desligar\n'.encode())
        time.sleep(2)

    except KeyboardInterrupt:
        # comando interrupção de teclado
        print('Apertou ctrl + C')
        desligarArduinoThread = True
        serialArduino.close()
        lerSerialThread.join()
        conectado = False
        break