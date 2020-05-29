from threading import Thread
import sys

total = 0
def sum(n):
    global total
    for i in range(n+1):
        total += i

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("run python3 sumthread.py <num>")
        sys.exit()
    n = int(sys.argv[1])
    t = Thread(target=sum, args=(n,))
    t.start()
    print('sum='+str(total))
    t.join()
