import asyncio
import sys

total = 0
async def add(id, delay):
    global total
    for i in range(delay):
        await asyncio.sleep(1)
        print('add'+str(id)+':', i+1)
    total = delay

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("run python3 addasynctask.py <num1> <num2>")
        sys.exit()
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    async def main():
        await asyncio.gather(add(1, n1), add(2, n2))
        print('You waited '+str(total)+' seconds.')
    asyncio.run(main())

