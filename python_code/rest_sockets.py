"""#  Date & Time 24/05/2024, 01:59.
#  @author Mesfin Haftu
import socket

server_addr = input("What server do you want to connect? ")  # ask user web address
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket object with specified parameters
sock.connect((server_addr, 80))  # create a connection to the server with tuple of (web address, port)
# b stands for bytes because server accepts only bytes, the website sends the root "/" file
sock.send(b"GET / HTTP/1.1 \r\nHost: " +
          bytes(server_addr, "UTF-8") +
          b"Connection: close\r\n\r\n")
# bytes() change string server address to 0-255 by using utf-8 encoding
# \n\r is must be done at the end of line additional \r\n used for termination
reply = sock.recv(10000)  # up-to 10,000 bytes
sock.shutdown(socket.SHUT_RDWR)  # we are not going to read and write
sock.close()  # close connection
print(repr(reply))  # print reply in elegant format
# we can raise error named getaddressinfo() error socket.gaierror, socket.timeout,

"""
import sys
import socket

if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments: at least one is required" +
          "and not more than two are allowed:")
    print("- http server's address (required)")
    print("- port number (defaults to 80 if not specified)")
    exit(1)

addr = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) == 3:
    try:
        port = int(sys.argv[2])
        if not (1 <= port <= 65535):
            raise ValueError
    except ValueError:
        print("Port number is invalid - exiting.")
        exit(2)
else:
    port = 80

try:
    sock.connect((addr, port))
except socket.timeout:
    print("The server" + addr + "seems to be dead - sorry.")
    exit(3)
except socket.gaierror:
    print("Server address" + addr + "is invalid or malformed - sorry.")
    exit(4)

request = b"HEAD / HTTP/1.0\r\nHost: " + \
          bytes(addr, "utf8") + \
          b"\r\nConnection:close\r\n\r\n"

sock.send(request)
answer = sock.recv(100).decode("utf8")
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(answer[:answer.find('\r')])
