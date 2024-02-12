import threading
import time

mic = threading.Semaphore(1)  # Semáforo para controlar acceso al micrófono
numAsistentes = threading.Semaphore(0)  # Semáforo contador de asistentes que desean hablar
respuesta = threading.Semaphore(0)  # Semáforo para sincronizar la salida de los asistentes

def asistente(id):
    print(f"Asistente {id}: Esperando turno para hacer pregunta.")
    numAsistentes.release()  # El asistente indica que desea hablar
    mic.acquire()  # Espera hasta que pueda tener acceso al micrófono
    print(f"Asistente {id}: Haciendo pregunta.")
    # Simulación de hacer pregunta al orador
    time.sleep(1)
    print(f"Asistente {id}: Gracias, terminando.")
    mic.release()  # Libera el micrófono
    respuesta.release()  # Indica que ha hecho su pregunta y puede salir

def orador():
    while True:
        numAsistentes.acquire()  # Espera a que un asistente quiera hablar
        mic.acquire()  # Espera a que el micrófono esté disponible
        print("Orador: Respondiendo pregunta.")
        # Simulación de responder la pregunta
        time.sleep(1)
        print("Orador: Pregunta respondida.")
        mic.release()  # Libera el micrófono
        respuesta.acquire()  # Indica que ha respondido a la pregunta

# Creamos e iniciamos el thread del orador
thread_orador = threading.Thread(target=orador)
thread_orador.start()

# Creamos e iniciamos los threads de los asistentes
num_asistentes = 5  # Número de asistentes
threads_asistentes = []
for i in range(num_asistentes):
    thread_asistente = threading.Thread(target=asistente, args=(i+1,))
    threads_asistentes.append(thread_asistente)
    thread_asistente.start()

# Esperamos a que todos los asistentes terminen
for thread in threads_asistentes:
    thread.join()

# Esperamos a que el thread del orador termine
thread_orador.join()

print("Sesión de preguntas y respuestas terminada.")
