FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt update && apt install wkhtmltopdf -y
RUN pip install -r requirements.txt
COPY . /code/