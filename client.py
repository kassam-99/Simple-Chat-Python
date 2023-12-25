import socket
import threading


ip = input("[*] Enter IP of server: ")
port = input("[*] Enter port of server: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))




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
        print("[*] IP:", host_ip)
        print("[*] Connected!")
        
    except:
        print("[!] Unable to get Hostname and IP")




def handle_rece_msg(client: socket.socket):
    while True:
        try:
            msg_rece = client.recv(4505)
            if msg_rece:
                print("[Server]: ",msg_rece.decode())
            else:
                client.close()
                break
            
        except Exception as e:
            print(f'[!] Error handling message from server: {e}')
            client.close()
            break




def handle_sent_msg(client: socket.socket):
    while True:
        try:
            msg_send  = input()
            if msg_send:
                client.send(msg_send.encode())
            else:
                client.close()
                break
            
        except Exception as e:
            print(f'[!] Error handling message from server: {e}')
            client.close()
            break   

    
    

def client_thread():
        send = threading.Thread(target=handle_sent_msg, args=(client,))
        rece = threading.Thread(target=handle_rece_msg, args=(client,))
        send.start()
        rece.start()
        send.join()
        rece.join()
        
        
        
        
while True:
    try:
        get_Host_name_IP()
        print("[$] Chat started")
        client_thread()
        
        
    except Exception as e:
        print(f'[!] Error handling message from server: 2{e}')
        client.close()
        break     
