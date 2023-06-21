# https://pinout.xyz/pinout/pin12_gpio18

# Core
import RPi.GPIO as GPIO
import time
import mysql.connector

# Clases
from SensorUS import SensorUS
from RFID import RFID

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Sensores - # Dar nombres entrada/salida
sensor1 = SensorUS(18, 24)
sensor1.setup()

sensor2 = SensorUS(19,26) # Check valores de pines
sensor2.setup() # Setup no acepta valores de pines por default

#cadena = ""
#archivo = "pruebaUID.txt"
#Pines RST
#GPIO.setup(25,GPIO.OUT)
#GPIO.setup(23,GPIO.OUT)

#pines = [23,25]
#GPIO.cleanup(pines)
#GPIO.setup(pines,GPIO.OUT)

#Tarjetas apagadas
#GPIO.output(25,True)
#GPIO.output(23,True)

# RFID
#lector = RFID()
#lector2 = RFID(25)

def leer(pin):
  lector = RFID()
#  print("Pin de lectura numero: ",pin)
  lector.read(pin)

#def agregar_cadena_al_archivo(cadena, archivo):
#    with open(archivo, 'a') as f:
#        f.write(cadena + "\n")



# Ciclo
try:


  while True:

#    GPIO.output(25,True)
#    GPIO.output(23,True)

    # Obtener distancias
    distancia1 = sensor1.getDistance()
#    print ("Distancia del sensor ultrasonico 2 = %.1f cm" % distancia1)
    distancia2 = sensor2.getDistance()
 #   print ("Distancia del sensor ultrasonico 1 = %.1f cm" % distancia2)


    # Para sensor 1 (ultrasonico abajo - RFID arriba pin 22 físico)
    if (distancia1 <= 5.0) or (distancia2 <= 5.0):
#Encender tarjeta
#      GPIO.output(23,True)
#      GPIO.output(25,False)
      #GPIO.output(23,True)
      # Leer tarjeta
      pin = 0
      if (distancia1 <= 5.0):
        pin = 25
       # print("Sensor ultrasonico 2 - RFID 2")
      else:
        pin = 23
       # print("Sensor ultrasonico 1 - RFID 1")
#      GPIO.output(25,GPIO.HIGH)
 #     GPIO.output(25,GPIO.LOW)
     # lector.read(pin)
      print("Detectado cuerpo cercano")
      leer(pin)
#      archivo = "prueba.txt"
#      agregar_cadena_al_archivo(cadena, archivo)

#agregar codigo



      #print("Soy el pin", pin)
  #    GPIO.output(25,GPIO.HIGH)
#      GPIO.output(23,True)
      #GPIO.output(23,True)
#      GPIO.output(25,True)
  #    distancia2 = 100.0


    # Para sensor 2
#    if distancia2 <= 5.0:
      #GPIO.output(25,True)
      #GPIO.output(23,False)
      #GPIO.output(25,True)
 #     print("Sensor 2 leyendo")
# Leer tarjeta
   #   GPIO.output(23,GPIO.HIGH)
    #  GPIO.output(23,GPIO.LOW)
  
#    lector.read(23)
     # GPIO.output(23,GPIO.HIGH)

     # lector2.read()
      #GPIO.output(25,True)
      #GPIO.output(23,True)
    # Delay
    time.sleep(1)

except KeyboardInterrupt:

  print('Ejecucion detenida por el usuario')
  GPIO.cleanup()
