from time import *
import os
import subprocess

def main():
    os.chdir(r"C:\Users\Roma\Desktop\Lab4")
    time1 = time()
    for i in range(100):
        subprocess.Popen(['Python3', 'lab4.1.py'])
    time1 = time()-time1
    print("Среднее время выполнения первой программы:", round((time1*10), 2), 'миллисекунд')
    time2 = time()
    for i in range(100):
        subprocess.Popen(['Python3', 'lab4.2.py'])
    time2 = time()-time2
    print("Среднее время выполнения второй программы:", round((time2*10), 2), 'миллисекунд')
    time3 = time()
    for i in range(100):
        subprocess.Popen(['Python3', 'lab4.3.py'])
    time3 = time()-time3
    print("Среднее время выполнения третьей программы:", round((time3*10), 2), 'миллисекунд')

if __name__ == '__main__':
    main()