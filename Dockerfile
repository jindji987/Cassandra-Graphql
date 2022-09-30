FROM python:3.6
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]