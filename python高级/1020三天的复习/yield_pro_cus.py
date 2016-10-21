# coding=utf-8
# 这个主要是用协程来解决生产者消费者的问题
import time
def consumer():
	r = ''
	while True:
		n = yield r # 这 如果没有通过send() 这时候n 是null的
		if not n:
			return


		print('[CONSUMER] Consuming %s...' % n)
		time.sleep(1)
		r = "200 OK"
def produce(c):
	c.next() #当执行next()时 会返回yield 后面的是 并在下次next时执行下面语句
	n = 0
	while n < 5:
		n = n+1
		print('[PRODUCER] Producing %s...' % n)

		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' % r)


	c.close()



if __name__ == '__main__':
	c = consumer() #<generator object consumer at 0x7f5b3852af00>
	#他保存的 是一个生成器的地址
	#区别 c = consumer     <function consumer at 0x7facb8cee320> 她保存的是一个函数的地址



	print c
	produce(c)
