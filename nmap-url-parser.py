from bs4 import BeautifulSoup
import sys
print (sys.argv)

file = sys.argv[0]

with open(file, 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents)

for node in soup.findAll("host"):
    ports = []
    hostname = node.hostname["name"]

    for xmlport in node.findAll("port"):
        ports.append(xmlport["portid"])
        
    for port in ports:
        print("https://"+hostname+":"+port+"/")
        print("http://"+hostname+":"+port+"/")
