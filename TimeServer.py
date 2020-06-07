import socket, time, sys

class TimeServer():

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.test_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(('localhost', 123))
        self.server.settimeout(0)
        self.test_socket.settimeout(0)
        with open("time.txt", "rb") as f:
            self.time = int(f.readline())

    def send(self):
        self.test_socket.sendto(bytes(str(time.time()), encoding = "utf-8"), ('localhost', 123))

    def take(self):
        data, addr = self.server.recvfrom(1024)
        if data:
            difference = time.time() - float(data)
            self.server.sendto(bytes(time.ctime(time.time() + self.time + difference), encoding = "utf-8"), addr)

    def check(self):
        data, addr = self.test_socket.recvfrom(1024)
        print("Response: " + str(data))


if __name__ == '__main__':
    timeServer = TimeServer()
    print("Выберите режим работы:")
    print("client - клиентский; server - серверный")
    t = input()
    try:
        if t == "client":
            while True:
                input("Нажмите enter для отправки запроса")
                timeServer.send()
                timeServer.take()
                timeServer.check()
        elif t == "server":
            while True:
                timeServer.take()
        else:
            print("Что-то пошло не так, попробуйте заново")
    except Exception as e:
        print(e)
    finally:
        timeServer.server.close()
        timeServer.test_socket.close()
        time.sleep(1)
        sys.exit(0)