# import multiprocessing as mp
# import time

# def worker():
#     proc = mp.current_process()
#     print(proc.name)
#     print(proc.pid)
#     time.sleep(5)
#     print("SubProcess End")


# if __name__ == "__main__":
#     proc = mp.current_process()
#     print(proc.name)
#     print(proc.pid)

#     # process spawning
#     p = mp.Process(name="SubProcess", target=worker)
#     p.start()

#     print("MainProcess End")

from multiprocessing import Pool


def work(x):
    print(x)


if __name__ == "__main__":
    pool = Pool(4)
    data = range(1, 100)
    pool.map(work, data)