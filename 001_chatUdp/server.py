from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024
HOST = "0.0.0.0"
PORT = 5000


def chatServer():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
            while True
                msg = s.recvfrom(BUFFER_SIZE)
                msg = msg[0].decode('UTF8')
                print(msg)



if __name__ == "__main__":
    chatServer()
