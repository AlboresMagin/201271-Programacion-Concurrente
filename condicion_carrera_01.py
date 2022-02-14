from random import random
import threading
import time
import random

class ConciertoBadBonny():
    def __init__(self, boletos = 0):
        self.locked = threading.Lock()
        self.ticket_send = boletos
        
    def incrementar(self):
        self.locked.acquire()
        
        try:
            self.ticket_send += 1
            print('Turno de compra de boleto: ',self.ticket_send)
        finally:
            self.locked.release()
            
def funcion_boletos(x):
    
    for y in range(6):
        time_f = random.random()
        time.sleep(time_f)
        x.incrementar()
        
if __name__ == '__main__':
    fila = ConciertoBadBonny()
    for y in range(6):
        tstart = threading.Thread(target=funcion_boletos, args=(fila,))
        tstart.start()