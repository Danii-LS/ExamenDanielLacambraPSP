import threading
import time
import random
import queue


class Producer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        listaNums = []
        while True:
            for i in range(10):
                numero = random.randint(10, 1000)
                listaNums.append(numero)
    
            for i in range(10):
                self.queue.put(listaNums[i])
                print('%d metido en cola por %s' %(listaNums[i], self.name))
            listaNums=[]
            time.sleep(2)


class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        recogidaNums = []
        while True:
            for i in range(2):
                num = self.queue.get()
                recogidaNums.append(num)

            resultMcd = calculoMcd(recogidaNums)
            print('El MCD es %d . Sacado por %s' %(res, self.name))
            self.queue.task_done()
            time.sleep(4)       # tiempo espera: 4 segundos


    def calculoMcd(recogidaNums):
        res = recogidaNums[0]
        for i in range(2):
            res = mcd(recogidaNums[i], res)
            if(res == 1):
                return 1
        return res

    def mcd(n1,n2):
        if n1<n2:
            i = n1
        else: 
            i = n2
        while not (n1 % i == 0 and n2 % i == 0):
            i -= 1
        else:
            return i
        




# relación productor:consumidor -> 4:2
def main():
    global queue
    queue = queue.Queue()
    p1 = Producer(queue)
    p2 = Producer(queue)
    p3 = Producer(queue)
    p4 = Producer(queue)

    c1 = Consumer(queue)
    c2 = Consumer(queue)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    c1.join()
    c2.join()

if __name__ == '__main__':
    main()