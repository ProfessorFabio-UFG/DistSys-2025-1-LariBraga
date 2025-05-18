import zmq, time
import random
from constPS import * #-

def calcula(): # realiza uma conta aleátoria de soma, subtração ou multiplicação
	op = random.randint(0,2)
	num1 = random.randint(0,20)
	num2 = random.randint(0,20)

	if op == 0:
		op_sinal = " + "
		res = num1 + num2
	elif op == 1:
		op_sinal = " - "
		res = num1 - num2
	else:
		op_sinal = " * "
		res = num1 * num2
	
	return str(num1) + op_sinal + str(num2) + " = " + str(res)


context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+HOST+":"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
	time.sleep(5)                    # wait every 5 seconds
	msg1 = str.encode("TIME " + time.asctime())
	s.send(msg1) # publish the current time
	msg2 = str.encode("CONTA " + calcula())
	s.send(msg2) # publish a calculation of sum, subtration or multiplication
