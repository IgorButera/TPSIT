from socket import AF_INET, SOCK_DGRAM, socket
from server import PORT

IP = str(input("inserisci l'indirizzo IP: "))
Utente = str(input("inserisci nome utente "))


def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            msg = input("inserisci un messaggio: ")
            msg = msg.encode('UTF8')
            s.sendto(msg, (IP, PORT))

if __name__ == "__main__":
    chatClient()
    
