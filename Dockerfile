FROM python:3.8-alpine

RUN apk add --no-cache build-base libffi-dev

COPY . /app/
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt && chmod +x run_server.sh

# RUN job
EXPOSE 8000

ENTRYPOINT ["./run_server.sh"]