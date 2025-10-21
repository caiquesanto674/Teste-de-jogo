# Dockerfile para rodar a simulação
FROM python:3.12-slim
WORKDIR /app
COPY . /app
# se houver requirements.txt: RUN pip install -r requirements.txt
CMD ["python", "-m", "src.main"]