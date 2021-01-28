FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD . /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
