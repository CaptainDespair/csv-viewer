FROM python:3.9.13

ENV PYTHONUNBUFFERED 1

WORKDIR /test-task
COPY ./ ./
COPY requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
