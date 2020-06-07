import socket, time, sys

class TimeServer():

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.test_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(('localhost', 123))
        self.server.settimeout(1)
        self.test_socket.settimeout(1)
        with open("time.txt", "rb") as f:
            self.time = int(f.readline())

    def take(self):
        data, address = self.server.recvfrom(512)
        if data:
            difference = time.time() - float(data)
            new_time = time.time() + self.time + difference
            self.server.sendto(bytes(time.ctime(new_time), encoding = "utf-8"), address)

    def check(self):
        data, _ = self.test_socket.recvfrom(512)
        print("Response: " + str(data))


if __name__ == '__main__':
    server = TimeServer()
    mode = input("Выберите режим работы: client - клиентский; server - серверный\n")
    try:
        if mode == "client":
            while True:
                input("Нажмите enter для отправки запроса")
                current_time = str(time.time()
                server.test_socket.sendto(bytes(current_time), encoding = "utf-8"), ('localhost', 123))
                server.take()
                server.check()
        elif mode == "server":
            while True:
                server.take()
        else:
            print("Что-то пошло не так, попробуйте заново")
    except Exception as e:
        print(e)
    finally:
        server.server.close()
        server.test_socket.close()
