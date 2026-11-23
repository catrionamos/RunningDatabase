#use an official lightweight Python image
FROM python:3.12-slim

#prevent Python from buffering stdout/stderr (helps logs show up in Windows terminal)
ENV PYTHONUNBUFFERED=1

#set the working folder inside the container
WORKDIR /app

#copy and install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy the rest of the Flask application code
COPY . .

#expose port 5000 for Flask
EXPOSE 5000

#run the application
CMD ["python", "run.py"]
