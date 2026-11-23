#lightweight Python image
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app

#install the packages first, then copy in the app code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000
CMD ["python", "run.py"]
