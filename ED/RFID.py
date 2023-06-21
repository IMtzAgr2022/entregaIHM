import RPi.GPIO as GPIO
import MFRC522
import time

#archivo = "pruebaUID.txt"

# signal

class RFID:
  """
  Clase utilizada para representar un lector RFID

  Atributos
    reader (MFRC522): Objeto utilizado para realizar la lectura
  """
#  archivo = "prueba.txt"
#  def agregar_cadena_al_archivo(cadena, archivo):
#    with open(archivo, 'a') as f:
#        f.write(cadena + "\n")


  def __init__(self):
    """
    Constructor por default
    """
    self.__reader = MFRC522.MFRC522()
    #self.__rst = rst
    #GPIO.setup(self.__rst,GPIO.OUT)
   # archivo = 'archivoUID.txt'

  def uidToString(self, uid):

    stringUID = ""

    for i in uid:
      stringUID = format(i, '02X') + stringUID

    return stringUID

  def read(self,rst):

    #print("Detectando tarjeta...")
    
    leyendo = True
#    GPIO.cleanup(rst)
    GPIO.setup(rst,GPIO.OUT)
    GPIO.output(rst,False)

    # Bandera de control de tiempo
    conTiempo = True

    # Obtener tiempo inicial
    tiempoInicial = time.time()

    # Mientras siga leyendo y no se pase tiempo limite
    while leyendo and conTiempo:

      # Obtener tiempo actual
      tiempoActual = time.time()

      # Si la diferencia de tiempo es mayor que el limite
      if ( abs(tiempoActual - tiempoInicial)>=5.0):

        # Establecer que se ha acabado el tiempo
        conTiempo = False
        print("Se ha acabado el tiempo")
        GPIO.output(rst,True)

      else:
     # print("111")
        # Escanear
        (status, TagType) = self.__reader.MFRC522_Request(self.__reader.PICC_REQIDL)
      #print("Escanear   ", status)
        # Si se detecta tarjeta
        if status == self.__reader.MI_OK:
          #print("      Detectado")
          # Obtener UID de la tarjeta
          (status, uid) = self.__reader.MFRC522_SelectTagSN()

          # Si se tiene el UID, continuar
          if status == self.__reader.MI_OK:
            #archivo = "pruebaUID.txt"
            print("UID de la tarjeta: %s" % self.uidToString(uid))
            cadena = self.uidToString(uid)
            with open("uid.txt","a") as archivo:
              archivo.write(self.uidToString(uid)+"\n")
            #agregarCadena(cadena,archivo)
            print(cadena)
            #print(archivo)
            #agregar_cadena_al_archivo(cadena, archivo)
            #with open('archivoUID.txt', 'w') as archivo:
            #archivo.write(cadena)
            # Aqui se desbloquearía la puerta y se checa lo de las camaras

            # Salir de lectura
            leyendo = False
            GPIO.output(rst,True)
#          GPIO.cleanup(rst)

          else:
            print("Error de autenticacion")

  # Check - Solo es un objeto para las dos RFID
