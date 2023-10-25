# Empezar corriendo una imagen de python 
#FROM python:3.8-alpine
FROM public.ecr.aws/lambda/python:3.8

# Copiar requerimientos para ejecutar el programa
COPY ./requirements.txt /app/requirements.txt
COPY breaker/ /app/breaker/
COPY vistas/ /app/vistas/
COPY ./app.py /app/app.py
COPY ./__init__.py /app/__init__.py
# Cambiar de directorio de trabajo a donde esta el ejectuable del API
WORKDIR /app
# Instalar requerimientos de la app
RUN pip install -r requirements.txt
# Copiar el contenido del directorio actual en la imagen de docker
#COPY . /app
# Agregar variable de entorno con el nombre del estudiante
ENV CAND_BACK_URL http://127.0.0.1:5001
EXPOSE 5002
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5002"]