import socket
from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler, ThreadingTCPServer


class EchoHandler(StreamRequestHandler):
    """
    服务于客户端连接
    """
    timeout = 5
    rbufsize = -1
    wbufsize = 0
    disable_nagle_algorithm = False

    def handle(self) -> None:
        print('Got connection from', self.client_address)
        # while True:
        #     msg = self.request.recv(8192)
        #     if not msg:
        #         break
        #     self.request.send(msg)
        try:
            for line in self.rfile:  # 给底层的socket加上了文件类型的接口
                self.wfile.write(line)
        except socket.timeout:
            print('Time out')


def echo_handler(address, client_sock):
    """
    服务端程序
    """
    print('Got connection from()'.format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()


def echo_server(address, backlog=5):
    sock = socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)


if __name__ == '__main__':
    # serv = TCPServer(('', 20000), EchoHandler)  # 单线程,一次只能处理一个客户端
    # serv = ThreadingTCPServer(('', 20000), EchoHandler)  # 多线程可能被黑客恶意攻击
    # from threading import Thread
    #
    # serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    # for n in range(16):
    #     t = Thread(target=serv.serve_forever)
    #     t.daemon = True
    #     t.start()
    # serv.serve_forever()
    # serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    # serv.socket.setsocket(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # serv.server_bind()
    # serv.server_activate()
    # serv.serve_forever()
    # 允许服务器重新对之前使用的端口号进行绑定
    # TCPServer.allow_reuse_address = True
    # serv = TCPServer(('', 20000), EchoHandler)
    # serv.serve_forever()

    echo_server(('', 20000))
