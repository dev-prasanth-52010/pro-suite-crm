FROM python:3.12

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1



RUN pip install --upgrade pip


COPY reqs.txt /app/


RUN pip install --no-cache-dir -r reqs.txt


COPY . /app/


EXPOSE 8000


CMD ["uvicorn", "core.asgi:application", "--host", "0.0.0.0", "--port", "8000"]