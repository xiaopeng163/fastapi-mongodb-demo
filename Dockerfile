FROM python:3.8-alpine

COPY . /app/
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt && chmod +x run_server.sh

# RUN job
EXPOSE 8000

ENTRYPOINT ["./run_server.sh"]