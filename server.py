import socket
import tqdm
import os

SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 50002
SEPARATOR = "<1111>"
BUFFER_SIZE = 4096

s= socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
conn, addr = s.accept()
print(f"[+] {addr} is connected.")

received = conn.recv(BUFFER_SIZE).decode()
print(received)
filename, filesize = received.split(SEPARATOR)

filename = os.path.basename(filename)

filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open("C:/Users/huy123/OneDrive/Desktop/file_server/"+filename,"wb") as f:
	while True:
		bytes_read = conn.recv(BUFFER_SIZE)
		if not bytes_read:
			break
		f.write(bytes_read)
		progress.update(len(bytes_read))

conn.close()
s.close()