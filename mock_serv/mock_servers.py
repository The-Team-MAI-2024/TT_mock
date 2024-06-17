# python mock_servers.py --num_servers 5 --start_port 5000 
# python mock_servers.py --num_servers 5 --start_port 5000 --min_response_time 1 --max_response_time 3
# python mock_servers.py --num_servers 5 --start_port 5000 --response_message "Hello from Mock Server"

# for check:
# curl http://127.0.0.1:5000/
# curl http://127.0.0.1:5001/
# curl http://127.0.0.1:5002/
# curl http://127.0.0.1:5003/
# curl http://127.0.0.1:5004/

# for closing ports:
# sudo netstat -tuln | grep 500
# sudo lsof -i :5000 
# sudo kill -9 <PID>

# docker build -t mock-servers .
# docker run -p 5000-5004:5000-5004 mock-servers

from multiprocessing import Process
import argparse
import os
import socket
import random

def run_server(port, server_number, response_time):

    # Проверка доступа к порту
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('0.0.0.0', port))
    if result == 0:
        print(f"Port {port} is already in use.")
        return
    sock.close()

    # Передача номера сервера и время отклика в качестве переменной окружения
    os.environ['SERVER_NUMBER'] = str(server_number)
    os.environ['RESPONSE_TIME'] = str(response_time)

    # Запуск Gunicorn
    os.system(f'gunicorn -w 1 -b 0.0.0.0:{port} wsgi:app')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate mock servers for load testing Nginx.')
    parser.add_argument('--num_servers', type=int, default=5, help='Number of mock servers to generate')
    parser.add_argument('--start_port', type=int, default=5000, help='Starting port number for mock servers')
    parser.add_argument('--min_response_time', type=float, default=0, help='Minimum response time for mock servers in seconds')
    parser.add_argument('--max_response_time', type=float, default=1, help='Maximum response time for mock servers in seconds')

    # Парсинг аргументов командной строки
    args = parser.parse_args()

    processes = []

    # Запуск процессов для создания моковых серверов
    for i in range(args.num_servers):
        port = args.start_port + i
        response_time = random.uniform(args.min_response_time, args.max_response_time)
        p = Process(target=run_server, args=(port, i, response_time))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
