# multithreading

import threading
import time

lock = threading.Lock()

with lock:
	# TODO
	# will release lock after finish code block
    pass

class Thread(threading.Thread):
	def __init__(self, target, *args):
		threading.Thread.__init__(self, target=target, args=args)
		self.start


count = 0
lock = threading.Lock()

def increase():
	global count
	with lock:
		print("Lock Acquired")
		count += 1
		time.sleep(2)

def bye():
	while count < 5:
		increase()

def hello():
	while count < 5:
		increase()


def main():
	h = Thread(hello)
	b = Thread(bye)


lock.acquire()
lock.release()