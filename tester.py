import pytest
import socket
import sys

s = socket.socket()
s.bind(('', 9876))
s.listen()

print("Listening on port 9876")

(client, addr) = s.accept()
key = client.recv(6)
print("Received %s" % (key))

clientF = client.makefile("w")
_stdout = sys.stdout
sys.stdout = clientF

pytest.main(["--color=yes"])

print("%s" % (key))

clientF.close()
client.shutdown(socket.SHUT_RDWR)
client.close()
s.shutdown(socket.SHUT_RDWR)
s.close()

