from python:3.7.9-slim-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","generate.py"]
WORKDIR /app/output
ENTRYPOINT [ "python","serve.py" ]