import socket


IP = "0.0.0.0"
PORT = 5004
#BUFF = 65507
BUFF = 1
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

counter = 0


def read_and_print_on_console():
    #data, from_ = socket.recvfrom(BUFF)
    socket.recv(BUFF)
    #print("This IP {} sends you: {}. The size is {}".format(
    #    from_[0], data, len(data))
    #)



try:
    while True:
        #print("{}: ".format(counter), end="")
        read_and_print_on_console()
        counter += 1
except KeyboardInterrupt:
    print("Thank you for sending me {} messages".format(counter))

