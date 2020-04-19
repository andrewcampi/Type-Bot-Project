import socket

def ip_address():
  hostname = socket.gethostname()    
  ip_address = socket.gethostbyname(hostname)     
    
  return "Your Computer's IP Address is " + str(ip_address)