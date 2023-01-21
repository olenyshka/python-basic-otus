FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /varapp

RUN pip install --upgrade pip
#RUN pip install poetry==1.2.2

#RUN pip install --ignore-installed uvicorn==0.20.0
# RUN poetry config virtualenvs.create false --local
COPY . .

#RUN poetry install --only main
# RUN pip freeze > requirements.txt

CMD uvicorn run homework_03.main:app --host 0.0.0.0 --port 8000
#CMD ["uvicorn", "homework_03.main:app", "--host", "0.0.0.0", "--port", "8000"]

