import socket
s=socket.socket()
#print("Socket creation successfully")
def bind_socket():  #binding the socket
    host='125.0.0.1'
    port=9999
    try:
        s.bind((host,port))
        s.listen(5)
        print(f"socket bound to {host}:{port}")
    except socket.error as e:
        print("Error binding socket")
bind_socket()
#establish connection with a client (socket must be listening)
def socket_accept():
    try:
        conn,addr=s.accept()
        print("connection has been estalished |" + " IP {addr[0]}" + addr[1] + " | port" + str(addr[1]))
        s.send(b"Hello server,thank you.")
        conn.close()
    except socket.error as e:
        print(f"Error accepting connection: {e}")
       
socket_accept()