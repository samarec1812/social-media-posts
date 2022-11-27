FROM python:3.10.8

# Set the working directory to /app
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt
EXPOSE 5000 
CMD ["python", "main.py"]