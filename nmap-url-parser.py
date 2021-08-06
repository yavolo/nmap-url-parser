from bs4 import BeautifulSoup
import sys

file = sys.argv[1]
print(file)

with open(file, 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, features="lxml")

for node in soup.findAll("host"):
    ports = []
    hostname = node.hostname["name"]

    for xmlport in node.findAll("port"):
        ports.append(xmlport["portid"])

    for port in ports:
        print("https://"+hostname+":"+port+"/")
        print("http://"+hostname+":"+port+"/")
