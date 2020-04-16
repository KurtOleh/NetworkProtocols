#!/usr/bin/python3
import socketserver

number = 1


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    @staticmethod
    def Mail(data_array):
        global number
        message = data_array.split('|')
        data_file = ""
        if message[0] == 'write':
            with open("TCP_Mail.txt", "a", encoding="utf-8") as file_write:
                file_write.write("{}\n".format(message[1]))

            print("Новое сообщение! ({})".format(number))
            number += 1
            return "Сообщение доставдено!"

        elif message[0] == 'bringout':
            index = 1
            with open("TCP_Mail.txt", "r", encoding="utf-8") as file_bringout:
                for line in file_bringout:
                    data_file += "{}. {}".format(index, line)
                    index += 1

            number = 1
            return data_file

        elif message[0] == 'delete':
            data_file = ""
            data = ""
            with open("TCP_Mail.txt", "r", encoding="utf-8") as file:
                for line in file:
                    data_file += line

                array_file = data_file.split('\n')

                for index, element in enumerate(array_file):
                    if index + 1 is int(message[1]):
                        array_file.remove(element)

                with open("TCP_Mail.txt", "w", encoding="utf-8") as file_delete:
                    for index, elem in enumerate(array_file):
                        if index == len(array_file) - 1:
                            file_delete.write("{}".format(data))
                        data += "{}\n".format(elem)

            return "Сообщение успешно удалено!"



    def handle(self):
        try:
            data1 = self.request.recv(1024).strip()
            data = data1.decode()
            print('Connect address: {}'.format(self.client_address[0]))

            result = self.Mail(data)

            self.request.sendall(result.encode())
        except ConnectionResetError:
            print("Сlient {} disconnected!".format(self.client_address[0]))


if __name__ == '__main__':
    try:
        with ThreadingTCPServer(('', 51000), EchoTCPHandler) as server:
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutdown")
