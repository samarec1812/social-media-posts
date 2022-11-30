FROM python:3.10.8

# Set the working directory to /app
WORKDIR /app
COPY ./ ./

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=main.py

CMD ["flask", "run"]