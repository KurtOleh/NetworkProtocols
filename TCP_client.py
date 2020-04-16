# !/usr/bin/python3
import socket


def Mail():
    while True:
        try:
            command = str(input(
                "Что Вы хотите сделать (Введите соотвествующую команду)?\nwrite(написать сообщение)/bringout(вывести весь список сообщений)/delete(удалить сообщение)\n"))

            if command == 'write':
                message = str(input("Введите сообщение: "))
                return "{}|{}".format(command, message)

            elif command == 'bringout':
                return command

            elif command == 'delete':
                message = int(input("Введите id сообщения которое хотите удалить: "))
                return "{}|{}".format(command, message)

            else:
                print("Такой команды не существует, попробуйте еще раз\n")
        except ValueError:
            print("Неверный формат!")


while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.56.102', 51000))

        sock.send(Mail().encode())

        result = sock.recv(1024)

        print(result.decode())
        sock.close()

    except KeyboardInterrupt:
        print("\nShutdown")
        break