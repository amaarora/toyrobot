FROM python:3.6-stretch

COPY . /code
WORKDIR /code
# RUN pip install pipenv
# RUN pipenv install 
RUN ls -l
RUN pip install .
RUN echo "Running Example:" && cat ./examples/example1.txt
RUN echo "Verbose output:" && toyrobot_run -path ./examples/example1.txt --verbose
