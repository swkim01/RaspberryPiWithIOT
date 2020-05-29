import asyncio
import sys

total = 0
async def add(id, delay):
    global total
    await asyncio.sleep(delay)
    total += delay
    print('add'+str(id)+':', total)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("run python3 addasyncio.py <num1> <num2>")
        sys.exit()
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    async def main():
        await add(1, n1)
        await add(2, n2)
        print('You waited '+str(total)+' seconds.')
    asyncio.run(main())

