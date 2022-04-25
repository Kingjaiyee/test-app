FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR .:usr/src/app

COPY requirements.txt ./

RUN if [[ -e requirements.txt ]]; then pip install -r requirements.txt && echo 'installation done'; fi

COPY . .

EXPOSE 8000
EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
