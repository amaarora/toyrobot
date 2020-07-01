FROM python:3.6-stretch
COPY . /code
WORKDIR /code
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile