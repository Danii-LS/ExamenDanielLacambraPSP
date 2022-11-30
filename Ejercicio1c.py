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
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        recogidaNums = []
        while True:
            for i in range(4):
                num = self.queue.get()
                recogidaNums.append(num)

            resultMcd = calculoMcd(recogidaNums)
            print('El MCD es %d . Sacado por %s' %(res, self.name))
            self.queue.task_done()
            time.sleep(10)       


    def calculoMcd(recogidaNums):
        res = recogidaNums[0]
        for i in range(4):
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
        




# relación productor:consumidor -> 2:10
def main():
    global queue
    queue = queue.Queue()
    p1 = Producer(queue)
    p2 = Producer(queue)

    c1 = Consumer(queue)
    c2 = Consumer(queue)
    c3 = Consumer(queue)
    c4 = Consumer(queue)
    c5 = Consumer(queue)
    c6 = Consumer(queue)
    c7 = Consumer(queue)
    c8 = Consumer(queue)
    c9 = Consumer(queue)
    c10 = Consumer(queue)

    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    c5.start()
    c6.start()
    c7.start()
    c8.start()
    c9.start()
    c10.start()

    
    p1.join()
    p2.join()
    c1.join()
    c2.join()
    c3.join()
    c4.join()
    c5.join()
    c6.join()
    c7.join()
    c8.join()
    c9.join()
    c10.join()


if __name__ == '__main__':
    main()