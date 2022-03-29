#creo mi lista de jugadores
todosjugadores=[]
#menu del juego juego instanciado con jugador
def option(jugador):
    while True:
        print("______________________")
        print("|PACMAN-♜-IPC 1-♜-2022|")
        print("-----------------------")
        print("|1.      INICIAR JUEGO|")
        print("|2.   TABLA POSICIONES|")
        print("|3.              SALIR|")
        print("-----------------------")
        opcion = int(input("INGRESE UNA OPCION..."))
        if opcion ==1:
            juego(jugador)#llamando al metodo del juego
        elif opcion ==2:
            Position()#llamo las posiciones
        elif opcion ==3:
            break#se rompe el while
#Importaciones
from ast import And
from math import e
from pickle import TRUE
##Importaciones de Librerias
import random
from re import T
#Definimos la clase Alimento
class Alimento():
    #Se crea el encapsulamiento
    def __init__(self, posx, posy):
         self.posx = posx
         self.posy = posy                   
         self.isEat = False
    def getPosX(self):
        return self.posx
    def getPosY(self):
        return self.posy
    def isComido(self):
        return self.isEat
    def setPosY(self, _posy):
        self.posy = _posy
    def setPosX(self, _posx):
        self.posx = _posx
    def setEat(self):
        self.isEat = True
#Clase orientada al jugador
class Jugador():
    def __init__(self):
        self.nombre = ""
        self.posx = -1
        self.posy = -1
        self.puntos = 0
        self.movimientos = 0
    def getPosX(self):
        return self.posx
    def getPosY(self):
        return self.posy
    def getMovimientos(self):
        return self.movimientos
    def getPuntos(self):
        return self.puntos
    def setPosY(self, _posy):
        self.posy = _posy
    def setPosX(self, _posx):
        self.posx = _posx
    def addMovimiento(self):
        self.movimientos = self.movimientos + 1
    def addPuntos(self):
        self.puntos = self.puntos + 5
    def __gt__(self,x):#metodo para ordenamientos
        return self.movimientos > x.movimientos
#Funciones Utilizadas en el programa
def ImpresionDeTablero(tablero):#ImpresionDeTablero
    for fila in tablero:
        print("\t| {0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]} {0[9]} {0[10]} {0[11]} {0[12]} | ".format(fila))
def pintarTablero(lista_comida, jugador):
    tablero = [
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "]
    ]
    #Arreglo utilizado Para mostrar al jugador y comida
    for comida in lista_comida:
        if not comida.isComido():
            tablero[comida.getPosX()][comida.getPosY()] = "@"
    tablero[jugador.getPosX()][jugador.getPosY()] = "C"
    return tablero

def CrearComidas(lista_comida, comidas: int):
    indice = 0
    while indice< comidas:#mientras indice sea menor a comida se generan las comidas random
        #13 posiciones de las comidas
        posxcg = random.randint(0,12)
        posycg = random.randint(0,12)
        estaOcupado = False
        for comidas_busqueda in lista_comida:
            if comidas_busqueda.getPosX() == posxcg and comidas_busqueda.getPosY() == posycg:
                estaOcupado = True
        if not estaOcupado:
            comida_creada = Alimento(posxcg, posycg)
            lista_comida.append(comida_creada)
            indice = indice + 1

def siguienteHayComida(jugador, lista_comida):
    for comida in lista_comida:
        if jugador.getPosX() == comida.getPosX() and jugador.getPosY() == comida.getPosY():
            comida.setEat()
            jugador.addPuntos()
            return True
    return False

def aunHayComidas(lista_comiditas):
    for comida in lista_comiditas:
        if not comida.isComido():
            return False
    return True

def moverArriba(jugador,lista_comiditas):
    posx= jugador.getPosX()-1#filas
    posy= jugador.getPosY()#colummnas
    if posx >= 0:
        jugador.setPosX(int(posx))
        jugador.setPosY(int(posy))
        movimiento = siguienteHayComida(jugador, lista_comiditas)
        jugador.addMovimiento() 
def moverAbajo(jugador,lista_comiditas):
    posx= jugador.getPosX()+1#filas
    posy= jugador.getPosY()#columnas
    if posx <= 12:
        jugador.setPosX(int(posx))
        jugador.setPosY(int(posy))
        movimiento = siguienteHayComida(jugador, lista_comiditas)
        jugador.addMovimiento()   
def moverIzquierda(jugador,lista_comiditas):
    posx= jugador.getPosX()#filas 
    posy= jugador.getPosY()-1#columnas
    if posy >= 0:
        jugador.setPosX(int(posx))
        jugador.setPosY(int(posy))
        movimiento = siguienteHayComida(jugador, lista_comiditas)
        jugador.addMovimiento()  
