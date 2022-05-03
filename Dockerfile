FROM python:3.8-alpine
RUN apk add gcc libc-dev libffi-dev

WORKDIR /app

COPY . .

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["python", "user_bots.py"]