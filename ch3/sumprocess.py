from multiprocessing import Process, Pipe
import sys

def sum(n, conn):
    total = 0
    for i in range(n+1):
        total += i
    conn.send(total)
    conn.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("run python3 sumprocess.py <num>")
        sys.exit()
    n = int(sys.argv[1])
    parent_conn, child_conn = Pipe()
    p = Process(target=sum, args=(n, child_conn))
    p.start()
    print('sum='+str(parent_conn.recv()))
    p.join()
