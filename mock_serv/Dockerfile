FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /mock_serv

COPY requirements.txt /mock_serv/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /mock_serv/

EXPOSE 5000 5001 5002 5003 5004

CMD ["python", "mock_servers.py", "--num_servers", "5", "--start_port", "5000", "--min_response_time", "1", "--max_response_time", "3"]
