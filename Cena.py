




# hice esta version primero porque me entiendo mejor con python, ya despues busque la traduccion. 



import threading
import time
import random

N = 5


# clase 1
class Tenedor:
    def __init__(self, id):
        self.id = id
        self.lock = threading.Lock()


# clase 2
class Filosofo:
    def __init__(self, id, izquierdo, derecho):
        self.id = id
        self.izquierdo = izquierdo
        self.derecho = derecho

    def piensa(self):
        print(f"Filosofo {self.id} esta pensando")
        time.sleep(random.uniform(0.1, 0.5))

    def come(self):
        if self.id % 2 == 0:
            primero = self.izquierdo
            segundo = self.derecho
        else:
            primero = self.derecho
            segundo = self.izquierdo

        with primero.lock:
            print(
                f"Filosofo {self.id} toma "
                f"el tenedor {primero.id}"
            )

            with segundo.lock:
                print(
                    f"Filosofo {self.id} toma "
                    f"el tenedor {segundo.id}"
                )

                print(
                    f"Filosofo {self.id} esta comiendo"
                )

                time.sleep(random.uniform(0.1, 0.5))

        print(
            f"Filosofo {self.id} termino de comer"
        )

    def run(self):
        for _ in range(3):
            self.piensa()
            self.come()


# clase 3
class MainApplication:
    def __init__(self):
        self.tenedores = []
        self.filosofos = []
        self.threads = []

    def crear_tenedores(self):
        for i in range(N):
            tenedor = Tenedor(i)
            self.tenedores.append(tenedor)

    def crear_filosofos(self):
        for i in range(N):
            izquierdo = self.tenedores[i]
            derecho = self.tenedores[(i + 1) % N]

            filosofo = Filosofo(
                i,
                izquierdo,
                derecho
            )

            self.filosofos.append(filosofo)

    def crear_threads(self):
        for filosofo in self.filosofos:
            thread = threading.Thread(
                target=filosofo.run
            )

            self.threads.append(thread)

    def iniciar_threads(self):
        for thread in self.threads:
            thread.start()

    def esperar_threads(self):
        for thread in self.threads:
            thread.join()

    def ejecutar(self):
        print("Iniciando la cena de los filosofos...\n")

        self.crear_tenedores()
        self.crear_filosofos()
        self.crear_threads()
        self.iniciar_threads()
        self.esperar_threads()

        print("\nTodos los filosofos terminaron.")


# inicia
if __name__ == "__main__":
    app = MainApplication()
    app.ejecutar()