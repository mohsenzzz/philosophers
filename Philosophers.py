from threading import Thread
lock_list= [True]*5
x=0

def increment():
    global x
    x=0
    for i in range(500):
        x+=1
    print(x)
class CustomThread(Thread):
    _tread_number =0
    def __init__(self):
        self.__class__._tread_number +=1
        self.tread_id = self.__class__._tread_number
        print(self.tread_id)
        Thread.__init__(self)

    def run(self):
        if lock_list[self.tread_id]:
            lock_list[self.tread_id] = False
            if self.tread_id != lock_list[-1] and lock_list[self.tread_id +1] :
                lock_list[self.tread_id+1] = False
                increment()
                print(f'thread {self.tread_id} is done')
                lock_list[self.tread_id] = True
                lock_list[self.tread_id+1] = True
            elif  self.tread_id == lock_list[-1] and lock_list[0] :
                lock_list[0] = False
                increment()
                print(f'thread {self.tread_id} is done')
                lock_list[self.tread_id] = True
                lock_list[0] = True
        else:
            return


if __name__ == '__main__':
    tread_list = list()
    for i in range(5):
        c = CustomThread()
        c.start()
        tread_list.append(c)
    for t in tread_list:
        t.join()


