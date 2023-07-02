FROM python:3.9

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

COPY requirements.txt /app/

RUN pip install --upgrade pip  

RUN pip install -r requirements.txt  

COPY . . 

EXPOSE 8000  
 
CMD python manage.py runserver  