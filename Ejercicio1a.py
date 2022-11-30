import threading
import time
import random
import queue

# Productor Consumidor mediante cola sincronizada tal que:

# Productor produce números mayor que 10 y menor que 1000
# Produce 10 numeros cada vez que los almacena en cola
# tiempo de espera entre la generacion de un num y otro es 1 segundo 

class Producer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        listaNums = []
        while True:
            for i in range(3):
                numero = random.randint(10, 1000)
                listaNums.append(numero)
    
            for i in range(3):
                self.queue.put(listaNums[i])
                print('%d metido en cola por %s' %(listaNums[i], self.name))

            time.sleep(4)



# consumer: lee 3 numeros de la cola de golpe y calcula el MCD
# tiempo espera: entre lectura de 3 elementos de la cola y la siguiente lectura de los siguientes 3 elementos es de 4 segundos
class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
        
    def calculoMcd(self, recogidaNums):
        resultado = recogidaNums[0]
        for i in range(3):
            resultado = mcd(recogidaNums[i], resultado)
            if resultado == 1:
                return 1
        return resultado

    def mcd(n1,n2):
        if n1<n2:
            i=n1
        else:
            i=n2
        while not (n1 % i == 0 and n2 % i == 0):
            i -= 1
        else:
            return i

    def run(self):
        recogidaNums = []
        while True:
            for i in range(3):
                num = self.queue.get()
                recogidaNums.append(num)

            resultMcd = calculoMcd(self, recogidaNums)
            print('El MCD es %s . Sacado por %d' %(resultMcd, self.name))
            self.queue.task_done()
            time.sleep(1)       # tiempo espera: 4 segundos




# relación productor:consumidor -> 1:1
def main():
    global queue
    queue = queue.Queue()
    p1 = Producer(queue)
    c1 = Consumer(queue)
    p1.start()
    c1.start()
    p1.join()
    c1.join()

if __name__ == '__main__':
    main()