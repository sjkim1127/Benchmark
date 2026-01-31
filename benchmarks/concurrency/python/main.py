import asyncio

N_TASKS = 100000
counter = 0

async def task():
    global counter
    counter += 1

async def main():
    tasks = []
    for _ in range(N_TASKS):
        tasks.append(asyncio.create_task(task()))
    
    await asyncio.gather(*tasks)
    print(f"Done. Counter: {counter}")

if __name__ == "__main__":
    asyncio.run(main())
