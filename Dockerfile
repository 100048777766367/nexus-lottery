FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY lottery/ ./lottery/
COPY synapses/ ./synapses/
COPY engine.py .

CMD ["python", "engine.py"]
