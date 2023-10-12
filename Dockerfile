FROM python:3.11

WORKDIR /app

COPY . /app/

RUN pip install -r req.txt

RUN chmod 777 entrypoint.sh

#CMD ["python3", "manage.py", "migrate"]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]