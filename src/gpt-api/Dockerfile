FROM python:3.12-slim

WORKDIR /gpt-api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "gpt-api.py"]