def moverDerecha(jugador,lista_comiditas):
    posx= jugador.getPosX()#filas
    posy= jugador.getPosY()+1#columnas
    if posy <= 12 :
        jugador.setPosX(int(posx))
        jugador.setPosY(int(posy))
        movimiento = siguienteHayComida(jugador, lista_comiditas)
        jugador.addMovimiento()            
def movimientos(jugador, lista_comiditas):
#Mientras movimiento sea verdadero, se efectuaran los movimientos ASDW,aswd,4568
    while True:
        movimiento = input("Movimiento: ")
        if str(movimiento)=="w" or str(movimiento)=="8" or str(movimiento)=="W":
            moverArriba(jugador,lista_comiditas)
        if str(movimiento)=="s" or str(movimiento)=="5" or str(movimiento)=="S":
            moverAbajo(jugador,lista_comiditas)
        if str(movimiento)=="a" or str(movimiento)=="4" or str(movimiento)=="A":
            moverIzquierda(jugador,lista_comiditas)  
        if str(movimiento)=="d" or str(movimiento)=="6" or str(movimiento)=="D":
            moverDerecha(jugador,lista_comiditas)
        if str(movimiento)=="e":
            return option(jugador)
        print(" - JUGADOR:{0} - PUNTOS: {1} - MOVIMIENTOS: {2}".format(jugador.nombre, jugador.getPuntos(),jugador.getMovimientos()))
        tablero = pintarTablero(lista_comiditas, jugador)
        ImpresionDeTablero(tablero)
        if jugador.getPuntos() > 35 or aunHayComidas(lista_comiditas):
            auxilio= Jugador()
            auxilio.nombre = jugador.nombre
            auxilio.puntos = jugador.puntos
            auxilio.movimientos = jugador.movimientos
            todosjugadores.append(auxilio)
            jugador.nombre = ""
            jugador.puntos = 0
            jugador.movimientos = 0
            break    
#Generador de Posiciones Aleatorias de jugador
def PosicionAleJugador(jugador,lista_comiditas):
    while True:
        posx = random.randint(0,12)
        posy = random.randint(0,12)
        isOcupado = False
        for comida in lista_comiditas:
            try:
                if comida.posx== posx and comida.posy==posy:
                    isOcupado = True     
            except Exception as e:
                """"""
        if  not isOcupado:
            jugador.setPosX(posx)
            jugador.setPosY(posy)
            break;
#Acá se definen los 3 primeros lugares
def Position():
    todosjugadores.sort()
    if len(todosjugadores) == 1:
        print("1. {0} - MOVIMIENTOS:{1}  PUNTOS:{2} ".format(todosjugadores[0].nombre, str(todosjugadores[0].movimientos),str(todosjugadores[0].puntos)))
    elif len(todosjugadores) == 2:
        print("1. {0} - MOVIMIENTOS:{1}  PUNTOS:{2} ".format(todosjugadores[0].nombre, str(todosjugadores[0].movimientos),str(todosjugadores[0].puntos)))
        print("2. {0} - MOVIMIENTOS:{1}  PUNTOS:{2} ".format(todosjugadores[1].nombre, str(todosjugadores[1].movimientos),str(todosjugadores[1].puntos)))
    elif len(todosjugadores) == 3:
        print("1. {0} - MOVIMIENTOS:{1}  PUNTOS:{2} ".format(todosjugadores[0].nombre, str(todosjugadores[0].movimientos),str(todosjugadores[0].puntos)))
        print("2. {0} - MOVIMIENTOS:{1}  PUNTOS:{2} ".format(todosjugadores[1].nombre, str(todosjugadores[1].movimientos),str(todosjugadores[1].puntos)))
        print("2. {0} - MOVIMIENTOS:{1}  PUNTOS:{2} ".format(todosjugadores[2].nombre, str(todosjugadores[2].movimientos),str(todosjugadores[2].puntos)))
def juego(jugador):
    #Se definen las comidas
    nombre = input("Por favor escribe tu nombre: ")
    jugador.nombre=nombre
    alimento_pedido = random.randint(1,int((13*13)*0.4))
    lista_comiditas = []
    CrearComidas(lista_comiditas, alimento_pedido)
    PosicionAleJugador(jugador,lista_comiditas)
    #inicia el tablero
    tablero = pintarTablero(lista_comiditas, jugador)
    ImpresionDeTablero(tablero)
    ##Realización de juegos
    movimientos(jugador, lista_comiditas)
    #Se manda a llamar el menú 
jugador = Jugador()
option(jugador)
