import socket
import threading


ip_server = ""
port = 12000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_server, port))
server.listen(5)
if len(ip_server) >= 1:
    print(f"[*] Server running!, listening on, {ip_server}:{port}")
else:
    ip_server = socket.gethostbyname(socket.gethostname())
    print(f"[*] Server running!, listening on", ip_server, ":", port)



# Function to print out Hostname and IP
def get_Host_name_IP():
    try:
        # Importing socket library
        # Function to display hostname and
        # IP address "Support windows and linux"
        host_name = socket.gethostname()
        x = socket.gethostbyname(host_name)
        x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        x.connect(('10.0.0.0', 0))
        host_ip = x.getsockname()[0]
        print("[*] Hostname:", host_name)
        print("[*] IP:", host_ip) #Share this IP with the client
        print("[*] Port:", port) #Share this port with the client
        
    except:
        print("[*] Unable to get Hostname and IP")



# Function to receive a message
def handle_rece_msg(server: socket.socket):
    while True:
        try:
            msg_rece = server.recv(4505)
            if msg_rece:
                print("[Client]: ", msg_rece.decode())
            else:
                server.close()
                break
            
        except Exception as e:
            print(f'[!] Error handling message from server: {e}')
            server.close()
            break



# Function to send a message
def handle_sent_msg(server: socket.socket):
    while True:
        try:
            msg_send  = input()
            if msg_send:
                server.send(msg_send.encode())
            else:
                server.close()
                break
            
        except Exception as e:
            print(f'[!] Error handling message from server: {e}')
            server.close()
            break        



# Function to handle threads
def server_thread():
        send = threading.Thread(target=handle_sent_msg, args=(client,))
        rece = threading.Thread(target=handle_rece_msg, args=(client,))
        send.start()
        rece.start()
        send.join()
        rece.join()
        
        
        
        
while True:
    get_Host_name_IP()
    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    print("[$] Chat started")
    try:
        server_thread()
        
    except:
        print("Error: {e}")
        server.close()
        break        
