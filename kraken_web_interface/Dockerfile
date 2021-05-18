FROM python:3.9
ENV PTYHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD uvicorn --host 0.0.0.0 --port 8000 --workers 1 kraken_web_interface.asgi:application