import RPi.GPIO as GPIO
import time

class SensorUS:
  """
  Clase utilizada para representar un sensor ultrasonico

  Atributos:
    trigger (int): Pin asignado a terminal trigger
    echo (int): Pin asignado a terminal echo
  """

  # Constructor default
  def __init__(self, trigger = -1, echo = -1):
    """
    Constructor por default

    Parametros:
      trigger (int): Pin asignado a terminal trigger (default: -1) \n
      echo (int): Pin asignado a terminal echo (default: -1)

    Notas:
      El valor de los pines se determina por nombre y no por numero fisico
    """

    self.__trigger = trigger
    self.__echo = echo

  def getDistance(self):
    """
    Metodo para calcular distancia
    """

    # Si los valores de pines son adecuados
    if (self.__trigger > 0 and self.__echo > 0):

      # Set trigger to high
      GPIO.output(self.__trigger, True)

      # Set trigger after 0.01ms to low
      time.sleep(0.00001)
      GPIO.output(self.__trigger, False)

      StartTime = time.time()
      StopTime = time.time()

      # Save StartTime
      while GPIO.input(self.__echo) == 0:
        StartTime = time.time()

      # Set time of arrival
      while GPIO.input(self.__echo) == 1:
        StopTime = time.time()

      # Time difference between start and arrival
      TimeElapsed = StopTime - StartTime

      # multiply with the sonic speed (34300 cm/s)
      # and divide by 2, because there and back
      distance = (TimeElapsed * 34300) / 2

    else:
      distance = 100.0

    return distance

  def setup(self):
    """
    Metodo para establecer pines IN-OUT
    """

    if (self.__trigger > 0 and self.__echo > 0):
      GPIO.setup(self.__trigger, GPIO.OUT)
      GPIO.setup(self.__echo, GPIO.IN)
    else:
      raise ValueError("Los valores de los pines son incorrectos")

  # Ejecutar dos lecturas distance al mismo tiempo
  # Check - modulo multiprocessing
  # Agregar GPIO.setmode(GPIO.BCM)