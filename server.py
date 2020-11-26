import socket as so
import json

HOST, PORT = '', 3334

ls_socket = so.socket(so.AF_INET, so.SOCK_STREAM)
ls_socket.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, 1)
ls_socket.bind((HOST, PORT))
ls_socket.listen(1)

print(f'Serving HTTP on port {PORT} ...')

while True:
    client_connection, client_address = ls_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))
    
    obj = json.dumps({
        "name": "Leandro",
        "email": "leandro@email.com"
    })

    http_response = f"""\
HTTP/1.1 200 OK

{obj}
    """

    client_connection.sendall(bytes(http_response, 'ASCII'))
    client_connection.close()

