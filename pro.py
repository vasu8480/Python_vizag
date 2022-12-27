import socket
host = input('Enter the site name without http/https or IP address: ')
print ("Wait, there is a port scan!")

for port in range(1,65536):
    s = socket.socket()
   # Setting the timeout to one second
    s.settimeout(1)
    try:
        s.connect((host, port))
# If the connection caused an error
    except socket.error:
 # then we don't do anything
        pass
    else:
        print(f"{host}: {port} port is active")
  # Closing the connection
        s.close
print ("The scan is complete!")
