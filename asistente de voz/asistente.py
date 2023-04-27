import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escucha el microfono y devolver audio como texto
def transformar_audio_en_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:  # Configura el micro
        r.pause_threshold = 0.8  # Tiempo de espera
        print("Ya puedes hablar")  # Informa del comienzo de la grabacion
        audio = r.listen(origen)  # Graba el audio

        try:
            pedido = r.recognize_google(audio, language="es-es")
            print("Has dicho: " + pedido)
            return pedido
        except sr.UnknownValueError:
            print("Uupss, no te he entendido")
            return "sigo esperando"
        except sr.RequestError:
            print("Uupss, no hay servicio")
            return "sigo esperando"
        except:
            print("Uupss, algo no ha ido bien")
            return "sigo esperando"


# Función para que el asistente hable
def hablar(mensaje):
    engine = pyttsx3.init()  # Enciende el motor de pyttsx
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    print(dia_semana)

    semanario = {0: 'Lunes',
                 1: 'Martes',
                 2: 'Miércoles',
                 3: 'Jueves',
                 4: 'Viernes',
                 5: 'Sábado',
                 6: 'Domingo'}

    hablar(f"Hoy es {semanario[dia_semana]}")


def pedir_hora():
    hora = datetime.datetime.now()
    hora = f"Son las {hora.hour} horas {hora.minute} minutos y {hora.second} segundos"
    hablar(hora)


def saludo_inicial():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos dias'
    else:
        momento = 'Buenas tardes'

    hablar(f"{momento}, soy Nerueah, tu asistente personal. Por favor, ¿En que puedo ayudarte?")


# Función central del asistente
def pedir_cosas():
    saludo_inicial()
    comenzar = True
    while comenzar:
        pedido = transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar("Abriendo YouTube")
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar("Buscando informacion en wikipedia")
            pedido.replace(' busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('En wikipedia sale:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar("buscando en internet")
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif 'reproducir' in pedido:
            hablar("buscando en YouTube para reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f"El precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("lo siento, no lo he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("voy a sobarla y luego a dormir, sallonara madafaka.")
            break

pedir_cosas()