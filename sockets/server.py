import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)  # 1 - длина очереди

conn, addr = sock.accept()
print(f"connected {addr}")

while True:
    data = conn.recv(1024)  # 1024 - количество данных, получаемых за раз.
    if not data:
        break
    conn.send(data.upper())

conn.close()
