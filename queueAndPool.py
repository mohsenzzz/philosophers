from multiprocessing import Pool
from queue import Queue


def square(x):
    while True:
        number = q.get()
        print(number*number)
        if q.empty():
            break



q=Queue()



if __name__ == '__main__':
    for i in range(20):
        q.put(i)

    with Pool(4) as p:
        results = p.map(square,range(20))
    print(results)