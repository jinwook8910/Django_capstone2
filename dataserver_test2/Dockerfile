FROM python:3.9.7
RUN pip3 install django
RUN pip3 install django_extensions
RUN pip3 install kubernetes
WORKDIR /usr/src/app
COPY . .
WORKDIR .
CMD ["python3", "manage.py", "runserver", "0:8000"]
EXPOSE 8000
