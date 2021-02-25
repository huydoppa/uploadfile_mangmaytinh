import socket
import tqdm
import os

SEPARATOR = "<1111>"
BUFFER_SIZE = 4096

host = socket.gethostbyname(socket.gethostname())
port = 50002

filename = "C:/Users/huy123/OneDrive/Desktop/network_ptit.pdf"

filesize =os.path.getsize(filename)

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")

s.connect((host,port))
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
def sendfile():
	progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
	with open(filename, "rb") as f:
		while True:
			bytes_read = f.read(BUFFER_SIZE)
			if not bytes_read:
				break

			s.sendall(bytes_read)
			progress.update(len(bytes_read))

sendfile()