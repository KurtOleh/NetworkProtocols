import socketserver

number = 1


class EchoUDPHandler(socketserver.BaseRequestHandler):

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

        data1, socket = self.request
        print('Connected address: {}'.format(self.client_address[0]))

        data = data1.decode()
        result = self.Mail(data)

        socket.sendto(result.encode(), self.client_address)


if __name__ == '__main__':
    try:
        with socketserver.UDPServer(('', 51000), EchoUDPHandler) as server:
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutdown")
