import pygame
import random
import math
from pygame import mixer

# Iniciar pygame
pygame.init()

# Iniciar pantalla pygame
pantalla = pygame.display.set_mode((800, 600))

# Configurar juego - Título + icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

# Agregar música y sonidos
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.25)
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 530
jugador_x_cambio = 0

# Enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(20, 200))
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(30)

# Bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 530
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# Puntuacion
puntuacion = 0
fuente = pygame.font.Font('freesansbold.ttf', 25)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 50)
def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER MADAFAKA", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (90, 200))

# Funcion Para mostrar la puntuacion
def mostar_puntuacion(x, y):
    texto = fuente.render(f"SCORE: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# Funcion del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Funcion disparo
def disparo(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))  # Centra el disparo en la nave


# Funcion detectar colisiones
def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    pantalla.blit(fondo, (0, 0))  # Cambiar el fondo

    # Iterar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Evita el cierre del Loop (ventana avierta)
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:  # Genera los movimientos con las teclas
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.4
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.4
            if evento.key == pygame.K_SPACE:  # Genera el disparo
                sonido_disparo = mixer.Sound("disparo.mp3")
                sonido_disparo.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparo(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    jugador_x += jugador_x_cambio  # Lama al movimiento del jugador
    if jugador_x <= 0:  # Mantiene al jugador dentro de pantalla
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    for e in range(cantidad_enemigos):
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]  # Lama al movimiento del enemigo
        if enemigo_x[e] <= 0:  # Mantiene al enemigo dentro de pantalla
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        acierto = colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if acierto:  # Genera los aciertos de las balas
            sonico_acierto = mixer.Sound("Golpe.mp3")
            sonico_acierto.play()
            bala_y = 530
            bala_visible = False
            puntuacion += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(20, 200)
        enemigo(enemigo_x[e], enemigo_y[e], e)  # Lamamos al enemigo

    if bala_y <= -64:
        bala_y = 530
        bala_visible = False
    if bala_visible:  # Genera el disparo y su movimiento
        disparo(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)  # Llamamos a la funcion jugador
    mostar_puntuacion(texto_x, texto_y)
    pygame.display.update()  # Actualiza la pantalla
