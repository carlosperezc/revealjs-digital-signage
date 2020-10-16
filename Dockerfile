from python:3.7.9-slim-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","generate.py"]