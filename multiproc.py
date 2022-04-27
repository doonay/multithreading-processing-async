import multiprocessing
import time
from random import randint
def countUp():
	i = 0
	while i <= 3:
		print('Up:\t{}'.format(i))
		time.sleep(randint(1,3))
		i+=1
def countDown():
	i = 3
	while i >= 0:
		print('Down:\t{}'.format(i))
		time.sleep(randint(1,3))
		i-=1
if __name__ == '__main__':
	#Инициализируем процессы
	workerUp = multiprocessing.Process(target=countUp)
	workerDown = multiprocessing.Process(target=countDown)
	#Запускаем процессы
	workerUp.start()
	workerDown.start()
	#Блокируем основной процесс
	workerUp.join()
	workerDown.join()