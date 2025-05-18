import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages
s.setsockopt_string(zmq.SUBSCRIBE, "CONTA") # subscribe to CONTA messages

for i in range(5):  # Five iterations
	time = s.recv()   # receive a TIME's message
	print (bytes.decode(time))
	conta = s.recv() # receive a CONTA's message
	print(bytes.decode(conta))
	print("")
