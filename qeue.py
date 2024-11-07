import threading
import queue

class Email:
    def __init__(self):
        pass

    @classmethod
    def send_mail(cls,reciver):
        print(f'email sent to {reciver}')

reciver_list=['mohsen@gmail.com','ali@gmail.com','reza@yahoo.com']*10
q = queue.Queue()

for email in reciver_list:
    q.put(email)
def say_hello():
    while True:
        email_address= q.get()
        Email.send_mail(email_address)
        print(f'queue size is:\t{q.qsize()}')
        q.task_done()
        if q.empty():
            break




for i in range(4):
    t= threading.Thread(target=say_hello)
    t.start()



q.join()
print("finish!!!")