FROM python:3.9-slim

ARG start_port=5000
ARG end_port=5004
ARG num_servers=5
ARG min_response_time=1
ARG max_response_time=3

ENV PYTHONUNBUFFERED 1

WORKDIR /mock_serv

COPY requirements.txt /mock_serv/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /mock_serv/

EXPOSE ${start_port}-${end_port}

CMD ["python", "mock_servers.py", "--num_servers", "${num_servers}", "--start_port", "${start_port}", "--min_response_time", "${min_response_time}", "--max_response_time", "${max_response_time}"]
