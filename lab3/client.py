import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")
inp = input("enter an 'head' or 'tail': ")
while inp != "exit":
    if inp == "head":
        result = server.head()
        print(result)
    elif inp=="tail":
         result = server.tail()
         print(result)
    inp=input("enter an 'head'or 'tail': ")

result = server

