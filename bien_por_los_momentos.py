from Hyperlib_v1_6 import *
import Hyperlib_v1_6 as lib
from pybricks.parameters import Stop as PBStop
from pybricks.tools import wait

PINZA_ABRIR   =  190
PINZA_CERRAR  =  15
PINZA_VEL     =  400
PinzaMotor = Motor(Port.F)
_pinza_abierta = False


async def abrirpinza(angulo=PINZA_ABRIR, velocidad=PINZA_VEL):
    """Gira el motor F para ABRIR la pinza (hacia la izquierda)."""
    await PinzaMotor.run_target(velocidad, angulo, then=PBStop.HOLD)

async def cerrarpinza(angulo=PINZA_CERRAR, velocidad=PINZA_VEL):
    """Gira el motor F para CERRAR la pinza (hacia la derecha)."""
    await PinzaMotor.run_target(velocidad, angulo, then=PBStop.HOLD)


async def my_mission():
    await wait(13000)
    # 1. Prepara la IMU (el giroscopio)
    hub.imu.ready()
    hub.imu.reset_heading(0)
    # 2. Inicializa la odometría en la esquina (0,0) mirando a 0°
    await OdomIni(0, 0, 0)
    await abrirpinza()

    # 3. Avanza 500 mm en línea recta manteniendo el rumbo de 0°
    await MoveGyro(1300, 0, MaxSpeed=1000) #recta primera larga
    await TurnGyro(-90) 
    await MoveGyro(400, -90, MaxSpeed=1000) #recta 2
    await TurnGyro(-90)

    await MoveGyro(100, -180, MaxSpeed=1000)

    await TurnGyro(270)

    await MoveGyro(100, 270) #avanzar para agarrar

    await cerrarpinza()

    #llevar a lugar destino

    await MoveGyro(300, 270, Forward=False) #atras

    await TurnGyro(-180) #vuelta viendo hacia destino

    await MoveGyro(700, -180) #avanza recto

    await TurnGyro(-90)

    await MoveGyro(100, -90)

    await abrirpinza()

    await MoveGyro(1000, -90, Forward=False)

    await TurnGyro(0)

    await MoveGyro(352, 0, Forward=False)

    await cerrarpinza()

# Inicia la misión
run_task(my_mission())