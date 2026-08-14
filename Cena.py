import threads 
import time 

class Tenedor:
    def __init__(self, id):
        self.id = id
        self.lock = threading.Lock()


class Filosofo:
    def __init__(self, id, izquierdo, derecho):
        self.id = id
        self.izquierdo = izquierdo
        self.derecho = derecho

    def piensa(self):
        print(f"Esta pensando: {self.id} ")
        time.sleep(1)

    def come(self):
        with self.izquierdo.lock:
            print(f" {self.id} toma el tenedor {self.izquierdo.id}")

            with self.derecho.lock:
                print(f" {self.id} toma el tenedor {self.derecho.id}")
                print(f" {self.id} va a comer")
                time.sleep(1)

        print(f" {self.id} termino de comer")

    def run(self):
        for _ in range(3):
            self.think()
            self.eat()


#5 tenedores
Tenedor = 5
Filosofo = 5
threads = 5

for i in range(5):
    izquierdo = forks[i]
    derecho = forks[(i + 1) % 5]

    Filosofo = Filosofo(i, izquierdo, derecho)
    Filosofo.append(Filosofo)

for philosopher in philosophers:
    thread = threading.Thread(target=philosopher.run)
    threads.append(thread)

for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()

print("Todos los filósofos terminaron.")