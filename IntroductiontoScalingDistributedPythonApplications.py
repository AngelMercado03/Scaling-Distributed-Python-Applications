import threading
import multiprocessing
import time

# Función para ejecutar en un hilo
def thread_function():
    print("Hilo ejecutando...")
    time.sleep(2)
    print("Hilo finalizado.")

# Función para ejecutar en un proceso
def process_function():
    print("Proceso ejecutando...")
    time.sleep(2)
    print("Proceso finalizado.")

if __name__ == "__main__":
    # Crear y ejecutar un hilo
    thread = threading.Thread(target=thread_function)
    thread.start()

    # Crear y ejecutar un proceso
    process = multiprocessing.Process(target=process_function)
    process.start()

    # Crear y ejecutar un demonio
    def daemon_function():
        print("Demonio ejecutando...")
        time.sleep(2)
        print("Demonio finalizado.")

    daemon_thread = threading.Thread(target=daemon_function)
    daemon_thread.daemon = True
    daemon_thread.start()

    print("Programa principal finalizado.")
